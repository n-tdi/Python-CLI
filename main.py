import colors, commands # import base modules for color and handling commands

print(colors.OKGREEN + " - type help for more information - \n") # Informational print statement 

# Loop to constantly run
while True:
    
    command = input(colors.OKBLUE + "> " + colors.FAIL) # Terminal prmopt for user

    print("") # Top spacing

    commands.handleCommand(command) # Handle the sent command

    print(colors.ENDC) # Bottom Spacing