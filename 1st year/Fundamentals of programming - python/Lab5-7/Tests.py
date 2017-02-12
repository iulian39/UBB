import unittest
from BookClass import Book
from BookRepo import BookRepository
from ClientClass import Client
from ClientRepo import ClientRepository
from RentalRepo import RentalRepository
from RentalClass import Rental
import datetime
import random

class AllTests(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)



    @staticmethod
    def AddBooksInRepository(BookRepo):
        BookRepo.add(1, "Faust", "", "Ghoethe")
        BookRepo.add(2, "Agonie si extaz", "", "Irving Stone")
        BookRepo.add(3, "Romanul adolescentului miop", "", "Mircea Eliade")
        BookRepo.add(4, "Invitație la vals", "", "Mihail Drumeș")
        BookRepo.add(5, "Exerciții de echilibru", "", "Tudor Chirilă")
        BookRepo.add(6, "Maitreyi", "", "Mircea Eliade")
        BookRepo.add(7, "Cismigiu et comp", "", "Grigore Băjenaru")
        BookRepo.add(8, "Jurnal 2003 – 2009", "", "Oana Pellea")
        BookRepo.add(9, "Pânza de păianjen", "", "Cella Serghi")
        BookRepo.add(10, "Toate sfârșiturile sunt la fel", "", "Andrei Cioată")

    @staticmethod
    def AddClientsInRepository(ClientRepo):
        ClientRepo.add(1, "George")
        ClientRepo.add(2, "Vasile")
        ClientRepo.add(3, "Grigore")
        ClientRepo.add(4, "Ionel")
        ClientRepo.add(5, "Costel")
        ClientRepo.add(6, "Ana")
        ClientRepo.add(7, "Adina")
        ClientRepo.add(8, "Gabriela")
        ClientRepo.add(9, "Georgeta")
        ClientRepo.add(10, "Delia")

    @staticmethod
    def AddRentalsIsRepository(RentalRepo, Books, Clients):
        date = datetime.date(2016, 11, 15)
        notReturned = datetime.date(1, 1, 1)
        d = datetime.timedelta(days=7)
        RentalRepo.add(1, 1, 1, date - d, date, date)
        RentalRepo.add(2, 2, 2, date, date + d, date)
        RentalRepo.add(3, 3, 3, date - 2 * d, date + d, date + d)
        RentalRepo.add(4, 4, 4, date - 2 * d, date - d, notReturned)
        RentalRepo.add(5, 5, 5, date - 3 * d, date - 2 * d, notReturned)
        RentalRepo.add(6, 6, 6, date - 2 * d, date, notReturned)
        Books.UpdateStatistics(1)
        Books.UpdateStatistics(2)
        Books.UpdateStatistics(3)
        Books.UpdateStatistics(4)
        Books.UpdateStatistics(5)
        Books.UpdateStatistics(6)
        Clients.UpdateStatistics(1, 7)
        Clients.UpdateStatistics(2, 0)
        Clients.UpdateStatistics(3, 21)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAddRemoveBook(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)
        titles = ["Amintiri din copilarie", "Morometii", "Aybf", "Fafgaas"]
        Authors = ["George", "Vasile", "Grigore", "Georrgel", "Cristi"]
        for i in range(1, 9):
            Title = random.choice(titles)
            Author = random.choice(Authors)
            assert TheBookList.AddNewBooks(i, Title, "", Author) == False

        for i in range(11, 15):
            Title = random.choice(titles)
            Author = random.choice(Authors)
            assert TheBookList.AddNewBooks(i, Title, "", Author) == True

        Title = random.choice(titles)
        Author = random.choice(Authors)

        assert TheBookList.AddNewBooks("a", Title, "", Author) == False
        assert TheBookList.AddNewBooks(80, "", "", Author) == False
        assert TheBookList.AddNewBooks(80, Title, "", "") == False

        for i in range(1, 9):
            assert TheBookList.RemoveBooks(i) == True
        for i in range(40, 50):
            assert TheBookList.RemoveBooks(i) == False
        assert TheBookList.RemoveBooks(5) == False
        assert TheBookList.RemoveBooks("a") == False

    def testModifyBooks(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)

        assert TheBookList.ModifyTitle(4, "Marcel") == True
        assert TheBookList.ModifyTitle(4, "") == False
        assert TheBookList.ModifyTitle(400, "Marcel") == False
        assert TheBookList.ModifyTitle("4a", "Marcel") == False
        assert TheBookList.ModifyDescription(4, "") == True
        assert TheBookList.ModifyDescription("4a", "") == False
        assert TheBookList.ModifyDescription(400, "") == False
        assert TheBookList.ModifyAuthor(400, "Dada") == False
        assert TheBookList.ModifyAuthor(4, "Dada") == True
        assert TheBookList.ModifyAuthor(4, "") == False
        assert TheBookList.ModifyID(4, "a") == False
        assert TheBookList.ModifyID(4, 3) == False
        assert TheBookList.ModifyID(4, 500) == True
        assert TheBookList.ModifyID("4a", 8) == False

    def testSearchBooks(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)

        assert TheBookList.SearchBooks("a") != True
        assert TheBookList.SearchBooks("") == False
        assert TheBookList.SearchBooks("aaaaaaaaaaaaa") == False


    def testBookIsRemovalble(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)
        for i in range(20, 100):
            try:
                assert TheBookList.removeAvailbaleBook(i) == False
            except ValueError:
                pass

        for i in range(1, 9):
            try:
                assert TheBookList.removeAvailbaleBook(i) == True
            except ValueError:
                pass

    def testBookIsAddable(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)
        for i in range(1, 9):
            try:
                assert TheBookList.addNewAvailableBook(i) == True
            except ValueError:
                pass

        for i in range(20, 100):
            try:
                assert TheBookList.addNewAvailableBook(i) == False
            except ValueError:
                pass

    def testBookIsUpdatable(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)
        for i in range(1, 9):
            try:
                assert TheBookList.UpdateStatistics(i) == True
            except ValueError:
                pass

        for i in range(20, 100):
            try:
                assert TheBookList.UpdateStatistics(i) == False
            except ValueError:
                pass

    def testAddRemoveClient(self):
        ClientRepo = ClientRepository()
        self.AddClientsInRepository(ClientRepo)
        TheClientList = Client(ClientRepo)

        Names = ["George", "Vasile", "Grigore", "Georrgel", "Cristi"]
        for i in range(1, 9):
            Name = random.choice(Names)
            assert TheClientList.AddNewClients(i, Name) == False

        for i in range(11, 15):
            Name = random.choice(Names)
            assert TheClientList.AddNewClients(i, Name) == True

        assert TheClientList.AddNewClients("a", "george") == False
        assert TheClientList.AddNewClients(80, "") == False

        for i in range(1, 9):
            assert TheClientList.RemoveClients(i) == True
        for i in range(40, 50):
            assert TheClientList.RemoveClients(i) == False
        assert TheClientList.RemoveClients(5) == False
        assert TheClientList.RemoveClients("a") == False

    def testModifyClients(self):
        ClientRepo = ClientRepository()
        self.AddClientsInRepository(ClientRepo)
        TheClientList = Client(ClientRepo)

        assert TheClientList.ModifyID(4, 3) == False
        assert TheClientList.ModifyID(4, 100) == True
        assert TheClientList.ModifyID(4, "3a") == False
        assert TheClientList.ModifyID("4a", 3) == False
        assert TheClientList.ModifyID(400, 3) == False
        assert TheClientList.ModifyName(5, "") == False
        assert TheClientList.ModifyName(500, "dad") == False
        assert TheClientList.ModifyName(5, "George") == True

    def testSearchClients(self):
        ClientRepo = ClientRepository()
        self.AddClientsInRepository(ClientRepo)
        TheClientList = Client(ClientRepo)

        assert TheClientList.SearchClients("a") != False
        assert TheClientList.SearchClients("") == False
        assert TheClientList.SearchClients("aaaaaaaaaaaaa") == False

    def testClientIsUpdatable(self):
        ClientRepo = ClientRepository()
        self.AddClientsInRepository(ClientRepo)
        TheClientList = Client(ClientRepo)
        for i in range(1, 9):
            try:
                assert  TheClientList.UpdateStatistics(i, 2) == True
            except ValueError:
                pass

        for i in range(20, 100):
            try:
                assert TheClientList.UpdateStatistics(i, 2) == False
            except ValueError:
                pass

    def testRentBooks(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)
        ClientRepo = ClientRepository()
        self.AddClientsInRepository(ClientRepo)
        TheClientList = Client(ClientRepo)
        RentalRepo = RentalRepository()
        self.AddRentalsIsRepository(RentalRepo, TheBookList, TheClientList)
        TheRentalList = Rental(RentalRepo)

        years = [2016, 2017]
        months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14 ,15 , 16, 17, 18, 19, 20, 21 , 22 ,23 ,24, 25, 26, 27, 28]

        for i in range(1, 5):
            YEAR = random.choice(years)
            MONTH = random.choice(months)
            DAY = random.choice(days)
            rentDay = datetime.date(YEAR, MONTH, DAY)
            YEAR = random.choice(years)
            MONTH = random.choice(months)
            DAY = random.choice(days)
            dueTime = datetime.date(YEAR, MONTH, DAY)
            returned = datetime.date(1, 1, 1)
            assert TheRentalList.RentBooks(TheBookList, TheClientList, i, i, i, rentDay, dueTime, returned) == False

        for i in range(10, 15):
            YEAR = random.choice(years)
            MONTH = random.choice(months)
            DAY = random.choice(days)
            rentDay = datetime.date(YEAR, MONTH, DAY)
            YEAR = random.choice(years)
            MONTH = random.choice(months)
            DAY = random.choice(days)
            dueTime = datetime.date(YEAR, MONTH, DAY)
            returned = datetime.date(1, 1, 1)
            if dueTime < rentDay:
                assert TheRentalList.RentBooks(TheBookList, TheClientList, i, 5, 5, rentDay, dueTime, returned) == False
            else:
                assert TheRentalList.RentBooks(TheBookList, TheClientList, i, 5, 5, rentDay, dueTime, returned) == True

        rentDay = datetime.date(2016, 12, 12)
        dueTime = datetime.date(2016, 12, 20)
        returned = datetime.date(1, 1, 1)
        assert TheRentalList.RentBooks(TheBookList, TheClientList, "a", 5, 5, rentDay, dueTime, returned) == False
        assert TheRentalList.RentBooks(TheBookList, TheClientList, 75, 50, 5, rentDay, dueTime, returned) == False
        assert TheRentalList.RentBooks(TheBookList, TheClientList, 76, 5, 50, rentDay, dueTime, returned) == False
        assert TheRentalList.RentBooks(TheBookList, TheClientList, 75, "5a", 5, rentDay, dueTime, returned) == False
        assert TheRentalList.RentBooks(TheBookList, TheClientList, 75, 5, "5a", rentDay, dueTime, returned) == False

    def testReturnBooks(self):
        BookRepo = BookRepository()
        self.AddBooksInRepository(BookRepo)
        TheBookList = Book(BookRepo)
        ClientRepo = ClientRepository()
        self.AddClientsInRepository(ClientRepo)
        TheClientList = Client(ClientRepo)
        RentalRepo = RentalRepository()
        self.AddRentalsIsRepository(RentalRepo, TheBookList, TheClientList)
        TheRentalList = Rental(RentalRepo)

        assert TheRentalList.ReturnBooks(TheBookList, TheClientList, 4) == True
        assert TheRentalList.ReturnBooks(TheBookList, TheClientList, "4a") == False
        assert TheRentalList.ReturnBooks(TheBookList, TheClientList, 400) == False

        for i in range(5, 6):
            assert TheRentalList.ReturnBooks(TheBookList, TheClientList, i) == True

        for i in range(5, 6):
            assert TheRentalList.ReturnBooks(TheBookList, TheClientList, i) == False




if __name__ == '__main__':
    unittest.main()