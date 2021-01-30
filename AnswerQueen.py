import pyttsx3, wikipedia, webbrowser as wb, wolframalpha 

#Property.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 For Male Voice
client  = wolframalpha.Client('9LXRT5-WHYX7PK8HX') # This Unique Key is Generated From wolframalpha

# Speaks The Audio.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Working of the app.
while True:
    try:
        try:
            query = str(input("\n     Query: ")).lower()
            if 'wiki' in query or 'wikipedia' in query:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    print(f'\n {results}')
                    speak(results)
                except:
                    speak("Unable to Get Wiki Results! Checkout Google!")
                    wb.open(f'www.google.com/search?q={query}')
            else:      
                res = client.query(query)
                output = next(res.results).text 
                print(f'\n{output}\n')
                speak(output)
        except Exception:
            results = wikipedia.summary(query, sentences=2)
            print(f'\n{results}')
            speak(results)
    except Exception:
        print('\nResults Not Found! Checkout Google.\n')
        speak('Sorry! Results Not Found! Checkout Google.')
        wb.open(f'www.google.com/search?q={query}')