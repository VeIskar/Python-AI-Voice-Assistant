from datetime import datetime
import speech_recognition as srec
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha


#text to speech engine
engine_srec = pyttsx3.init()
voices = engine_srec.getProperty('vocies')  #library of voices you can use for AI assistant
engine_srec.setProperty('vocie', voices[1].id) #[1] female [0] male
trigger_phrase = 'computer' #word to activate assistant

def speak(text, rate=120):  
    engine_srec.setProperty('rate', rate)
    engine_srec.say(text)
    engine_srec.runAndWait()
    #method leverages text to speech 


#listen to commands
def parseCommand():
    listener = srec.Recognizer() # parse the voice to text
    print('Listening for commands')

    with srec.Microphone() as source:
        listener.pause_threshold = 2 #length of pause while speaking
        input_speech=listener.listen(source)

    try:
        print('Recognizing speech')
        query = listener.recognize_whisper(input_speech, language ='en_gb') #whisper api to convert to text
        print(f'Recognized input speech was {query} ')
    except Exception as exp:
        print('Sorry I cannot recognize this, could you repeat?')
        speak('Sorry I cannot recognize this, could you repeat?')

        print(exp)
        return 'None'
    return query

#parser
#main loop

if __name__ == '__main__':
    speak('Awaiting instructions', 120)

    #commands listening loop
    while True:
        #parse as list
        query = parseCommand.lower().split()

        if query[0] == trigger_phrase:
            query.pop(0)

            #commands
            if query[0] == 'say':

                if 'hello' in query:
                    speak('Greetings everyone.')
                else:
                    query.pop(0) #remove say
                    speech =' '.join(query)

                    speak(speech)

