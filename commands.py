import colors # For adding color to terminal
import data # Useful methods for storing data and using it

history = [] # List of all session run commands

# Called when a new command is sent
def handleCommand(command):
    addToHistory = True # Checks if command should be added to the history

    # Split command to first word incase there are arugments
    prefix = command.split(" ", 2)[0];

    if prefix == "exit": # Exit the terminal
        data.saveHistorytoFile(history) # Save the command history to a file

        sendOutput("Goodbye!\n" + colors.ENDC)
        exit() # Exit out of the program

    elif prefix == "history": # View command history        
        addToHistory = False # Make command not saved to history

        for command in history:
            sendOutput("\t" + command)

    elif prefix == "full-history":
        addToHistory = False # Make command not saved to history

        data.saveHistorytoFile(history) # Save the current history so the user can see it live

        for line in data.getTotalHistory(): # loop through all the lines in history.txt
            sendOutput("\t" + line.replace("\n", "")) # Print out each line and remove the stored '\n'

    elif prefix == "say": # Repeat back what the user sent to the console
        command.split(' ', 1)
        sendOutput(command.split(' ', 1)[1])

    elif prefix == "whereami": # Get location data of the user
        json = data.jsonObject('https://ipinfo.io') # Loads json object from 
        
        sendOutput("IP - " + colors.WARNING + json["ip"]) # Send output of IP
        sendOutput("CITY - " + colors.WARNING + json["city"]) # Send output of CITY
        sendOutput("REGION - " + colors.WARNING + json["region"]) # Send output of REGION
        sendOutput("Longitude/Latitdude - " + colors.WARNING + json["loc"]) # Send output of Longitude/Latitdude

    elif prefix == "cowsay": # Say your message, but with a cow!
        command.split(' ', 1) # Split the command without the prefix
        data.cowSay(command.split(' ', 1)[1]) # Call the cowsay function to print out a cow's message

    elif prefix == "help": # Helpful commands
        sendOutput("\texit\n\thistory\n\tfull-history\n\tsay\n\twhereami\n\thelp")

    else: # Not a valid command
        addToHistory = False # Make command not saved to history
        sendOutput("Command not found!") 

    if addToHistory == True:
        history.append(prefix) # Add command to history

# Send text back to terminal with fancy formatting
def sendOutput(text):
    print(colors.OKGREEN + text) # give top and bottom space for message, and restting color if last command
