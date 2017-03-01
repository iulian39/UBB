import datetime
import copy
import sqlite3

class MenuUI:

    def __init__(self, Books, Clients, RentedBooks, UndoList, RedoList, settings):
        while True:
            self.MainMenuUI()
            command = input("Please type the command : ")
            if self.validInputCommand(command, "Principal Menu"):
                if command == "0":
                    self.SaveFiles(Books, Clients, RentedBooks,settings)
                    break
                elif command == "1":
                    self.ClientsList(Books, Clients, RentedBooks, UndoList)
                elif command == "2":
                    self.BooksList(Books, Clients, RentedBooks, UndoList)
                elif command == "3":
                    self.RentBooks(Books, Clients, RentedBooks, UndoList)
                elif command == "4":
                    self.ReturnBooks(Books, Clients, RentedBooks, UndoList)
                    # RentedBooks.ReturnBooks(Books, Clients)
                elif command == "5":
                    self.Statistics(Books, Clients, RentedBooks)
                elif command == "6":
                    self.Undo( Books, Clients, RentedBooks, UndoList, RedoList)
                elif command == "7":
                    self.Redo( Books, Clients, RentedBooks, RedoList, UndoList )
                elif command == "8":
                    self.SaveFiles(Books, Clients, RentedBooks,settings)

    @staticmethod
    def SaveFiles(Books, Clients, RentedBooks ,settings):
        if settings.GetTypeOfRepo() == 'TEXT':
            Books.saveTEXT(settings.GetBookFile())
            Clients.saveTEXT(settings.GetClientFile())
            RentedBooks.saveTEXT(settings.GetRentalFile())
        elif settings.GetTypeOfRepo() == 'PICKLE':
            Books.savePICKLE(settings.GetBookFile())
            Clients.savePICKLE(settings.GetClientFile())
            RentedBooks.savePICKLE(settings.GetRentalFile())
        elif settings.GetTypeOfRepo() == 'DATABASE':
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            Books.saveDB(c, conn)
            Clients.saveDB(c, conn)
            RentedBooks.saveDB(c, conn)
            c.close()
            conn.close()
        else:
            print("Cant save, sorry !")
            return
        print("Saved !")

    @staticmethod
    def Undo( Books, Clients, RentedBooks, UndoList, RedoList):
        if len(UndoList) == 0:
            print("There is nothing to undo !")
            return
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        RedoList.append([a, s, d])
        Clients.setRepo(UndoList[len(UndoList) - 1][0])
        Books.setRepo(UndoList[len(UndoList) - 1][1])
        RentedBooks.setRepo(UndoList[len(UndoList) - 1][2])
        UndoList.pop()


    @staticmethod
    def Redo( Books, Clients, RentedBooks, RedoList, UndoList ):
        if len(RedoList) == 0:
            print("There is nothing to redo !")
            return
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Clients.setRepo(RedoList[len(RedoList) - 1][0])
        Books.setRepo(RedoList[len(RedoList) - 1][1])
        RentedBooks.setRepo(RedoList[len(RedoList) - 1][2])
        RedoList.pop()

    @staticmethod
    def ReturnBooks(Books, Clients, RentedBooks, UndoList):
        if RentedBooks.getLen() == 0:
            print("No rentals !")
            return
        RentedBooks.List()
        while True:
            try:
                rentID = int(input("Please type the rental id : "))
                if not RentedBooks.VerifyID(rentID):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        if RentedBooks.ReturnBooks(Books, Clients, rentID) == False:
            UndoList.pop()


    def RentBooks(self,Books, Clients, RentedBooks, UndoList):
        if len(Books.getAllAvailbleBooks()) == 0:
            print("There are no available books at the moment")
            return
        print("The list of clients :")
        for i in Clients.getClients():
            print(i)
        print("The list of books :")
        for i in Books.getAllAvailbleBooks():
            print(i)
        if RentedBooks.getLen() > 0:
            print("The list of rented books :")
            RentedBooks.List()
        while True:
            try:
                rentID = int(input("Please type the rent id : "))
                if RentedBooks.VerifyID(rentID):
                    break
                else:
                    print("The id already exists !")
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            try:
                clientID = int(input("Please type the client id : "))
                if not RentedBooks.CheckId(Clients.getClients(), clientID):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            try:
                bookID = int(input("Please type the book id : "))
                if not RentedBooks.CheckId(Books.getAllAvailbleBooks(), bookID):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")
        today = datetime.date.today()
        while True:
            try:
                dueYear = int(input("Please type the year : "))
                if dueYear < 2016 or dueYear > 2017:
                    print("Please enter a valid year !")
                else:
                    break
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            try:
                dueMonth = int(input("Please type the month: "))
                if dueMonth < 1 or dueMonth > 12:
                    print("Please enter a valid month !")
                else:
                    break
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            try:
                dueDay = int(input("Please type the day: "))
                if dueMonth < 1 or dueMonth > 31:
                    print("Please enter a valid day !")
                else:
                    break
            except ValueError:
                print("Error ! Please type correctly")

        dueTime = datetime.date(dueYear, dueMonth, dueDay)
        if dueTime < today:
            print("Due date can't be before today's date !!!")
            self.RentBooks(RentedBooks, Clients, Books)
            return

        returned = datetime.date(1, 1, 1)
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        RentedBooks.RentBooks(Books, Clients, rentID, bookID, clientID, today, dueTime, returned)



    @staticmethod
    def ClientsMenu():
        str = "\nAvailable commands :\n"
        str += "\t1 - add new clients\n"
        str += "\t2 - to remove clients\n"
        str += "\t3 - to update the client list\n"
        str += "\t4 - to list the client list\n"
        str += "\t5 - to search clients by name\n"
        str += "\t0 - to exit"
        print(str)


    def ClientsList(self, Books, Clients, RentedBooks, UndoList):
        while True:
            self.ClientsMenu()
            command = input("Pleast type the command : ")
            if self.validInputCommand(command, "Command Menu"):
                if command == "0":
                    break
                elif command == "1":
                    self.AddNewClients(Books, Clients, RentedBooks, UndoList)
                elif command == "2":
                    self.RemoveClients(Books, Clients, RentedBooks, UndoList)
                elif command == "3":
                    self.UpdateClientList(Books, Clients, RentedBooks, UndoList)
                elif command == "4":
                    Clients.List()
                elif command == "5":
                    self.SearchClients(Clients)

    @staticmethod
    def SearchClients(Clients):
        while True:
            Name = input("Please type the name of a client : ")
            if len(Name) > 0:
                break
        list = Clients.SearchClients(Name)
        for i in list:
            print(i)

    @staticmethod
    def AddNewClients(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                id = int(input("Please type the id : "))
                if Clients.VerifyID(id):
                    break
                else:
                    print("The id already exists !")
            except ValueError:
                print("Error ! Please type correctly")

        while True:
            name = input("Please type the name : ")
            if len(name) > 0:
                break
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Clients.AddNewClients(id, name)

    @staticmethod
    def RemoveClients(Books, Clients, RentedBooks, UndoList):
        Clients.List()
        while True:
            if Clients.getLen() == 0:
                print("There are no clients in the list !")
                break
            try:
                id = int(input("Please type the id : "))
                if not Clients.VerifyID(id):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Clients.RemoveClients(id, RentedBooks)


    def BooksList(self, Books, Clients, RentedBooks, UndoList):
        while True:
            self.BooksMenu()
            command = input("Pleast type the command : ")
            if self.validInputCommand(command, "Command Menu"):
                if command == "0":
                    break
                elif command == "1":
                    self.AddNewBooks(Books, Clients, RentedBooks, UndoList)
                elif command == "2":
                    self.RemoveBooks(Books, Clients, RentedBooks, UndoList)
                elif command == "3":
                    self.UpdateBookList(Books, Clients, RentedBooks, UndoList)
                elif command == "4":
                    Books.List()
                elif command == "5":
                    self.SearchBooks(Books)

    @staticmethod
    def AddNewBooks(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                id = int(input("Please type the id : "))
                if Books.VerifyID(id):
                    break
                else:
                    print("The id already exists !")
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            title = input("Please type the title : ")
            if len(title) > 0:
                break
        description = input("Please type the description : ")
        while True:
            author = input("Please type the author : ")
            if len(author) > 0:
                break


        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Books.AddNewBooks(id, title, description, author)

    @staticmethod
    def RemoveBooks(Books, Clients, RentedBooks, UndoList):
        Books.List()
        while True:
            if Books.getLen() == 0:
                print("There are no books in the list !")
                break
            try:
                id = int(input("Please type the id : "))
                if not Books.VerifyID(id):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Books.RemoveBooks(id, RentedBooks)

    @staticmethod
    def SearchBooks(Books):
        while True:
            Title = input("Please type the title of a book : ")
            if len(Title) > 0:
                break
        list = Books.SearchBooks(Title)
        for i in list:
            print(i)




    def UpdateBookList(self, Books, Clients, RentedBooks, UndoList):
        Books.List()
        while True:
            if Books.getLen == 0:
                print("There are no books in the list !")
                break
            self.UpdateBookMenu()
            command = input("Pleast type the command : ")
            if self.validInputCommand(command, "Update Book Menu"):
                if command == "1":
                    self.ModifyID(Books, Clients, RentedBooks, UndoList)
                    break
                if command == "2":
                    self.ModifyTitle(Books, Clients, RentedBooks, UndoList)
                    break
                if command == "3":
                    self.ModifyDescription(Books, Clients, RentedBooks, UndoList)
                    break
                if command == "4":
                    self.ModifyAuthor(Books, Clients, RentedBooks, UndoList)
                    break

    @staticmethod
    def ModifyID(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                oldId = int(input("Please type the current id : "))
                if not Books.VerifyID(oldId):
                    break
                else:
                    print("The id does not exist !")
            except:
                print("Error ! Please type correctly")

        while True:
            try:
                newId = int(input("Please type the new id : "))
                if Books.VerifyID(newId):
                    break
                else:
                    print("The id already exists !")
            except ValueError:
                print("Error ! Please type correctly")

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyID(oldId, newId)

    @staticmethod
    def ModifyTitle(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                idOfBook = int(input("Please type the id : "))
                if not Books.VerifyID(idOfBook):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            newTitle = input("Please type the new title : ")
            if len(newTitle) > 0:
                break

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyTitle(idOfBook, newTitle)


    @staticmethod
    def ModifyDescription(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                idOfBook = int(input("Please type the id : "))
                if not Books.VerifyID(idOfBook):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")

        newDescription = input("Please type the new description : ")

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyDescription(idOfBook, newDescription)

    @staticmethod
    def ModifyAuthor(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                idOfBook = int(input("Please type the id : "))
                if not Books.VerifyID(idOfBook):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")

        while True:
            newAuthor = input("Please type the new author : ")
            if len(newAuthor) > 0:
                break

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyAuthor(idOfBook, newAuthor)

    @staticmethod
    def StatisticsMenu():
        str = "\nAvailable commands :\n"
        str += "\t1 - Most rented books\n"
        str += "\t2 - Most rented author\n"
        str += "\t3 - Most active clients\n"
        str += "\t4 - Late rentals\n"
        str += "\t0 - to exit"
        print(str)

    def Statistics(self, Books, Clients, RentedBooks):
        while True:
            self.StatisticsMenu()
            command = input("Please type the command : ")
            if self.validInputCommand(command, "Statistics Menu"):
                if command == "0":
                    break
                elif command == "1":
                    print("\nThe most rented books : \n")
                    list = Books.PrintMostRentedBooks()
                    for i in list:
                        print(str(i) + "    RENTED : " + str(i.getRentals()) + " TIME(S)")
                elif command == "2":
                    print("\nThe most rented author : \n")
                    list = Books.PrintMostRentedAuthor()
                    for i in list:
                        ok = False
                        printed = False
                        for j in Books.getAllBook():
                            if i[0] == j.author:
                                if printed == False:
                                    print("Author : " + j.author)
                                    printed = True
                                print(j)
                                ok = True
                        if ok == True:
                            print("Number of rentals : " + str(i[1]))
                elif command == "3":
                    print("\nThe most active clients : \n")
                    list = Clients.PrintClients()
                    for i in list:
                        print(str(i) + ", Active for : " + str(i.days))
                elif command == "4":
                    print("\nLate rentals : \n")
                    list = RentedBooks.PrintLateRentals()
                    today = datetime.date.today()
                    for i in list:
                        print(str(i) + " Days of delay : " + str((today - i.dueDate).days))

    def UpdateClientList(self, Books, Clients, RentedBooks, UndoList):
        Clients.List()
        while True:
            if Clients.getLen() == 0:
                print("There are no clients in the list !")
                break
            self.UpdateClientMenu()
            command = input("Pleast type the command : ")
            if self.validInputCommand(command, "Update Menu"):
                if command == "1":
                    self.ModifyIdClient(Clients, UndoList, Books, RentedBooks)
                    break
                if command == "2":
                    self.ModifyName(Clients, UndoList, Books, RentedBooks)
                    break

    @staticmethod
    def ModifyIdClient(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                ID = int(input("Please type the current id : "))
                if not Clients.VerifyID(ID):
                    break
                else:
                    print("The id does not exist !")
            except:
                print("Error ! Please type correctly")

        while True:
            try:
                newId = int(input("Please type the new id : "))
                if Clients.VerifyID(newId):
                    break
                else:
                    print("The id already exists !")

            except ValueError:
                print("Error ! Please type correctly")

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Clients.ModifyID(ID, newId)

    @staticmethod
    def ModifyName(Books, Clients, RentedBooks, UndoList):
        while True:
            try:
                ID = int(input("Please type the id : "))
                if not Clients.VerifyID(ID):
                    break
                else:
                    print("The id does not exist !")
            except ValueError:
                print("Error ! Please type correctly")
        while True:
            newName = input("Please type the new name : ")
            if len(newName) > 0:
                break
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(RentedBooks.getAllRentals())

        UndoList.append([a, s, d])
        Clients.ModifyName(ID, newName)

    @staticmethod
    def UpdateBookMenu():
        str = "\nAvailable commands\n"
        str += "\t1- to update the ID of a book\n"
        str += "\t2- to update the title of a book\n"
        str += "\t3- to update the description of a book\n"
        str += "\t4- to update the author of a book"
        print(str)

    @staticmethod
    def UpdateClientMenu():
        str = "\nAvailable commands\n"
        str += "\t1- to update the ID of a client\n"
        str += "\t2- to update the name of a client"
        print(str)

    @staticmethod
    def BooksMenu():
        str = "\nAvailable commands :\n"
        str += "\t1 - add new books\n"
        str += "\t2 - to remove books\n"
        str += "\t3 - to update the books list\n"
        str += "\t4 - to list the books list\n"
        str += "\t5 - to search books by title\n"
        str += "\t0 - to exit"
        print(str)

    @staticmethod
    def MainMenuUI():
        str = "\nAvailable commands :\n"
        str += "\t1 - Manage client list\n"
        str += "\t2 - Manage books list\n"
        str += "\t3 - Rent a book\n"
        str += "\t4 - Return a book\n"
        str += "\t5 - Show statistics\n"
        str += "\t6 - Undo the last change\n"
        str += "\t7 - Redo the last change\n"
        str += "\t8 - Save\n"
        str += "\t0 - Exit"
        print(str)

    @staticmethod
    def validInputCommand(command, typeOfMenu):
        '''
        Verify if the command is valid
        input: command
        output: true / false
        '''
        if typeOfMenu == "Principal Menu":
            availableCommands = ['1', '2', '3', '4', '5','6', '7', '8','0']
        if typeOfMenu == "Update Menu":
            availableCommands = ['1', '2']
        if typeOfMenu == "Command Menu":
            availableCommands = ['1', '2', '3', '4', '5', '0']
        if typeOfMenu == "Update Book Menu":
            availableCommands = ['1', '2', '3', '4']
        if typeOfMenu == "Statistics Menu":
            availableCommands = ['1', '2', '3', '4', '0']
        return (command in availableCommands)