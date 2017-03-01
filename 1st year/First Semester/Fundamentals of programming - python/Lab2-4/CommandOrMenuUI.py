from CommandUI import mainCommand
from MenuUI import mainMenu

while True:
    command = input("Please type 'command' in order to access the command UI or 'menu' in order to access the menu UI : ")
    if command == 'command':
        mainCommand()
        break
    elif command == 'menu':
        mainMenu()
        break
