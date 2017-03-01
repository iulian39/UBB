import datetime
import tkinter
import tkinter.messagebox
import copy
import sqlite3

class MainClass:
    def __init__(self, master, Books, Clients, Rentals, UndoList, RedoList, Settings):
        self.master = master
        # self.Books = Books
        # self.Clients = Clients
        # self.Rentals = Rentals
        # self.UndoList = UndoList
        # self.RedoList = RedoList
        self.frame = tkinter.Frame(self.master)
        self.ManageClients = tkinter.Button(self.frame, text='Manage Clients',  width = 15, command =lambda: self.ClientsMenu(Books, Clients, Rentals, UndoList))
        self.ManageBooks = tkinter.Button(self.frame, text='Manage Books', width = 15, command = lambda: self.BooksMenu(Books, Clients, Rentals, UndoList))
        self.Rental = tkinter.Button(self.frame, text='Rentals',  width = 15, command = lambda: self.RentalsMenu(Books, Clients, Rentals, UndoList))
        self.ShowStatistic = tkinter.Button(self.frame, text='Show Statistics', width=15, command=lambda: self.StatisticMenu(Books, Clients, Rentals))
        self.UndoButton = tkinter.Button(self.frame, text = 'Undo', width = 15, command = lambda: self.Undo(Books, Clients, Rentals, UndoList, RedoList))
        self.RedoButton = tkinter.Button(self.frame, text='Redo', width=15, command=lambda: self.Redo(Books, Clients, Rentals, UndoList, RedoList))
        self.SaveButton = tkinter.Button(self.frame, text='Save', width=15, command=lambda: self.Save(Books, Clients, Rentals, Settings))
        self.CloseButton = tkinter.Button(self.frame, text='Quit', width=15, command=lambda: self.close_windows(Books, Clients, Rentals, Settings))
        self.ManageClients.pack(pady=10)
        self.ManageBooks.pack(pady=10)
        self.Rental.pack(pady=10)
        self.ShowStatistic.pack(pady=10)
        self.UndoButton.pack(pady=10)
        self.RedoButton.pack(pady=10)
        self.SaveButton.pack(pady=10)
        self.CloseButton.pack(pady=10)
        self.frame.pack()

    @staticmethod
    def Save(Books, Clients, RentedBooks ,settings):
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
            tkinter.messagebox.showwarning("Error", "Cant save, sorry !")
            return
        tkinter.messagebox.showwarning("Succes !", "Saved !")
    @staticmethod
    def Redo(Books, Clients, Rentals, UndoList, RedoList):
        if len(RedoList) == 0:
            tkinter.messagebox.showwarning("Error", "There is nothing to redo !")
            return
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Clients.setRepo(RedoList[len(RedoList) - 1][0])
        Books.setRepo(RedoList[len(RedoList) - 1][1])
        Rentals.setRepo(RedoList[len(RedoList) - 1][2])
        RedoList.pop()
    @staticmethod
    def Undo(Books, Clients, Rentals, UndoList, RedoList):
        if len(UndoList) == 0:
            tkinter.messagebox.showwarning("Error", "There is nothing to undo !")
            return
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        RedoList.append([a, s, d])
        Clients.setRepo(UndoList[len(UndoList) - 1][0])
        Books.setRepo(UndoList[len(UndoList) - 1][1])
        Rentals.setRepo(UndoList[len(UndoList) - 1][2])
        UndoList.pop()

    def StatisticMenu(self,Books, Clients, Rentals):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = StatisticForm(self.newWindow, Books, Clients, Rentals)
    def ClientsMenu(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = ClientsForm(self.newWindow, Books, Clients, Rentals, UndoList)
    def BooksMenu(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = BookForm(self.newWindow, Books, Clients, Rentals, UndoList)
    def RentalsMenu(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = RentalsForm(self.newWindow, Books, Clients, Rentals, UndoList)
    def close_windows(self, Books, Clients, Rentals, Settings):
        self.Save( Books, Clients, Rentals, Settings)
        self.master.destroy()

class StatisticForm:
    def __init__(self, master, Books, Clients, Rentals):
        self.master = master
        # self.Rentals = Rentals
        # self.Clients = Clients
        # self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.MrentedBooks = tkinter.Button(self.frame, text='Most Rented Books', width=15, command=lambda: self.MostRentedBooks(Books))
        self.MrentedAuthor = tkinter.Button(self.frame, text='Most Rented Author', width=15, command=lambda: self.MostRentedAuthor(Books))
        self.ActiveClients = tkinter.Button(self.frame, text='Most Active Clients', width=15, command=lambda: self.MostActiveClient(Clients))
        self.LateRentals = tkinter.Button(self.frame, text='Late Rentals', width=15, command=lambda: self.LateRental(Rentals))
        self.MrentedBooks.pack(pady=10)
        self.MrentedAuthor.pack(pady=10)
        self.ActiveClients.pack(pady=10)
        self.LateRentals.pack(pady=10)
        self.frame.pack()
    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)
    def MostRentedBooks(self, Books):
        txt = ""
        list = Books.PrintMostRentedBooks()
        for i in list:
            txt += str(i) + "    RENTED : " + str(i.getRentals()) + " TIME(S)" + '\n'
        self.text_window(txt)
    def MostRentedAuthor(self, Books):
        txt = ""
        list = Books.PrintMostRentedAuthor()
        for i in list:
            ok = False
            printed = False
            for j in Books.getAllBook():
                if i[0] == j.author:
                    if printed == False:
                        txt += "Author : " + str(j.author) + '\n'
                        printed = True
                    txt += str(j) + '\n'
                    ok = True
            if ok == True:
                txt += "Number of rentals : " + str(i[1]) + '\n'
        self.text_window(txt)
    def MostActiveClient(self, Clients):
        txt = ""
        list = Clients.PrintClients()
        for i in list:
            txt += str(i) + ", Active for : " + str(i.days) + '\n'
        self.text_window(txt)
    def LateRental(self, Rentals):
        txt = ""
        list = Rentals.PrintLateRentals()
        today = datetime.date.today()
        for i in list:
            txt += str(i) + " Days of delay : " + str((today - i.dueDate).days) + '\n'
        self.text_window(txt)


class RentalsForm:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Rentals = Rentals
        # self.Clients = Clients
        # self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.RentBook = tkinter.Button(self.frame, text='Rent a book', width=15, command=lambda: self.rentBook(Books, Clients, Rentals, UndoList))
        self.ReturnBook = tkinter.Button(self.frame, text='Return a book', width=15, command=lambda: self.returnBook(Books, Clients, Rentals, UndoList))
        self.RentBook.pack(pady=10)
        self.ReturnBook.pack(pady=10)
        self.frame.pack()
    def rentBook(self, Books, Clients, Rentals, UndoList):
        if len(Books.getAllAvailbleBooks()) == 0:
            tkinter.messagebox.showwarning("Error", "There are no available books at the moment")
            return

        self.newWindow = tkinter.Toplevel(self.master)
        self.app = RentBook(self.newWindow, Books, Clients, Rentals, UndoList)
    def returnBook(self, Books, Clients, Rentals, UndoList):
        if Rentals.getLen() == 0:
            tkinter.messagebox.showwarning("Error", "No rentals")
            return
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = ReturnBook(self.newWindow, Books, Clients, Rentals, UndoList)

class ReturnBook:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Rentals = Rentals
        # self.Clients = Clients
        # self.Books = Books
        self.frame = tkinter.Frame(self.master)

        self.rentalidLabel = tkinter.StringVar()
        self.rentalidLabel.set("Rent Id: ")
        self.rentalidDir = tkinter.Label(self.master, textvariable=self.rentalidLabel, height=4)
        self.rentalidDir.pack(side="left")

        self.directoryRentalID = tkinter.StringVar(None)
        self.dirRentalID = tkinter.Entry(self.master, textvariable=self.directoryRentalID, width=10)
        self.dirRentalID.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Delete', width=15, command=lambda: self.returnBook(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady=20, padx=15)
        self.frame.pack()

        txt = "The list of rented books :\n"
        for i in Rentals.getAllRentals():
            txt += str(i) + '\n'

        self.text_window(txt)

    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)
    def returnBook(self, Books, Clients, Rentals, UndoList):
            try:
                rentID = int(self.dirRentalID.get())
                if Rentals.VerifyID(rentID):
                    tkinter.messagebox.showwarning("Error", "The id does not exist !")
                    return
            except ValueError:
                tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
                return

            a = copy.deepcopy(Clients.getClients())
            s = copy.deepcopy(Books.getAllBook())
            d = copy.deepcopy(Rentals.getAllRentals())

            UndoList.append([a, s, d])
            if Rentals.ReturnBooks(Books, Clients, rentID) == False:
                UndoList.pop()


class RentBook:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Rentals = Rentals
        # self.Clients = Clients
        # self.Books = Books
        self.frame = tkinter.Frame(self.master)

        self.rentalidLabel = tkinter.StringVar()
        self.rentalidLabel.set("Rent Id: ")
        self.rentalidDir = tkinter.Label(self.master, textvariable=self.rentalidLabel, height=4)
        self.rentalidDir.pack(side="left")

        self.directoryRentalID = tkinter.StringVar(None)
        self.dirRentalID = tkinter.Entry(self.master, textvariable=self.directoryRentalID, width=10)
        self.dirRentalID.pack(side="left")

        self.clientidLabel = tkinter.StringVar()
        self.clientidLabel.set("Client Id : ")
        self.clientidDir = tkinter.Label(self.master, textvariable=self.clientidLabel, height=4)
        self.clientidDir.pack(side="left")

        self.directoryClientID = tkinter.StringVar(None)
        self.dirClientID = tkinter.Entry(self.master, textvariable=self.directoryClientID, width=10)
        self.dirClientID.pack(side="left")

        self.BookLabe = tkinter.StringVar()
        self.BookLabe.set("Book Id: ")
        self.BookDir = tkinter.Label(self.master, textvariable=self.BookLabe, height=4)
        self.BookDir.pack(side="left")

        self.directoryBook = tkinter.StringVar(None)
        self.dirBookID = tkinter.Entry(self.master, textvariable=self.directoryBook, width=15)
        self.dirBookID.pack(side="left")

        self.YearLabe = tkinter.StringVar()
        self.YearLabe.set("Year: ")
        self.YearDir = tkinter.Label(self.master, textvariable=self.YearLabe, height=4)
        self.YearDir.pack(side="left")

        self.directoryYear = tkinter.StringVar(None)
        self.dirYear = tkinter.Entry(self.master, textvariable=self.directoryYear, width=15)
        self.dirYear.pack(side="left")

        self.MonthLabe = tkinter.StringVar()
        self.MonthLabe.set("Month: ")
        self.MonthDir = tkinter.Label(self.master, textvariable=self.MonthLabe, height=4)
        self.MonthDir.pack(side="left")

        self.directoryMonth = tkinter.StringVar(None)
        self.dirMonth = tkinter.Entry(self.master, textvariable=self.directoryMonth, width=15)
        self.dirMonth.pack(side="left")

        self.DayLabe = tkinter.StringVar()
        self.DayLabe.set("Day: ")
        self.DayDir = tkinter.Label(self.master, textvariable=self.DayLabe, height=4)
        self.DayDir.pack(side="left")

        self.directoryDay = tkinter.StringVar(None)
        self.dirDay = tkinter.Entry(self.master, textvariable=self.directoryDay, width=15)
        self.dirDay.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Submit', width=15, command=lambda: self.newRental(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady=20, padx=15)

        self.frame.pack()
        txt = "The list of clients :\n"
        for i in Clients.getClients():
            txt += str(i) + '\n'
        txt += "The list of books :\n"
        for i in Books.getAllAvailbleBooks():
            txt += str(i) + '\n'

        if  Rentals.getLen() > 0:
            txt += "The list of rented books :\n"
            for i in Rentals.getAllRentals():
                txt += str(i) + '\n'
        #tkinter.messagebox.showinfo("Lists", txt)
        self.text_window(txt)

    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)
    def close_windows(self):
        self.master.destroy()
    def newRental(self, Books, Clients, Rentals, UndoList):
        try:
            rentID = int(self.dirRentalID.get())
            if not Rentals.VerifyID(rentID):
                tkinter.messagebox.showwarning("Error", "The id already exists !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        try:
            clientID = int(self.dirClientID.get())
            if Rentals.CheckId(Clients.getClients(), clientID):
                tkinter.messagebox.showwarning("Error", "The id does not exist !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        try:
            bookID = int(self.dirBookID.get())
            if Rentals.CheckId(Books.getAllAvailbleBooks(), bookID):
                tkinter.messagebox.showwarning("Error", "The id does not exist !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        today = datetime.date.today()

        try:
            dueYear = int(self.dirYear.get())
            if dueYear < 2016 or dueYear > 2017:
                tkinter.messagebox.showwarning("Error", "Please enter a valid year !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        try:
            dueMonth = int(self.dirMonth.get())
            if dueMonth < 1 or dueMonth > 12:
                tkinter.messagebox.showwarning("Error", "Please enter a valid month !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        try:
            dueDay = int(self.dirDay.get())
            if dueMonth < 1 or dueMonth > 31:
                tkinter.messagebox.showwarning("Error", "Please enter a valid day !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        dueTime = datetime.date(dueYear, dueMonth, dueDay)
        if dueTime < today:
            tkinter.messagebox.showwarning("Error", "Due date can't be before today's date !!!")
            return

        returned = datetime.date(1, 1, 1)
        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Rentals.RentBooks(Books, Clients, rentID, bookID, clientID, today, dueTime, returned)

class TextForm:
    def __init__(self, master ,txt):
        self.master = master
        self.frame = tkinter.Frame(self.master)
        self.T = tkinter.Text(self.master, height=20, width=150)
        self.T.insert(tkinter.END , txt)
        self.T.pack()
        self.frame.pack()

class ClientsForm:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Clients = Clients
        self.frame = tkinter.Frame(self.master)
        self.AddButton = tkinter.Button(self.frame, text='Add Clients', width = 15, command=lambda: self.addClients(Books, Clients, Rentals, UndoList))
        self.RemoveButton = tkinter.Button(self.frame, text='Remove Clients', width = 15, command=lambda: self.removeClients(Books, Clients, Rentals, UndoList))
        self.UpdateButton = tkinter.Button(self.frame, text='Update Clients', width = 15, command=lambda: self.updateClients(Books, Clients, Rentals, UndoList))
        self.ListButton = tkinter.Button(self.frame, text='List Clients', width=15, command=lambda: self.printClients(Clients))
        self.SearchButton = tkinter.Button(self.frame, text='Search Clients', width=15, command=lambda: self.searchClients(Clients))
        self.quitButton = tkinter.Button(self.frame, text = 'Quit', width = 15, command = self.close_windows)
        self.AddButton.pack(pady=10)
        self.RemoveButton.pack(pady=10)
        self.UpdateButton.pack(pady=10)
        self.ListButton.pack(pady=10)
        self.SearchButton.pack(pady=10)
        self.quitButton.pack(pady=10)
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    def addClients(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = AddClient(self.newWindow, Books, Clients, Rentals, UndoList)
    def removeClients(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = RemoveClient(self.newWindow, Books, Clients, Rentals, UndoList)
    def updateClients(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = UpdateClient(self.newWindow, Books, Clients, Rentals, UndoList)
    def printClients(self, Clients):
        txt = ""
        for i in Clients.getClients():
            txt += str(i) + '\n'
        self.text_window(txt)
    def searchClients(self, Clients):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = SearchClient(self.newWindow, Clients)
    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)

class AddClient:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Clients = Clients
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Id : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirnameID = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirnameID.pack(side="left")

        self.nameLabe = tkinter.StringVar()
        self.nameLabe.set("Name : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.nameLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryName = tkinter.StringVar(None)
        self.dirName = tkinter.Entry(self.master, textvariable=self.directoryName, width=15)
        self.dirName.pack(side="left")
        self.SubmitButton = tkinter.Button(self.frame, text='Submit', width=15, command=lambda: self.addClient(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady = 20, padx = 15)
        self.frame.pack()
    def addClient(self, Books, Clients, Rentals, UndoList):
        try:
            id = int(self.dirnameID.get())
            if not Clients.VerifyID(id):
                tkinter.messagebox.showwarning("Error", "The id already exists !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return

        if len(self.dirName.get()) == 0:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Clients.AddNewClients(id, self.dirName.get())

class RemoveClient:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Clients = Clients
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Id : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirnameID = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirnameID.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Delete', width=15, command=lambda: self.removeClient(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady = 20, padx = 15)
        self.frame.pack()
    def removeClient(self, Books, Clients, Rentals, UndoList):
        if Clients.getLen() == 0:
            tkinter.messagebox.showwarning("Error", "No clients in the list ! ")
            return
        try:
            id = int(self.dirnameID.get())
            if Clients.VerifyID(id):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Clients.RemoveClients(id, Rentals)

class SearchClient:
    def __init__(self, master, Clients):
        self.master = master
        #self.Clients = Clients
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Name : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirName = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirName.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Search', width=15, command=lambda: self.searchClient(Clients))
        self.SubmitButton.pack(side="left", pady = 20, padx = 15)
        self.frame.pack()
    def searchClient(self, Clients):
        if len(self.dirName.get()) == 0:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return
        list = Clients.SearchClients(self.dirName.get())
        txt = ""
        for i in list:
            txt += str(i) + '\n'
        self.text_window(txt)
    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)

class UpdateClient:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        # self.Clients = Clients
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Id : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirnameID = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirnameID.pack(side="left")

        self.nameLabe = tkinter.StringVar()
        self.nameLabe.set("New Id : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.nameLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryName = tkinter.StringVar(None)
        self.dirNewID = tkinter.Entry(self.master, textvariable=self.directoryName, width=15)
        self.dirNewID.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Submit new ID', width=15, command=lambda: self.newID(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady = 20, padx = 15)
        self.nameLabe = tkinter.StringVar()

        self.nameLabe.set("New Name : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.nameLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryName = tkinter.StringVar(None)
        self.dirName = tkinter.Entry(self.master, textvariable=self.directoryName, width=15)
        self.dirName.pack(side="left")
        self.SubmitButton1 = tkinter.Button(self.frame, text='Submit new name', width=15, command=lambda: self.newName(Books, Clients, Rentals, UndoList))
        self.SubmitButton1.pack(side="left", pady = 20, padx = 15)
        self.frame.pack()
    def newID(self, Books, Clients, Rentals, UndoList):
        try:
            ID = int(self.dirnameID.get())
            if Clients.VerifyID(ID):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return


        try:
            newId = int(self.dirNewID.get())
            if Clients.VerifyID(newId):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return

        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Clients.ModifyID(ID, newId)

    def newName(self, Books, Clients, Rentals, UndoList):

        try:
            ID = int(self.dirnameID.get())
            if not Clients.VerifyID(ID):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        if len(self.dirName.get()) == 0:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Clients.ModifyName(ID, self.dirName.get())

class BookForm:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        #self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.AddButton = tkinter.Button(self.frame, text='Add Books', width = 15, command=lambda: self.addBooks(Books, Clients, Rentals, UndoList))
        self.RemoveButton = tkinter.Button(self.frame, text='Remove Books', width = 15, command=lambda: self.removeBooks(Books, Clients, Rentals, UndoList))
        self.UpdateButton = tkinter.Button(self.frame, text='Update Books', width = 15, command=lambda: self.updateBooks(Books, Clients, Rentals, UndoList))
        self.ListButton = tkinter.Button(self.frame, text='List Books', width=15, command=lambda: self.printBooks(Books))
        self.SearchButton = tkinter.Button(self.frame, text='Search Books', width=15, command=lambda: self.searchBook(Books))
        self.quitButton = tkinter.Button(self.frame, text = 'Quit', width = 15, command = self.close_windows)
        self.AddButton.pack(pady=10)
        self.RemoveButton.pack(pady=10)
        self.UpdateButton.pack(pady=10)
        self.ListButton.pack(pady=10)
        self.SearchButton.pack(pady=10)
        self.quitButton.pack(pady=10)
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    def addBooks(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = AddBook(self.newWindow, Books, Clients, Rentals, UndoList)
    def removeBooks(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = RemoveBook(self.newWindow, Books, Clients, Rentals, UndoList)
    def updateBooks(self, Books, Clients, Rentals, UndoList):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = UpdateBook(self.newWindow, Books, Clients, Rentals, UndoList)
    def printBooks(self, Books):
        txt = ""
        for i in Books.getAllBook():
            txt += str(i) + '\n'
        self.text_window(txt)
    def searchBook(self, Books):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = SearchBook(self.newWindow, Books)
    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)

class AddBook:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        #self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Id : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirID = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirID.pack(side="left")

        self.titleLabe = tkinter.StringVar()
        self.titleLabe.set("Title : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.titleLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryTitle = tkinter.StringVar(None)
        self.dirTitle = tkinter.Entry(self.master, textvariable=self.directoryTitle, width=15)
        self.dirTitle.pack(side="left")

        self.descriptLabe = tkinter.StringVar()
        self.descriptLabe.set("Description : ")
        self.descriptLabel = tkinter.Label(self.master, textvariable=self.descriptLabe, height=4)
        self.descriptLabel.pack(side="left")

        self.directoryDescript = tkinter.StringVar(None)
        self.dirDescript = tkinter.Entry(self.master, textvariable=self.directoryDescript, width=15)
        self.dirDescript.pack(side="left")

        self.authLabe = tkinter.StringVar()
        self.authLabe.set("Author : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.authLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryAuth = tkinter.StringVar(None)
        self.dirAuthor = tkinter.Entry(self.master, textvariable=self.directoryAuth, width=15)
        self.dirAuthor.pack(side="left")
        self.SubmitButton = tkinter.Button(self.frame, text='Submit', width=15, command=lambda: self.addBook(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady=20, padx=15)
        self.frame.pack()

    def addBook(self, Books, Clients, Rentals, UndoList):
        try:
            id = int(self.dirID.get())
            if not Books.VerifyID(id):
                tkinter.messagebox.showwarning("Error", "The id already exists !")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return


        title = self.dirTitle.get()
        if len(title) == 0:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return
        description = self.dirDescript.get()

        author = self.dirAuthor.get()
        if len(author) == 0:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Books.AddNewBooks(id, title, description, author)

class RemoveBook:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        #self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Id : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirnameID = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirnameID.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Delete', width=15, command=lambda: self.removeBook(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady=20, padx=15)
        self.frame.pack()

    def removeBook(self, Books, Clients, Rentals, UndoList):
        if Books.getLen() == 0:
            tkinter.messagebox.showwarning("Error", "No books in the list ! ")
            return
        try:
            id = int(self.dirnameID.get())
            if Books.VerifyID(id):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Books.RemoveBooks(id, Rentals)

class SearchBook:
    def __init__(self, master, Books):
        self.master = master
        #self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Title : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirTitle = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirTitle.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Search', width=15, command=lambda: self.searchBook(Books))
        self.SubmitButton.pack(side="left", pady=20, padx=15)
        self.frame.pack()

    def searchBook(self, Books):
        if len(self.dirTitle.get()) == 0:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return
        list = Books.SearchBooks(self.dirTitle.get())
        txt = ""
        for i in list:
            txt += str(i) + '\n'
        self.text_window(txt)
    def text_window(self, txt):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = TextForm(self.newWindow, txt)

class UpdateBook:
    def __init__(self, master, Books, Clients, Rentals, UndoList):
        self.master = master
        #self.Books = Books
        self.frame = tkinter.Frame(self.master)
        self.idLabel = tkinter.StringVar()
        self.idLabel.set("Id : ")
        self.idDir = tkinter.Label(self.master, textvariable=self.idLabel, height=4)
        self.idDir.pack(side="left")

        self.directoryID = tkinter.StringVar(None)
        self.dirnameID = tkinter.Entry(self.master, textvariable=self.directoryID, width=10)
        self.dirnameID.pack(side="left")

        self.nameLabe = tkinter.StringVar()
        self.nameLabe.set("New Id : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.nameLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryName = tkinter.StringVar(None)
        self.dirNewID = tkinter.Entry(self.master, textvariable=self.directoryName, width=15)
        self.dirNewID.pack(side="left")

        self.TitleLabe = tkinter.StringVar()
        self.TitleLabe.set("New Title : ")
        self.labelDir = tkinter.Label(self.master, textvariable=self.TitleLabe, height=4)
        self.labelDir.pack(side="left")

        self.directoryName = tkinter.StringVar(None)
        self.dirName = tkinter.Entry(self.master, textvariable=self.directoryName, width=15)
        self.dirName.pack(side="left")

        self.DescLabe = tkinter.StringVar()
        self.DescLabe.set("New Descriptin : ")
        self.labelDesc = tkinter.Label(self.master, textvariable=self.DescLabe, height=4)
        self.labelDesc.pack(side="left")

        self.directoryDesc = tkinter.StringVar(None)
        self.dirDesc = tkinter.Entry(self.master, textvariable=self.directoryDesc, width=50)
        self.dirDesc.pack(side="left")

        self.AuthLabe = tkinter.StringVar()
        self.AuthLabe.set("New Author : ")
        self.labelAuth = tkinter.Label(self.master, textvariable=self.AuthLabe, height=4)
        self.labelAuth.pack(side="left")

        self.directoryAuth = tkinter.StringVar(None)
        self.dirAuth = tkinter.Entry(self.master, textvariable=self.directoryAuth, width=15)
        self.dirAuth.pack(side="left")

        self.SubmitButton = tkinter.Button(self.frame, text='Submit ID', width=15, command=lambda:self.newID(Books, Clients, Rentals, UndoList))
        self.SubmitButton.pack(side="left", pady=20, padx=5)

        self.SubmitButton1 = tkinter.Button(self.frame, text='Submit title', width=15, command=lambda: self.newTitle(Books, Clients, Rentals, UndoList))
        self.SubmitButton1.pack(side="left", pady=20, padx=5)

        self.SubmitButton1 = tkinter.Button(self.frame, text='Submit description', width=15, command=lambda: self.newDesc(Books, Clients, Rentals, UndoList))
        self.SubmitButton1.pack(side="left", pady=20, padx=5)

        self.SubmitButton1 = tkinter.Button(self.frame, text='Submit author', width=15, command=lambda: self.newAuth(Books, Clients, Rentals, UndoList))
        self.SubmitButton1.pack(side="left", pady=20, padx=5)
        self.frame.pack()

    def newID(self, Books, Clients, Rentals, UndoList):
        try:
            ID = int(self.dirnameID.get())
            if Books.VerifyID(ID):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        try:
            newId = int(self.dirName.get())
            if Books.VerifyID(newId):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return

        except ValueError:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyID(ID, newId)

    def newTitle(self, Books, Clients, Rentals, UndoList):
        try:
            ID = int(self.dirnameID.get())
            if Books.VerifyID(ID):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        if len(self.dirName.get()) == 0:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyTitle(ID, self.dirName.get())

    def newDesc(self, Books, Clients, Rentals, UndoList):
        try:
            ID = int(self.dirnameID.get())
            if Books.VerifyID(ID):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyDescription(ID, self.dirDesc.get())

    def newAuth(self, Books, Clients, Rentals, UndoList):
        try:
            ID = int(self.dirnameID.get())
            if Books.VerifyID(ID):
                tkinter.messagebox.showwarning("Error", "The id does not exist ! ")
                return
        except:
            tkinter.messagebox.showwarning("Error", "Error ! Please type correctly")
            return

        if len(self.dirAuth.get()) == 0:
            tkinter.messagebox.showwarning("Error", "Please type correctly ! ")
            return

        a = copy.deepcopy(Clients.getClients())
        s = copy.deepcopy(Books.getAllBook())
        d = copy.deepcopy(Rentals.getAllRentals())

        UndoList.append([a, s, d])
        Books.ModifyAuthor(ID, self.dirName.get())
