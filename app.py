"""imports from the flask module"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    """Home page"""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
