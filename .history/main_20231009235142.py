from datetime import datetime
import speech_recognition as srec
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha



#text to speech engine
engine_srec = pyttsx3.init()
voices = engine_srec.getProperty('voices')  #library of voices you can use for AI assistant
engine_srec.setProperty('voice', voices[1].id) #[1] female [0] male
trigger_phrase = 'computer' #word to activate assistant

#browsers
browsers__=['chrome', 'firefox','edge']


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
        query = listener.recognize_google(input_speech, language ='en_gb') #whisper api to convert to text
        print(f'Recognized input speech was {query} ')
    except Exception as exp:
        print('Sorry I cannot recognize this, could you repeat?')
        speak('Sorry I cannot recognize this, could you repeat?')

        print(exp)
        return 'None'
    return query

def browser_conf_open(query_, browser):
    
    speak(f'Going to {query_} in {browser} browser')

    if browser== 'chrome':
        webbrowser.get('chrome').open_new(query_)    
    elif browser=='firefox':
        webbrowser.get('mozilla').open_new(query_)
    elif browser=='edge':
        webbrowser.get('edge').open_new(query_)



#browser parsing
def parseBrowser():
    listener = srec.Recognizer() # parse the voice to text
    #speak('Listening for browser choice')

    try:
        with srec.Microphone() as source:
            listener.pause_threshold = 2
            speak('Listening for browser choice')
            audio = listener.listen(source)
        
        #speech recognition
        browser_selected = listener.recognize_google(audio).lower() # add .lower at the end 

        if browser_selected in browsers__:
            speak(f'You decided to choose {browser_selected} as the browser.')
            print(f'selected browser accepted {browser_selected}')
            return browser_selected
        else:
            speak('Browser not supported, please choose other')
            print(f'Browser {browser_selected} not supported/recognized')
            return None
    
    except srec.UnknownValueError:
            print('Could you please repeat')
            return None

#parser
#main loop

if __name__ == '__main__':
    speak('Awaiting instructions')

    #commands listening loop
    while True:
        #parse as list
        query = parseCommand().lower().split()

        if query[0] == trigger_phrase:
            query.pop(0)

            #commands
            if query[0] == 'say':

                if 'hello' in query:
                    speak('Greetings everyone.')
                    print('greeitngs sequence')
                else:
                    query.pop(0) #remove say
                    speech =' '.join(query)

                    speak(speech)
            
            #navigation
            if query[0]=='select' and query[1]=='browser':     
                
                #speak('Opening: ') prev
                                
                speak("In which browser you would like to open? Available browsers are: " + ', '.join(browsers__))

                selected_br = parseBrowser()

                if selected_br :
                    speak('Please say "computer go to" followed by the website you want to visit to activate.')

            elif selected_br is not None and query[0] == 'go' and query[1]=='to' :        
                query = ' '.join(query[2:]) #we will skip the 'go to'
                browser_conf_open(query,selected_br)
            elif selected_br is None:
                speak("Please select browser first")
                    
                    
            else:
                    speak("Sorry I couldn't recognize your voice. Please try again")


                #webbrowser.open_new(query) #opening page for query #prev
               