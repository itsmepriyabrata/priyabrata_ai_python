import speech_recognition as sr
import pyttsx3
def recognize_name():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Initialize text-to-speech engine
    engine = pyttsx3.init()
    
    # Set the rate of speech
    engine.setProperty('rate', 150)
    
    # Set the volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)
    
    # Use the system's default voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # You can change the index to select a different voice
    
    try:
        with sr.Microphone() as source:
            print("Say your name...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
            audio = recognizer.listen(source, timeout=5)  # Listen for 5 seconds
            
            print("Recognizing...")
            name = recognizer.recognize_google(audio)  # Recognize the speech using Google Speech Recognition
            print("You said:", name)
            engine.say(f"Hello {name}, nice to meet you!")  # Speak out a personalized greeting
            engine.runAndWait()
            
    except sr.UnknownValueError:
        print("Sorry, could not understand your name.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Error: {0}".format(e))

if __name__ == "__main__":
    recognize_name()
