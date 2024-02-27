"""imports from the flask module"""
from flask import Flask, render_template

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
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
