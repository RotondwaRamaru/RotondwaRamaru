#Contact page
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        comments = request.form['comments']

        return render_template('contact_success.html', name=name)

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
