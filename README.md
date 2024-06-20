# Python AI Assistant

This Python AI Assistant project is designed to perform various tasks based on voice commands. It utilizes speech recognition and text-to-speech conversion, as well as web browsing, API integration and many others. 

### Features
1. Voice Commands: The assistant responds to voice commands prefixed with the trigger phrase "computer".
2. Web Navigation: User can instruct the assistant to open specified websites in selected browsers, or allow it to automatically open links in the default web browser.
3. Weather Information: By specifying a city and preferred measurement system (metric or imperial), the assistant fetches current weather data from the OpenWeatherMap API. It can also provide extended weather information upon request.
4. Date and Time: User can ask for the current date.
5. To-Do List Management: The assistant allows users to add, remove, and view tasks in their to-do list.
6. Wikipedia Search: User can ask the assistant to search for information on Wikipedia.
7. Note-taking: The assistant can record and save notes provided by the user.
8. Calculations: User can ask the assistant to perform calculations using Wolfram Alpha's computational engine.
9. GUI (Feauture in progress): The assistant can appear in a separate GUI window whenever started (currently in testing in other-features branch)


### Requirements
- Pyaudio wheel matching your Python version (the project was made on Python 3.10) I recommend 3.8+
(If you're struggling to find the PyAudio wheel file matching your python version you can try getting it from this web archive site: https://web.archive.org/web/20230901035327/https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio the original site)
- API keys for wolframalpha and openweather
- Libraries: speech_recognition, pyttsx3, webbrowser, wikipedia, wolframalpha, requests

### Setup

1. Install Dependencies and Pyaudio wheel file (add Pyaudio file to your project path)
```bash
pip install pyaudio
pip install .\PyAudio-0.2.13-cp310-cp310-win_amd64.whl
```
2. Add your API Keys to creds.py
3. Run the Program:
```bash
python voice_assistant.py
```
4. Activate the Assistant by saying the trigger phrase "computer," followed by your command


**Future features**
- Update and change GUI for main branch
- More complex to do list
- more functions