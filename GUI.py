import tkinter as tk
import threading

class AI_GUI:
    def __init__(self, root, parse_command, speak, trigger_phrase):
        self.root = root
        self.root.title("AI Assistant Graphical Interface")
        
        self.label = tk.Label(root, text="🖥️", font=("Arial", 140, "bold"))
        self.label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.label.pack()

        self.parse_command = parse_command
        self.speak = speak
        self.trigger_phrase = trigger_phrase
        self.is_listening = False

        threading.Thread(target=self.listen_for_commands).start()

    def listen_for_commands(self):
        while True:

            command = self.parse_command()
            if command:
                self.change_emoji_color("white")
                self.handle_command(command)
                self.change_emoji_color("red")
    
    def handle_command(self, command):
        if command[0] == self.trigger_phrase:
            command.pop(0)

            if command[0] == 'say':
                response = ' '.join(command[1:])
                self.speak(response)
           

    def change_emoji_color(self, color):
        self.label.config(fg=color)


