#FAQ page
from flask import Flask, render_template

app = Flask(__name__)

faq_data = {
    "Q1": "What is Python?",
    "A1": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "Q2": "How do I install Flask?",
    "A2": "You can install Flask using the command: pip install Flask",
}

@app.route('/faq')
def faq():
    return render_template('faq.html', faq_data=faq_data)

if __name__ == '__main__':
    app.run(debug=True)
