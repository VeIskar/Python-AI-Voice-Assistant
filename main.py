import datetime
from datetime import date
import speech_recognition as srec
import pyttsx3
import webbrowser
import browsers
import wikipedia
import wolframalpha
import sys
import requests
#API keys
import creds
#GUI
from GUI import AI_GUI
import threading
import tkinter as tk

#text to speech engine
engine_srec = pyttsx3.init()
voices = engine_srec.getProperty('voices')  #library of voices you can use for AI assistant
engine_srec.setProperty('voice', voices[1].id) #[1] female [0] male
trigger_phrase = 'computer' #word to activate assistant

#browsers
browsers_list=['chrome', 'firefox','edge']


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

    if browser == 'chrome':
        browsers.launch("chrome", url=f"https://{query}")   
    elif browser =='firefox':
        browsers.launch("firefox", url=f"https://{query}")
    elif browser =='edge':
        browsers.launch("msedge", url=f"https://{query}")


#ending program
def exit_program(query):
    speak("Shutting down the assistant, goodbye")
    raise SystemExit   

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

        if browser_selected in browsers_list:
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


#searching the wikipedia method
def search_wikipedia(query = ''):
    search_results = wikipedia.search(query) #array of results

    if not search_results:
        print('No result found for users query')
        return 'No result received'
    try:    #getting the first result from array
        wikipedia_page = wikipedia.page([search_results[0]])

    except wikipedia.DisambiguationError as error:
        wikipedia_page = wikipedia.page(error.options[0])
        #in case there is an Disambiguation Error and many results we take the still take the first

    print(f"{wikipedia_page.title} chosen as primary query of interest")

    #AI will read the summary of what the wikipedia page is about
    page_sum = str(wikipedia_page.summary)
    return page_sum


#Wolfram Alpha
wolframClient = wolframalpha.Client(creds.app_id_wolfram)

#Weather api
weather_key = creds.app_id_weather


#add different func for checking query_mes_sys and extended info about weather
def temp_sys(query_mes_sys = ''):
    if query_mes_sys == 'metric':
        print("metric system chosen")
        return 'metric'
    elif query_mes_sys == 'imperial':
        print("imperial system chosen")
        return 'imperial'
    else:
        print("unknown system")
        return 'error'


def weather_func(query = '', query_mes_sys = '', query_ext = ''):
    if query_mes_sys == 'error':
        print('measurement system error: unknown system')
        return 'unknown measurement system'

    w_req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={query}&units={query_mes_sys}&APPID={weather_key}")  
    #uses requests lib to fetch the url
    td = datetime

    try:
        if w_req.json()['cod'] == '404':
            print("no city found")
            return "No city found"  
        else:
            #base data which we want to retrive:
            weather_data = w_req.json()['weather'][0]['description']
            temp_data = round(w_req.json()['main']['temp'])


            #extended data:
            humidity = w_req.json()['main']['humidity']
            feels_like = w_req.json()['main']['feels_like']
            sunrise = td.datetime.utcfromtimestamp(w_req.json()['sys']['sunrise']).strftime('%H:%M')
            sunset = td.datetime.utcfromtimestamp(w_req.json()['sys']['sunset']).strftime('%H:%M')
            windspeed = w_req.json()['wind']['speed']

            #formated_td = td.strftime('%B %d, %Y')

            if query_ext == 'yes':

                if query_mes_sys == 'metric':
                    speak(f"The weather in {query} is {weather_data} and the temperature is {temp_data}ºC")
                    #ext info
                    speak(f'The temperature in {query} feels like {feels_like} Humidity is {humidity},'+ 
                            f'windspeed is {windspeed}, sunrise begins at: {sunrise} and sunset at: {sunset} ')
                    
                    print(f"Chosen city: {query}, weather: {weather_data}, temperature{temp_data}ºC in metric units")
                    #ext info
                    print(f'{query} feels like: {feels_like} Humidity: {humidity}, windspeed: {windspeed}, sunrise: {sunrise} sunset: {sunset} ')
                        
                
                if query_mes_sys == 'imperial':
                    speak(f"The weather in {query} is {weather_data} and the temperature is {temp_data}ºF")
                    #ext info
                    speak(f'The temperature in {query} feels like {feels_like} Humidity is {humidity},'+ 
                            f'windspeed is {windspeed}, sunrise begins at: {sunrise} and sunset at: {sunset} ')
                    
                    print(f"Chosen city: {query}, weather: {weather_data}, temperature{temp_data}ºF in imperial units")
                    #ext info
                    print(f'{query} feels like: {feels_like} Humidity: {humidity}, windspeed: {windspeed}, sunrise: {sunrise} sunset: {sunset} ')
            
            else:
                if query_mes_sys == 'metric':
                    speak(f"The weather in {query} is {weather_data} and the temperature is {temp_data}ºC")
                    print(f"Chosen city: {query}, weather: {weather_data}, temperature{temp_data}ºC in metric units")
                if query_mes_sys == 'imperial':
                    speak(f"The weather in {query} is {weather_data} and the temperature is {temp_data}ºF")
                    print(f"Chosen city: {query}, weather: {weather_data}, temperature{temp_data}ºF in imperial units")
                
    
    #API errors
    except requests.RequestException as req_exp:
        print(f"Error while fetching weather data: {req_exp}")
        return "An error occured while fetching weather data"
    except KeyError as key_error:
        print(f"KeyError in weather response: {key_error}")
        return "Error processing weather data or API key"
    except Exception as e:
        print(f"unexpected/unknown error occurrence: {e}")
        return "An unexpected error occurred"
    

#todolist
#implementation prop. 2: add separate functions for specified tasks for better modularity
list_of_items = []
def to_do_list(query=''):

    global list_of_items

    if 'check' in query:
        return list_tasks(list_of_items)
    
    if 'add' in query:
        add_task(query,list_of_items)
        return(f"Adding {query[1:]} to the list")
        
    if ("remove") in query:
        remove_task(query,list_of_items)
        return (f"Removing {query[1:]} from list")
    

#listing the content of the list
def list_tasks(list_of_items):
    if list_of_items:
        print("current tasks in list:")
        for i, item in enumerate(list_of_items, start=1):
            print(i, item)
            speak (f"{i} {item}")
        return "Those are the current tasks"
    else:
        print("List is empty")
        return "List is empty"
        

#add new task to the list
def add_task(query,list_of_items):
    task=' '.join(query[1:])
    list_of_items.append(task)
    print(f"added task: {task}")

#removing task from the list
def remove_task(query,list_of_items):
    task = ' '.join(query[1:])

    for item in list_of_items:
        if item == task:
            list_of_items.remove(task)
            print(f"removed task {query}")
            break
        return "task removed"
    else:
        print("Task doesnt exist")
        return "Task doesnt exist"  

#wolfram result
def dict_or_list(var):
    if isinstance(var,list):
        return var[0]['plaintext']
    else:
        return var['plaintext'] #plain dict




def calc_wolfram_a(query = ''):
    response = wolframClient.query(query)

    try:
        if response['@success'] == 'false':
            return 'Could not compute'

        else:
            result = ''
            #question

            pod_0 = response['pod'][0]
            pod_1 = response['pod'][1]

            #highest confidence value - possible answer
            #if its primary or has the title of result or def -> its official result
            if (('result') in pod_1['@title'].lower() or (pod_1.get('primary', 'false') == 'true') or ('definition' in pod_1['@title'].lower() )):

                #result may be list or dict.
                result = dict_or_list(pod_1['subpod'])
                print("query result: ",result)

                #removing bracket section
                return result.split('(')[0]
            else:
                #get answer from pod 0
                question = dict_or_list(pod_0['subpod'])
                
                return question.split('(')[0]

                #searching wikipedia instead

                speak('Unable to compute, querying wikipedia')
                print("computation failure")
                return search_wikipedia(question)
    #API key error
    except KeyError as wolf_key_e:
        speak(f"Error occurring with Wolfram Alpha api key")
        print(f"Error occurring with Wolfram Alpha api key: {wolf_key_e}")
    except Exception as e:
        print(f"unexpected/unknown error occurrence: {e}")
        return "An unexpected error occurred"



#parser
#main loop
saved_select_br = None #the saved browser selected by user

if __name__ == '__main__':

    root = tk.Tk()
    gui = AI_GUI(root, parseCommand, speak, trigger_phrase)
    root.mainloop()
    
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
                    continue

                else:
                    query.pop(0) #remove say
                    speech =' '.join(query)

                    speak(speech)
            
            #empty browser for parsing
            selected_br = None
            
            #navigation
            if query[0]=='select' and query[1]=='browser':     
                                
                speak("In which browser you would like to open? Available browsers are: " + ', '.join(browsers_list))

                selected_br = parseBrowser()

                #saved_select_br is going to be an additional checker in case selected_br doesn't work

                if selected_br :
                    speak('Please say "computer go to" followed by the website you want to visit to activate.')
                    saved_select_br = selected_br
                    
            if saved_select_br != None :                
                if query[0] == 'go' and query[1]=='to':
                    query = ' '.join(query[2:]) #we will skip the 'go to'
                    browser_conf_open(query,saved_select_br)
            
                               
            elif  (selected_br == None) or (saved_select_br == None):
                if query[0] == 'go' and query[1]=='to':
                    speak("Please select browser first or ask for auto navigate function") 

                if query[0] == 'auto' and query[1] == 'navigate' and query[2] == 'to' : #auxiliary website navigation function 
                    
                    query = ' '.join(query[3:])
                    speak(f'Going to {query} in auto web mode')
                    webbrowser.open_new(query)
                    print('opening in emergency mode')           
            
            if query[0] == 'check':

                if query[1] == 'weather':
                    #measurement system
                    speak('Which measurement system do you prefer? Available are metric and imperial')
                    query_mes_sys = parseCommand().lower()
                    t_sys = temp_sys(query_mes_sys)

                    #extended info
                    speak('Would you like extended information about the weather? Proceed with yes or no')
                    query_ext = parseCommand().lower()

                    speak('From which city would you like to get the information about the weather?')
                    query = ' '.join(query[2:])

                    speak(weather_func(query,t_sys,query_ext))
                    continue
                           
                if 'current date' in query:
                    td=date.today()
                    formated_td = td.strftime('%B %d, %Y')   
                                    
                    speak(formated_td)
                    print(f'current date: {formated_td}')
                    continue

                    #listing items of to do list
                if query[1] in ['checklist', 'list', 'tasks', 'todo', "to do's ", 'chores', 'assignments']:
                    speak(to_do_list(query))
                    print("todo list checking")  
                    continue  
            
            #adding new task to do list
            if query[0] == 'add':
                speak(to_do_list(query))
                continue
            
            #removing task from to do list 
            if query[0] == 'remove':
                speak(to_do_list(query))
                continue

            #using wikipedia
            if 'wikipedia' in query:
                query = ' '.join(query)
                speak('Querying the wikipedia ')
                speak(search_wikipedia(query))
                print(f'returning summary about {query}')

            #taking notes
            if query[0] == 'log':
                print("taking notes mode")
                speak("recording your note")

                note_new = parseCommand().lower()
                current = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

                with open('note_%s.txt' % current, 'w' ) as newFile:
                    newFile.write(note_new)
                
                speak('Note has been written')
            
            # calculations/Wolfram commands
            if query[0] == 'calculate':
                query = ' '.join(query[1:])
                speak('Computing')
                try:
                    result = calc_wolfram_a(query)
                    speak(result)
                    print('wolfram alpha used for calculation')
                except:
                    speak('Unable to compute')
                    print('computing failed')
            
            if query[0] == 'exit':
                exit_program(query)
                print('ending the program')
                break   #get out of loop and end without triggering else
                    
            else:
                    speak("Sorry I couldn't recognize your voice. Please try again")