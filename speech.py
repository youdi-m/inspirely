import pyttsx3

# initialize the engine
engine = pyttsx3.init()

# get user input
text = input("Enter the text you want to convert to speech: ")

# set the engine properties
engine.setProperty('rate', 150) # speed in words per minute
engine.setProperty('volume', 0.7) # volume between 0 and 1

# convert the text to speech
engine.say(text)
engine.runAndWait()