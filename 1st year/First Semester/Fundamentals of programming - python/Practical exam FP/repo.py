class Repository:
    __repo = []
    def __init__(self, fileName):
        self.__repo = []
        self.fileName = fileName
        self.AddFromTXT(fileName)

    def addProposition(self, proposition):
        '''
        Adds a proposition in repository
        '''
        self.__repo.append(proposition)

    def getAll(self):
        '''
        Returns the list
        '''
        return self.__repo

    def getFileName(self):
        '''
        Returns the file name
        '''
        return self.fileName

    def AddFromTXT(self, file):
        '''
        Adds the content of a file in the repository
        '''
        try:
            with open(file) as f:
                content = f.read().splitlines()
                for line in content:
                    self.verifyPropositionFromText(line)
        except:
            print("There was an error")

    def writeText(self, fileName):
        '''
        Writes the list in the specifyed file
        '''
        f = open(fileName, "w")
        try:
            for p in self.__repo:
                pString = str(p) + '\n'
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))


    def verifyPropositionFromText(self, proposition):
        '''
        Used to verify the proposition taken from the text file
        '''
        if len(proposition) < 1:
            return False
        params = proposition.split(" ")
        for i in params:
            if len(i) < 3:
                return False
        for i in self.__repo:
            if i == proposition:
                return False
        self.addProposition(proposition)
        return True