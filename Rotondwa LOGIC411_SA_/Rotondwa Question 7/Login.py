#Login
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [{'username': 'tragedy_07', 'password': 'password123'}]

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    
    username = request.form['username']
    password = request.form['password']
    remember_me = 'remember_me' in request.form

    user = next((user for user in users if user['username'] == username and user['password'] == password), None)

    if user:
        return f"Welcome, {username}! Remember Me: {remember_me}"
    else:
        return "Invalid username or password"

if __name__ == '__main__':
    app.run(debug=True)
