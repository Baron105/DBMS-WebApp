"""imports from the flask module"""
from flask import Flask, render_template,redirect,request,url_for,flash
import psycopg2


    

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """Login page"""
    flag = 0
    
    # flags to know if the user is a student or an organiser or a participant
    organise = 1
    student = 1
    
    
    if request.method == 'POST':
        cursor = conn.cursor()
        username = request.form['username']
        username = username[6:]
        
        try :
            username = int(username)
        except :
            flag = 1
            return render_template('login.html',flag = flag)
        password = request.form['password']
        
        fest_id = 0
        print(username, password)
        
        if(username > 1000) :
            organise = 0
            student = 0
            cursor.execute(f"SELECT fest_id from ext_participant where fest_id = '{username}' and pass = '{password}'")
            fest_id = cursor.fetchone()
        else :
            cursor.execute(f"SELECT fest_id from student where fest_id = '{username}' and pass = '{password}'")
            fest_id = cursor.fetchone()
            cursor.execute(f"SELECT fest_id from organising where fest_id = '{username}'")
            fest_id_organise = cursor.fetchone()
            if fest_id_organise is not None:
                organise = 1
            else:
                organise = 0
            
        
        cursor.close()
        if fest_id is not None:
            fest_id = fest_id[0]
            return redirect(url_for('index',fest_id = fest_id,organise = organise,student = student))
        else:
            flag = 1
            return render_template('login.html',flag = flag)
    
    else :
        return render_template('login.html')

@app.route('/index/<int:fest_id>/<int:organise>/<int:student>', methods = ['GET', 'POST'])
def index(fest_id,organise,student):
    """INDEX page"""
    
    
    
    cursor = conn.cursor()
    
    participating_event = []
    non_participating_event = []
    
    if fest_id > 1000 :
        cursor.execute(f"SELECT event_name,event_date,event_time,event_venue,event_winner from event NATURAL JOIN participating_ext where fest_id = {fest_id}")
        participating_event = cursor.fetchall()
    
        cursor.execute(f"SELECT event_name,event_date,event_time,event_venue from event where event_id not in (select event_id from participating_ext where fest_id = {fest_id})")
        non_participating_event = cursor.fetchall()
    
    else :
        cursor.execute(f"SELECT event_name,event_date,event_time,event_venue,event_winner from event NATURAL JOIN participating_int where fest_id = {fest_id}")
        participating_event = cursor.fetchall()
    
        cursor.execute(f"SELECT event_name,event_date,event_time,event_venue from event where event_id not in (select event_id from participating_int where fest_id = {fest_id})")
        non_participating_event = cursor.fetchall()
        
    
    print(participating_event)
    print(non_participating_event)    
    
    return render_template('index.html',fest_id = fest_id,organise = organise,student = student,participating_event = participating_event,non_participating_event = non_participating_event)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    """Register page"""
    flag = 0
    if request.method == 'POST':
        
        cursor = conn.cursor()
        
        # get the largest fest_id from ext_participant table
        cursor.execute("SELECT fest_id from ext_participant order by fest_id desc limit 1")
        fest_id  = 0
        fest_id = cursor.fetchone()
        fest_id = fest_id[0]

        #if fest_id is None, then set fest_id to 1001
        if fest_id is None:
            fest_id = 1000
        
        
        username = request.form['name']
        password = request.form['password']
        confirm_password = request.form['repassword']
        college = request.form['college']
        
        print(fest_id,username, password, confirm_password, college)
        
        if password == confirm_password:
            cursor.execute(f"SELECT acc_id  from accomodation order by capacity desc  limit 1")
            acc_id = cursor.fetchone()
            acc_id = int(acc_id[0])
            fest_id = fest_id + 1
            cursor.execute(f"INSERT into ext_participant VALUES ({fest_id},'{username}','{college}',{acc_id},'{password}')")
            conn.commit()
            cursor.execute(f"UPDATE accomodation SET capacity = capacity - 1 WHERE acc_id = {acc_id}")
            conn.commit()
            cursor.close()
            
            flag = 1
            return render_template('register.html',flag = flag ,fest_id = fest_id)
        else:
            # add the part where user is asked to enter again 
            return redirect(url_for('register'))
        
    else : 
        return render_template('register.html')

if __name__ == '__main__':
    # connect to the database
    conn = psycopg2.connect(
        dbname="21CS30032",
        user = "21CS30032", 
        password="21CS30032",
        host="10.5.18.70",
        port="5432"
    )

    app.secret_key = 'secret'

    app.run(debug=True)