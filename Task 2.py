#imort the libraries
from gtts import gTTS
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import os
import random
import segno

#let us create listen function
def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()
    #we will take micro phone as source
    with sr.Microphone() as source:
        print("Ika modaledadamma")
        audio = r.listen(source,phrase_time_limit = 10)
    #we need to give our text as voice
    data = ""
    #here we will give exceptions (try,except)
    try:
        data = r.recognize_google(audio)
        print("You said: ",data)
    except sr.UnknownValueError as e:
        print("Request Failed")
    except sr.RequestError as e:
        print("sariga matladu , nuvvu chepindi ardhamkale")
    return data

def generate_developer_qr():
    """Generate Developer Profile QR Code"""

    profile = """
            ================================
                    DEVELOPER PROFILE
            ================================
            Name: Kalahasthi Rohith

            Role: Python Full Stack

            Skills:
            C (Programming Language)
            HTML
            CSS
            JavaScript
            Python
            IOT

            Email:
            krohith2205@gmail.com

            LinkedIn:
            https://github.com/krohith2205-alt

            GitHub:
            https://www.linkedin.com/in/k-rohith-33a230297/

            ================================
                    THANK YOU!
            ================================
            """

    # Create QR code
    qr = segno.make(profile)

    # Save QR code
    qr.save("developer_profile.png", scale=10)

    print("Developer Profile QR Code Created Successfully!")

def respond(String):
    """Function to respond back"""
    print(String)
    tts = gTTS(String)
    tts.save("Speech.mp3")
    #we are using uuid --> to randomize the content in the
    #audio file
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#here we will amke our virtual assistant into action

def va(data):
    """Our Virtual Assistant with the actions"""
    if "how are you" in data:
        listening = True
        respond("I'm fine, nuvvu ala vunav")
    elif "QR" in data:
        respond("Okay, generating your developer profile QR code.")
        generate_developer_qr()
        respond("Developer profile QR code has been generated successfully.")
        # Open QR image automatically
        os.startfile("developer_profile.png")
    elif "number game" in data:
        listening = True
        respond("Okay, let's play a number guessing game. I have selected a number between 1 and 20.")
        number = random.randint(1, 20)
        for i in range(3):
            respond("Guess the number")
            guess_data = listen()
            try:
                guess = int(guess_data)
                if guess == number:
                    respond("Congratulations! You guess the correct number.")
                    break
                elif guess < number:
                    respond("Your guess is too low. Try again.")
                else:
                    respond("Your guess is too high. Try again.")

            except ValueError:
                respond("Please say a valid number.")

        else:
            respond("Sorry, you lost the game. The number was " + str(number))
        
    try:
        return listening
    except UnboundLocalError as e:
        print("sariga matladu koncham")
        
respond("hi rohith.. , we will go to movie")
listening = True
while listening:
    data = listen()
    listening = va(data)
