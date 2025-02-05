from flask import Flask, render_template, jsonify
from voice_recognition.voice_command import recognize_voice_command  # Import the voice recognition function

app = Flask(__name__)

# Define your map-related routes
@app.route('/')
def home():
    return render_template('index.html')  # Render the map on the home page

@app.route('/voice-command')
def voice_command():
    command = recognize_voice_command()  # Call the voice recognition function
    return jsonify({"command": command})  # Return the recognized command as JSON

if __name__ == '__main__':
    app.run(debug=True)
