import json # Deal with json related tasks
from pathlib import Path # Import file utiles for path
import cowsay # Import fun cowsay project
import urllib.request # Request library
import colors # Color library

historyFile = "history.txt"

# Save the command history to a file
def saveHistorytoFile(history):
    historyTxt = Path(historyFile)
    historyTxt.touch(exist_ok=True)
    with open(historyFile, 'a') as f: # Open the file with write access
        for cmd in history: # Write all the lines from the history list
            f.write(cmd + "\n")

# Read the contents of history.txt
def getTotalHistory():
    historyTxt = Path(historyFile)
    historyTxt.touch(exist_ok=True)
    with open(historyFile) as f:
        return f.readlines()


# Turn api request into Json Object
def jsonObject(url):
    return json.loads(urllib.request.urlopen(url).read().decode())

# Use cowsay library to send a funny cow message
def cowSay(text):
    print(colors.OKGREEN)
    cowsay.cow(text)