import pyttsx3
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

while True:
    try:
        sentence = input("\nEnter : ")
        sentence = sentence.title()
        destL = input('\nDestination: ')
        destL = destL.lower()
        translated_sent = Translator().translate(sentence, src = 'en' , dest = destL)
        translated = translated_sent.text
        try:
            speak(translated)
            print(f'\n\t{sentence} in {destL} "{translated}"')
        except Exception:
            print(f'\n\t{sentence} in {destL} "{translated}"')
    except:
        print('\nERROR!')