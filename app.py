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
        
        
        if(username > 1000) :
            organise = 0
            student = 0
            cursor.execute(f"SELECT fest_id from ext_participant where fest_id = '{username}' and pass = '{password}'")
        else :
            
            cursor.execute(f"SELECT fest_id from student where fest_id = '{username}' and pass = '{password}'")
        fest_id = cursor.fetchone()
        
        cursor.close()
        if fest_id is not None:
            fest_id = fest_id[0]
            return render_template('home.html',fest_id = fest_id)
        else:
            flag = 1
            return render_template('login.html',flag = flag)
    
    else :
        return render_template('login.html')



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
            
            # write a popup to show the username of the user using flash
            flash(f'Account created for 24FEST{fest_id}!', 'success')
            
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