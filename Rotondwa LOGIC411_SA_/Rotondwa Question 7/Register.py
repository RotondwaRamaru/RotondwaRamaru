#Register
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        surname = request.form['surname']
        id_number = request.form['id_number']
        icas_number = request.form['icas_number']
        password = request.form['password']

        if any(user['username'] == username for user in users):
            return "Username already exists. Please choose a different one."

        users.append({'username': username, 'surname': surname, 'id_number': id_number, 'icas_number': icas_number, 'password': password})

        return redirect(url_for('registration_success', username=username))

    return render_template('register.html')

@app.route('/registration-success/<username>')
def registration_success(username):
    return f"Registration successful! Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
