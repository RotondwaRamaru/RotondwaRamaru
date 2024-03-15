#Content page
from flask import Flask, render_template

app = Flask(__name__)

topics = [
    {"name": "Python", "video_url": "https://example.com/python_video.mp4", "document_url": "https://example.com/python_document.pdf"},
    {"name": "HTML and CSS", "video_url": "https://example.com/html_css_video.mp4", "document_url": "https://example.com/html_css_document.pdf"},
]

@app.route('/content/<topic>')
def content(topic):
    selected_topic = next((t for t in topics if t['name'] == topic), None)

    if selected_topic:
        return render_template('content.html', topic=selected_topic)
    else:
        return "Topic not found"

if __name__ == '__main__':
    app.run(debug=True)
