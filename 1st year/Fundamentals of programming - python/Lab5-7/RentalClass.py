import datetime
import copy

class Rental:
    def __init__(self, repo):
        self.__repo = []
        self.__repo = copy.deepcopy(repo)



    def List(self):
        '''
        Prints the list
        '''
        for i in self.__repo.getAll():
            print(i)


    def RentBooks(self, Books, Clients, rentID, bookID, clientID, rentDay, dueTime, returned):
        '''
        The rent fucntion allows renting the availble books
        '''
        if len(Books.getAllAvailbleBooks()) == 0:
            return False
        while True:
            try:
                rentID = int(rentID)
                if self.__repo.CheckId(rentID):
                    break
                else:
                    return False
            except ValueError:
                return False
        while True:
            try:
                clientID = int(clientID)
                if not self.CheckId(Clients.getClients(), clientID):
                    break
                else:
                    return False
            except ValueError:
                return False
        while True:
            try:
                bookID = int(bookID)
                if not self.CheckId(Books.getAllAvailbleBooks(), bookID):
                    break
                else:
                    return False
            except ValueError:
                return False


        if dueTime < rentDay:
            return False
        Books.removeAvailbaleBook(bookID)
        Books.UpdateStatistics(bookID)
        self.__repo.add(rentID, clientID, bookID, rentDay, dueTime, returned)

        return True


    def ReturnBooks(self, Books, Clients, rentID):
        '''
        The return book function
        '''
        if len(self.__repo.getAll()) == 0:
            return False
        while True:
            try:
                rentID = int(rentID)
                if not self.__repo.CheckId(rentID):
                    break
                else:
                    return False
            except ValueError:
                return False
        notReturned = datetime.date(1, 1, 1)
        today = datetime.date.today()
        for i in self.__repo.getAll():
            if i.id == rentID and i.returnedDate != notReturned:
                return False
            elif i.id == rentID and i.returnedDate == notReturned:
                bookID = i.bookID
                i.returnedDate = today
                Clients.UpdateStatistics(i.getClientID(), (today - i.getRentedDate()).days)
                break
        Books.addNewAvailableBook(bookID)

        return True

    def PrintLateRentals(self):
        #if book is rented)->if dueDate<today&returnedDay=(1,1,1)->in lista
        newList = []
        today = datetime.date.today()
        for i in self.__repo.getAll():
            if i.returnedDate == datetime.date(1, 1, 1):
                if i.dueDate < today:
                    newList.append(i)
        newList.sort(key=lambda newList : newList.dueDate)
        return newList
        # for i in newList:
        #     print(str(i) + " Days of delay : " + str((today - i.dueDate).days))

    @staticmethod
    def CheckId(list, id):  # for both client list and book list
        '''checks if there is a given id into the list'''
        for i in list:
            if id == i.id:
                return False
        return True

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__repo

    def setRepo(self, newRepo):
        self.__repo.ItemsInRepo(newRepo)

    def getAllRentals(self):
        '''
        Return the items from the repository
        '''
        return self.__repo.getAll()

    def saveTEXT(self, fileName):
        '''
        Calls the function from the repository that saves the file
        '''
        return self.__repo.writeRentalsText(fileName)

    def saveDB(self, c, conn):
        return self.__repo.writeRentalsDatabase(c, conn)

    def savePICKLE(self, fileName):
        '''
        Calls the function from the repository that saves the file
        '''
        return self.__repo.writeRentalsPickle(fileName)

    def getLen(self):
        '''
        Returns the length of the list
        '''
        return len(self.__repo.getAll())

    def VerifyID(self, id):
        '''
        Verifies if there exists the given id into the list.
        '''
        return self.__repo.CheckId(id)