#Learning page
from flask import Flask, render_template

app = Flask(__name__)

topics = [
    {"name": "Python", "image_url": "https://example.com/python_image.jpg"},
    {"name": "HTML and CSS", "image_url": "https://example.com/html_css_image.jpg"},
    {"name": "JavaScript", "image_url": "https://example.com/javascript_image.jpg"},
    {"name": "Java", "image_url": "https://example.com/java_image.jpg"},
    {"name": "C#", "image_url": "https://example.com/csharp_image.jpg"},
    {"name": "Unity", "image_url": "https://example.com/unity_image.jpg"},
    {"name": "Photoshop", "image_url": "https://example.com/photoshop_image.jpg"},
    {"name": "Digital Marketing", "image_url": "https://example.com/digital_marketing_image.jpg"}
]

@app.route('/learning')
def learning():
    return render_template('learning.html', topics=topics)

if __name__ == '__main__':
    app.run(debug=True)
