Voice Recognition Tool

Overview

This is a Voice Recognition Tool created using Python that acts similarly to a personal assistant like Alexa. The tool listens to voice commands from the user and performs specific actions on the computer such as opening YouTube, searching on Google, or telling the current time. It leverages various Python libraries to process speech input and execute system commands.

Features

Speech Recognition: The tool listens for voice commands and interprets them to perform specific tasks.
Voice Commands: Supports commands like opening websites (e.g., YouTube, Google) or fetching the current time.
Keyboard-Free Interaction: No need to use the keyboard or mouse; just speak the commands to execute actions.
Extensible: Can be easily expanded to include additional commands for more functionality.

How It Works

The tool continuously listens for voice input using the microphone.
Once a command is recognized, it processes the voice input using speech recognition.
It matches the input to a predefined list of actions, such as:
Opening YouTube or Google in a web browser.
Fetching and announcing the current time.
Can be extended to other commands like opening specific applications, weather updates, etc.
The tool then performs the corresponding task based on the recognized command.

Voice Commands

Here are a few example commands the tool supports:

"Open YouTube": Opens the YouTube homepage in the default web browser.
"Search Google for {query}": Performs a Google search for the specified query.
"What time is it?": Announces the current system time.
"Quit": Exits the program.

Required Libraries

The tool utilizes the following Python libraries:

SpeechRecognition: To convert speech input into text.
pyttsx3: For text-to-speech functionality, allowing the assistant to respond back.
webbrowser: To open web pages like YouTube or Google.
datetime: To fetch and announce the current time.
