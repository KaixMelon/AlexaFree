from flask import Flask, send_from_directory
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "✅ Bot is running."

# Route to serve the video
@app.route('/tutorial.mp4')
def tutorial_video():
    return send_from_directory('.', 'tutorial.mp4')  # serve from current dir

def keep_alive():
    t = Thread(target=lambda: app.run(host='0.0.0.0', port=8080))
    t.start()

