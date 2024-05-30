# Python AI Assistant

This Python AI Assistant project is designed to perform various tasks based on voice commands. It utilizes speech recognition and text-to-speech conversion, as well as web browsing, API integration and many others. 

### Features
1. Voice Commands: The assistant responds to voice commands prefixed with the trigger phrase "computer".

2. Web Navigation: Users can instruct the assistant to open specified websites in selected browsers, or allow it to automatically open links in the default web browser.

3. Weather Information: By specifying a city and preferred measurement system (metric or imperial), the assistant fetches current weather data from the OpenWeatherMap API. It can also provide extended weather information upon request.

4. Date and Time: Users can ask for the current date.

5. To-Do List Management: The assistant allows users to add, remove, and view tasks in their to-do list.

6. Wikipedia Search: Users can ask the assistant to search for information on Wikipedia.

7. Note-taking: The assistant can record and save notes provided by the user.

8. Calculations: Users can ask the assistant to perform calculations using Wolfram Alpha's computational engine.


### Requirements
- Pyaudio wheel matching your Python version (the project was made on Python 3.10) I recommend 3.8+
- API keys for wolframalpha and openweather
- Libraries: speech_recognition, pyttsx3, webbrowser, wikipedia, wolframalpha, requests

### Setup

1. Install Dependencies and Pyaudio wheel
2. Add your API Keys to creds.py
3. Run the Program:
```bash
python voice_assistant.py
```
4. Activate the Assistant by saying the trigger phrase "computer," followed by your command


**Future features**
- GUI
- More complex to do list
- more functions