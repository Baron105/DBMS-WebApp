"""imports from the flask module"""
from flask import Flask, render_template, redirect, request, url_for
import psycopg2

conn = psycopg2.connect(
    dbname="21CS10048",
    user="21CS10048",
    password="21CS10048",
    host="10.5.18.69",
    port="5432",
)


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """Home page"""

    cursor = conn.cursor()
    cursor.execute("SELECT event_name, event_venue, event_date, event_time, event_type FROM event ORDER BY RANDOM() LIMIT 3;")
    events = cursor.fetchall()
    return render_template('home.html', events=events)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page"""
    flag = 0

    # flags to know if the user is a student or an organiser or a participant
    organise = 1
    student = 1

    if request.method == "POST":
        cursor = conn.cursor()
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute(f"SELECT * from admin where username = '{username}' and password = '{password}'")
        admin = cursor.fetchone()
        if(admin is not None):
            return redirect(url_for("admin"))
        
        username = username[6:]

        try:
            username = int(username)
        except():
            flag = 1
            return render_template("login.html", flag=flag)
<<<<<<< Updated upstream
        password = request.form["password"]
=======

        
>>>>>>> Stashed changes

        fest_id = 0
        print(username, password)

        if username > 1000:
            organise = 0
            student = 0
            cursor.execute(
                f"SELECT fest_id from ext_participant where fest_id = '{username}' and pass = '{password}'"
            )
            fest_id = cursor.fetchone()
        else:
            cursor.execute(
                f"SELECT fest_id from student where fest_id = '{username}' and pass = '{password}'"
            )
            fest_id = cursor.fetchone()
            cursor.execute(
                f"SELECT fest_id from organising where fest_id = '{username}'"
            )
            fest_id_organise = cursor.fetchone()
            if fest_id_organise is not None:
                organise = 1
            else:
                organise = 0

        cursor.close()
        if fest_id is not None:
            fest_id = fest_id[0]
            return redirect(
                url_for("index", fest_id=fest_id, organise=organise, student=student)
            )
        else:
            flag = 1
            return render_template("login.html", flag=flag)

    else:
        return render_template("login.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    """Admin page"""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "select event_id,event_name,event_venue,event_description,event_date,event_time,event_type from event"
        )
        events = cursor.fetchall()
    except psycopg2.Error as e:
        print(e)
        events = []
        conn.rollback()
    return render_template("admin.html", events=events)

@app.route("/index/<int:fest_id>/<int:organise>/<int:student>", methods=["GET", "POST"])
def index(fest_id, organise, student):
    """INDEX page"""

    cursor = conn.cursor()

    participating_event = []
    non_participating_event = []
    volunteering_event = []
    non_volunteering_event = []
    other_events = []
    organising_event = []
    participant_event=[]
    volunteer_event = []
    if fest_id > 1000:
        cursor.execute(
            f"SELECT event_id,event_name,event_date,event_time,event_venue,event_winner from event NATURAL JOIN participating_ext where fest_id = {fest_id}"
        )
        participating_event = cursor.fetchall()

        cursor.execute(
            f"SELECT event_id,event_name,event_date,event_time,event_venue from event where event_id not in (select event_id from participating_ext where fest_id = {fest_id})"
        )
        non_participating_event = cursor.fetchall()

    else:
        cursor.execute(
            f"SELECT event_id,event_name,event_date,event_time,event_venue,event_winner from event NATURAL JOIN participating_int where fest_id = {fest_id}"
        )
        participating_event = cursor.fetchall()

        # cursor.execute(
        #     f"SELECT event_id,event_name,event_date,event_time,event_venue from event where event_id not in (select event_id from participating_int where fest_id = {fest_id})"
        # )
        # non_participating_event = cursor.fetchall()
        #get the list of events in which the student is volunteering
        cursor.execute(f"SELECT event_id,event_name,event_date,event_time,event_venue from event where event_id in (select event_id from volunteering where fest_id = {fest_id})")
        volunteering_event = cursor.fetchall()
        #get the list of events in which the student is not volunteering
        # cursor.execute(f"SELECT event_id,event_name,event_date,event_time,event_venue from event where event_id not in (select event_id from volunteering where fest_id = {fest_id})")
        # non_volunteering_event = cursor.fetchall()
        participant_event_2 = []

            
        # merge the tables of participating, volunteering and organising events and return all the events not in these tables such that the student can participate in them
        cursor.execute(
            f"SELECT event_id,event_name,event_date,event_time,event_venue from event where event_id not in (select event_id from participating_int where fest_id = {fest_id}) and event_id not in (select event_id from volunteering where fest_id = {fest_id}) and event_id not in (select event_id from organising where fest_id = {fest_id})"
        )
        other_events = cursor.fetchall()

        #Organising events

        if organise == 1:
            
            cursor.execute(
                f"SELECT event_id,event_name,event_date,event_time,event_venue,event_winner from event where event_id in (select event_id from organising where fest_id = {fest_id})"
            )
            organising_event = cursor.fetchone()
            cursor.execute(
                f"SELECT fest_id, name from participating_ext natural join ext_participant where event_id = {organising_event[0]}"
            )

            participant_event = cursor.fetchall()
            cursor.execute(
                f"SELECT fest_id, name from participating_int natural join student where event_id = {organising_event[0]}"
            )
            participant_event += cursor.fetchall()
            cursor.execute(
                f"SELECT roll, name from volunteering natural join student where event_id = {organising_event[0]}"
            )
            volunteer_event = cursor.fetchall()
            for participant in participant_event:
                participant2 = list(participant)
                participant2[0]="24FEST"+str(participant[0]).zfill(4)
                participant_event_2.append(participant2)
    cursor.close()


    return render_template(
        "index.html",
        fest_id=fest_id,
        organise=organise,
        student=student,
        participating_event=participating_event,
        non_participating_event=non_participating_event,
        volunteering_event = volunteering_event,
        non_volunteering_event = non_volunteering_event,
        organising_event=organising_event,
        other_events=other_events,
        participant_event = participant_event_2,
        volunteer_event = volunteer_event
    )

@app.route("/winner/<int:fest_id>/<int:event_id>/<int:organise>/<int:student>/<winner_name>", methods=["GET", "POST"])
def winner(fest_id, event_id,organise,student,winner_name):
    """Winner page"""
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE event SET event_winner = '{winner_name}' WHERE event_id = {event_id}"
    )
    conn.commit()
    cursor.close()
    return redirect(url_for("index", fest_id=fest_id, organise=organise, student = student))

@app.route("/participate/<int:fest_id>/<int:event_id>/<int:organise>/<int:student>", methods=["GET", "POST"])
def participate(fest_id, event_id,organise,student):
    """Participate page"""
    cursor = conn.cursor()
    if fest_id > 1000:
        cursor.execute(
            f"INSERT INTO participating_ext VALUES ({fest_id},{event_id})"
        )
    else:
        cursor.execute(
            f"INSERT INTO participating_int VALUES ({fest_id},{event_id})"
        )
    conn.commit()
    cursor.close()
    return redirect(url_for("index", fest_id=fest_id, organise=organise, student = student))

@app.route("/volunteer/<int:fest_id>/<int:event_id>/<int:organise>/<int:student>", methods=["GET", "POST"])
def volunteer(fest_id, event_id,organise,student):
    """Volunteer page"""
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO volunteering VALUES ({fest_id},{event_id})"
    )
    conn.commit()
    cursor.close()
    return redirect(url_for("index", fest_id=fest_id, organise=organise, student = student))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register page"""
    flag = 0
    if request.method == "POST":
        cursor = conn.cursor()

        # get the largest fest_id from ext_participant table
        cursor.execute(
            "SELECT fest_id from ext_participant order by fest_id desc limit 1"
        )
        fest_id = 0
        fest_id = cursor.fetchone()
        fest_id = fest_id[0]

        # if fest_id is None, then set fest_id to 1001
        if fest_id is None:
            fest_id = 1000

        username = request.form["name"]
        password = request.form["password"]
        confirm_password = request.form["repassword"]
        college = request.form["college"]

        print(fest_id, username, password, confirm_password, college)

        if password == confirm_password:
            cursor.execute(
                "SELECT acc_id from accomodation order by capacity desc limit 1"
            )
            acc_id = cursor.fetchone()
            acc_id = int(acc_id[0])
            fest_id = fest_id + 1
            cursor.execute(
                f"INSERT into ext_participant VALUES ({fest_id},'{username}','{college}',{acc_id},'{password}')"
            )
            conn.commit()
            cursor.execute(
                f"UPDATE accomodation SET capacity = capacity - 1 WHERE acc_id = {acc_id}"
            )
            conn.commit()
            cursor.close()

            flag = 1

            return render_template('register.html',flag = flag ,fest_id = fest_id)
        else:
            # add the part where user is asked to enter again 
            flag = -1
            return render_template('register.html',flag = flag)
        
    else : 
        return render_template('register.html')


if __name__ == "__main__":
    # connect to the database

    app.secret_key = "secret"

    app.run(debug=True)