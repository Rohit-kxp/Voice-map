import speech_recognition as sr

def recognize_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command recognized: {command}")
        return command
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return "Error: Unable to understand"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "Error: Speech Recognition service failed"
