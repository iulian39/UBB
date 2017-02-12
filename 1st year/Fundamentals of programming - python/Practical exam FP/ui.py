class MenuUI:

    def __init__(self, controller, fileName):
        while True:
            self.MainMenuUI()
            command = input("Please type the command : ")
            if self.validInputCommand(command):
                if command == "0":
                    self.saveInText(controller, fileName)
                    break
                elif command == "1":
                    self.AddASentence(controller)
                elif command == "2":
                    controller.printPropositions()
                elif command == "3":
                    self.NewGame(controller)



    def NewGame(self, controller):
        newprop, proposition, hiddenLetters = controller.RandomProposition()
        str = ""
        hangmanS = controller.makeHangman()
        hangman = ['h','a','n','g','m','a','n']
        index = 0
        while str != "hangman":
            ok = False
            print(hangmanS[index] + newprop + " - " + str)
            letter = input('Please input a letter : ')
            if letter in hiddenLetters:
                newprop = controller.NewProposition(newprop, proposition, letter)
                hiddenLetters = controller.DeleteHiddenLetter(hiddenLetters,letter)
                if len(hiddenLetters) == 0:
                    print("YOU WON !")
                    return
            else:
                str += hangman[index]
                index += 1
        print(hangmanS[len(hangmanS) - 1])
        print("HANGMAN !!\nYOU LOST !")
        print("The propostion was : ", proposition)


    def AddASentence(self, controller):
        x = self.readCommand()
        controller.addProp(x)

    @staticmethod
    def saveInText(controller, fileName):
        '''
        We save the content in to the destination file
        '''
        controller.writeText(fileName)



    def readCommand(self):
        '''
        Read and parse user commands
        input: -
        output: the proposition
        '''
        cmd = input("\nPlease input a proposition : ")
        params = cmd.split(" ")
        if len(params) == 0:
            print("INVALID INPUT")
            self.readCommand()
        for i in params:
            if len(i) < 3:
                print("INVALID INPUT")
                self.readCommand()
        return cmd

    @staticmethod
    def MainMenuUI():
        str = "\nAvailable commands :\n"
        str += "\t1 - Add a new proposition\n"
        str += "\t2 - Print the existing propositions\n"
        str += "\t3 - Start a new game\n"
        str += "\t0 - Exit"
        print(str)

    @staticmethod
    def validInputCommand(command):
        '''
        Verify if the command is valid
        input: command
        output: true / false
        '''
        availableCommands = ['1','2','3','0']
        return (command in availableCommands)