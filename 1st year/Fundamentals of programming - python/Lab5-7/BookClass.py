import copy
class Book:
    def __init__(self, repo):
        self.__repo = []
        self.__availableBooks = []
        self.__repo = copy.deepcopy(repo)
        self.__availableBooks = copy.deepcopy(repo.getAll())



    def AddNewBooks(self, ID, title, description, author):
        '''
        Adds a new book to the list
        '''
        if len(title) == 0 or len(author) == 0:
            return False

        while True:
            try:
                ID = int(ID)
                if self.__repo.CheckId(ID):
                    break
                else:
                    return False
            except ValueError:
                return False


        self.__repo.add(ID, title, description, author)
        self.__availableBooks.append(self.__repo.lastItem())
        return True

    def VerifyID(self, id):
        '''
        Verifies if there exists the given id into the list.
        '''
        return self.__repo.CheckId(id)

    def List(self):
        '''
        Prints the list of books
        '''
        for i in self.__repo.getAll():
            print(i)

    def RemoveBooks(self, ID, Rentals):
        '''
        Removes a book from the list
        '''
        while True:
            if len(self.__repo.getAll()) == 0:
                return False
            try:
                ID = int(ID)
                if not self.__repo.CheckId(ID):
                    break
                else:
                    return False
            except ValueError:
                return False
        self.__repo.remove(ID)
        for i in Rentals.getAllRentals():
            if i.bookID == ID:
                i.removeBookId(ID)
                break


        self.removeAvailbaleBook(ID)
        return True


    def ModifyTitle(self, idOfBook, newTitle):
        '''
        Modifies the title of a book
        '''
        while True:
            try:
                idOfBook = int(idOfBook)
                if not self.__repo.CheckId(idOfBook):
                    break
                else:
                    return False
            except ValueError:
                return False
        if len(newTitle) > 0:
            self.__repo.updateTitle(idOfBook, newTitle)
            for i in self.__availableBooks:
                if i.id == idOfBook:
                    i.title = newTitle
            return True
        else:
            return False



    def ModifyDescription(self, idOfBook, newDescription):
        '''
        Modifies the description of a book
        '''
        while True:
            try:
                idOfBook = int(idOfBook)
                if not self.__repo.CheckId(idOfBook):
                    break
                else:
                    return False
            except ValueError:
                return False


        self.__repo.updateDescription(idOfBook, newDescription)
        for i in self.__availableBooks:
            if i.id == idOfBook:
                i.description = newDescription

        return True


    def ModifyAuthor(self, idOfBook, newAuthor):
        '''
        Modifies the author of a book
        '''
        while True:
            try:
                idOfBook = int(idOfBook)
                if not self.__repo.CheckId(idOfBook):
                    break
                else:
                    return False
            except ValueError:
                return False

        if len(newAuthor) == 0:
            return False

        self.__repo.updateAuthor(idOfBook, newAuthor)
        for i in self.__availableBooks:
            if i.id == idOfBook:
                i.author = newAuthor

        return True

    def ModifyID(self, oldID, newId):
        '''
        Modifies the id of a book
        '''
        while True:
            try:
                oldID = int(oldID)
                if not self.__repo.CheckId(oldID):
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
        self.__repo.updateID(oldID, newId)
        for i in self.__availableBooks:
            if i.id == oldID:
                i.id = newId
        return True

    def setRepo(self, newRepo):
        self.__repo.ItemsInRepo(newRepo)

    def getAllBooks(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__repo

    def getAllBook(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__repo.getAll()

    def getAllAvailbleBooks(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__availableBooks

    def removeAvailbaleBook(self, ID):
        '''
        Removes a book from the availableBooks list only, the book list is not affected
        '''
        for i in range(len(self.__availableBooks) - 1, -1, -1):
            if self.__availableBooks[i].id == ID:
                del self.__availableBooks[i]
                return True
        return False

    def addNewAvailableBook(self, bookID):
        '''
        Adds back a book from the list into the available books
        '''
        for i in self.__repo.getAll():
            if i.id == bookID:
                self.__availableBooks.append(i)
                return True
        return False

    def UpdateStatistics(self, bookID):
        '''
        Updates the statistics of a book
        '''
        ok = False
        for i in self.__repo.getAll():
            if i.id == bookID:
                i.IncrementRentals()
                ok = True
        if ok == True:
            return True
        else:
            return False

    def PrintMostRentedBooks(self):
        '''
        Prints the list descending by the most rented books
        '''
        # for i in self.__repo.sortByRentals():
        #     print(str(i) + "    RENTED : " + str(i.getRentals()) + " TIME(S)")
        return self.__repo.sortByRentals()

    def saveTEXT(self, fileName):
        '''
        Calls the function from the repository that saves the file
        '''
        return self.__repo.writeBooksText(fileName)

    def saveDB(self, c, conn):
        return self.__repo.writeBooksDatabase(c, conn)

    def savePICKLE(self, fileName):
        '''
        Calls the function from the repository that saves the file
        '''
        return self.__repo.writeBooksPickle(fileName)

    def PrintMostRentedAuthor(self):
        '''
        Prints the list descending by the most rented author
        '''
        newList = []
        for i in self.__repo.getAll():
            ok = False
            if i.getRentals() > 0:
                for j in newList:
                    if j[0] == i.author:
                        j[1] += i.rentals
                        ok = True
                if ok == False:
                    s = [i.author, i.rentals]
                    newList.append(s)
        if len(newList) == 0:
            return
        newList.sort(key=lambda newList: newList[0])
        newList.sort(key=lambda newList: newList[1], reverse=True)
        return newList
        # for i in newList:
        #     ok = False
        #     printed = False
        #     for j in self.__repo.getAll():
        #         if i[0] == j.author:
        #             if printed == False:
        #                 print("Author : " + j.author)
        #                 printed = True
        #             print(j)
        #             ok = True
        #     if ok == True:
        #         print("Number of rentals : " + str(i[1]))




    # @staticmethod
    # def printList(list):
    #     '''
    #     Prints the books having the same author
    #     '''
    #     sum = 0
    #     for i in sorted(list, key=lambda x: x.rentals, reverse=True):
    #         print(i)
    #         sum += i.getRentals()
    #     print("Total: ", sum)

    def SearchBooks(self, Title):
        '''
        Searches for books having a certain title/part of title
        '''
        list = []
        if len(Title) > 0:
            Title = Title.lower()
            ok = False
            for i in self.__repo.getAll():
                if i.title.lower().find(Title) != -1:
                    list.append(i)
                    ok = True
            if ok == True:
                return list
            else:
                return False
        else:
            return False

    def getLen(self):
        '''
        Returns the lenght of the book list
        '''
        return len(self.__repo.getAll())

