import copy
class Client:
    def __init__(self, repo):
        self.__repo = []
        self.__repo = copy.deepcopy(repo)



    @property
    def id(self):
        return self.clientId

    @id.setter
    def id(self, arg):
        self.clientId = arg


    def List(self):
        for i in self.__repo.getAll():
            print(i)

    def VerifyID(self, id):
        '''
        Verifies if there exists the given id into the list.
        '''
        return self.__repo.CheckId(id)

    def AddNewClients(self, id, name):
        '''
        Adds a new client to the list
        '''
        while True:
            try:
                id = int(id)
                if self.__repo.CheckId(id):
                    break
                else:
                    return False
            except ValueError:
                return False

        if len(name) > 0:
            self.__repo.add(id, name)
            return True
        else:
            return False

    def RemoveClients(self, id, Rentals):
        '''
        Removes a client from the list
        '''
        while True:
            if len(self.__repo.getAll()) == 0:
                return False
            try:
                id = int(id)
                if not self.__repo.CheckId(id):
                    break
                else:
                    return False
            except ValueError:
                return False

        self.__repo.remove(id)

        for i in Rentals.getAllRentals():
            if i.bookID == id:
                i.removeClientId(id)
                break
        return True

    def ModifyName(self, ID, newName):
        '''
        Modifies the name of a client
        '''
        while True:
            try:
                ID = int(ID)
                if not self.__repo.CheckId(ID):
                    break
                else:
                    return False
            except ValueError:
                return False
        if len(newName) > 0:
            self.__repo.updateName(ID ,newName)
            return True
        else:
            return False

    def ModifyID(self, ID, newId):
        '''
        Modifies the ID of a client
        '''
        while True:
            try:
                ID = int(ID)
                if not self.__repo.CheckId(ID):
                    break
                else:
                    return False
            except:
                return False

        while True:
            try:
                newId = int(newId)
                if self.__repo.CheckId(newId):
                    break
                else:
                    return False

            except ValueError:
                return False


        self.__repo.updateID(ID, newId)
        return True

    def saveTEXT(self, fileName):
        '''
        Calls the function from the repository that saves the file
        '''
        return self.__repo.writeClientsText(fileName)

    def saveDB(self, c, conn):
        return self.__repo.writeClientsDatabase(c, conn)

    def savePICKLE(self, fileName):
        '''
        Calls the function from the repository that saves the file
        '''
        return self.__repo.writeClientsPickle(fileName)

    def SearchClients(self, Name):
        '''
        Searches for clients having a certain name/part of name
        '''
        list = []
        if len(Name) > 0:
            Name = Name.lower()
            ok = False
            for i in self.__repo.getAll():
                if i.name.lower().find(Name) != -1:
                    list.append(i)
                    ok = True
            if ok == True:
                return list
            else:
                return False
        else:
            return False

    def PrintClients(self):
        '''
        Prints clients descending by the number of days they rented a book
        '''
        newList = []
        for i in self.__repo.getAll():
            if i.days > 0:
                newList.append(i)
        if len(newList) == 0:
            return
        newList.sort(key=lambda newList: newList.days, reverse=True)
        return newList
        # for i in newList:
        #     print(str(i) + ", Active for : " + str(i.days))

    def UpdateStatistics(self, clientId, days):
        '''
        Updates the statistics of a client
        '''
        ok = False
        for i in self.__repo.getAll():
            if i.id == clientId:
                i.IncrementDays(days)
                ok = True
        if ok == True:
            return True
        return False



    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__repo


    def setRepo(self, newRepo):
        self.__repo.ItemsInRepo(newRepo)

    def getClients(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__repo.getAll()

    def getLen(self):
        '''
        Returns the length of the list
        '''
        return len(self.__repo.getAll())
