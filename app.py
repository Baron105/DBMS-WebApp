"""imports from the flask module"""
from flask import Flask, render_template,redirect,request,url_for
import psycopg2

# connect to the database
conn = psycopg2.connect(
    dbname="21CS10014",
    password="21CS10014",
    host="10.5.18.68",
    port="5432"
)

# create a cursor
cursor = conn.cursor()
    

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """Login page"""
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    """Register page"""
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        confirm_password = request.form['repassword']
        college = request.form['college']
        
        print(username, password, confirm_password)
        
        if password == confirm_password:
            cursor.execute(f"SELECT acc_id  from accomodation order by desc capacity limit 1")
            acc_id = cursor.fetchone()
            cursor.execute(f"INSERT into ext_participant ('name','college','acc_id','pass') VALUES ('{username}','{college}','{acc_id}','{password}')")
            cursor.commit()
            cursor.execute(f"UPDATE accomodation SET capacity = capacity - 1 WHERE acc_id = {acc_id}")
            cursor.commit()
            return redirect(url_for('login'))
        else:
            # add the part where user is asked to enter again 
            return redirect(url_for('register'))
        
    else : 
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
