import random
class Controller:

    def __init__(self, repo):
        self.__data = repo

    def addProp(self, proposition):
        '''
        We verify if the proposition is OK
        '''
        if len(proposition) < 1:
            return False
        params = proposition.split(" ")
        for i in params:
            if len(i) < 3:
                return False
        for i in self.__data.getAll():
            if i == proposition:
                return False
        self.__data.addProposition(proposition)
        return True

    def printPropositions(self):
        '''
        Prints the propositions
        '''
        for i in self.__data.getAll():
            print(i)

    def getPropositions(self):
        '''
        Returns all the propositions from the controller
        '''
        return self.__data.getAll()

    def writeText(self, fileName):
        '''
        we transfer the control to the repository in order to save in file
        '''
        self.__data.writeText(fileName)

    def GetLettersEnd(self, randomProposition):
        '''
        Input: randomProposition
        Output: returns the list with the letters found at the endings of a word
        '''
        if len(randomProposition) == 0:
            return False
        splittedPro = randomProposition.split(" ")
        letters = []
        for i in splittedPro:
            for j in range(0, len(i)):
                ok = True
                if j == 0 or j == (len(i) - 1):
                    for k in range(0, len(letters)):
                        if i[j] == letters[k]:
                            ok = False
                    if ok == True:
                        letters.append(i[j])
        return letters

    def RandomProposition(self):
        '''
        Input: -
        Output: - Returns a random proposition from the list, the hidden letters and the new proposition(the one with _ in it)
        '''
        randomProposition = random.choice(self.getPropositions())
        lettersFromEnd = self.GetLettersEnd(randomProposition)
        savedProp = randomProposition.split(" ")
        newprop = []
        hiddenLetters = []
        for i in savedProp:
            for j in range(0, len(i)):
                if j == 0 or j == (len(i) - 1) or i[j] in lettersFromEnd:
                    newprop.append(i[j])
                else:
                    newprop.append('_')
                    hiddenLetters.append(i[j])
            newprop.append(" ")
        newprop = "".join(newprop)
        return newprop, randomProposition, hiddenLetters

    def NewProposition(self, newProposition, proposition, letter):
        '''
        Creates the new proposition
        '''
        newprop = newProposition.split()
        newprop1 = []
        saveInitialProp = proposition.split()
        for i in range(0, len(newprop)):
            for j in range(0, len(newprop[i])):
                if newprop[i][j] == '_' and letter == saveInitialProp[i][j]:
                    newprop1.append(saveInitialProp[i][j])
                else:
                    newprop1.append(newprop[i][j])
            newprop1.append(' ')
        newprop1 = "".join(newprop1)
        return newprop1

    def DeleteHiddenLetter(self, hiddenLetters, letter):
        '''
        Delets the hidden letters from a list
        '''
        for i in range(len(hiddenLetters) - 1, -1, -1):
            if hiddenLetters[i] == letter:
                del hiddenLetters[i]
        return hiddenLetters

    def makeHangman(self):
        hangmanS = []
        hangmanS.append("____________\n|\n|\n|\n|\n|\n|\n")
        hangmanS.append("____________\n|      |\n|\n|\n|\n|\n|\n")
        hangmanS.append("____________\n|      |\n|      O\n|\n|\n|\n")
        hangmanS.append("____________\n|      |\n|      O\n|      |\n|\n|\n|\n")
        hangmanS.append("____________\n|      |\n|      O\n|     /|\n|\n|\n|\n")
        hangmanS.append("____________\n|      |\n|      O\n|     /|\ \n|\n|\n|\n")
        hangmanS.append("____________\n|      |\n|      O\n|     /|\ \n|     /\n|\n|\n")
        hangmanS.append("____________\n|      |\n|      O\n|     /|\ \n|     / \ \n|\n|\n")
        return hangmanS