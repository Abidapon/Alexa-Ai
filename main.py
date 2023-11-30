import speech_recognition as sr
import pyttsx3
from datetime import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('Listening...')
            voice = listener.listen(source, timeout=10)  # Set a 10-second timeout
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except sr.WaitTimeoutError:
        print("Listening timed out. No command received.")
        command = ""
    except sr.UnknownValueError:
        print("Could not understand audio.")
        command = ""
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        command = ""

    return command


def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry brother, I am in a relationship')
    else:
        talk('please say it again')
        breakpoint()

while True:
    run_alexa()

