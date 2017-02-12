import pickle
from lab9 import Module

class BookRepository:
    __data = []
    bookID = 0
    title = ""
    description = ""
    author = ""
    rentals = 0


    def __init__(self):
        """
        Constructor for BookRepository class
        """
        self.__data = [] #Module()

    def __init__(self, bookID = 0, title = "", description = "", author = ""):
        self.bookID = bookID
        self.title = title
        self.description = description
        self.author = author
        self.rentals = 0

    def __str__(self):
        return "Book id : %s,title : %s,description : %s,author : %s" % (self.bookID, self.title, self.description, self.author)

    @property
    def id(self):
        return self.bookID

    @id.setter
    def id(self, arg):
        self.bookID = arg

    def AddBooksInRepositoryPickle(self, file):
        for p in self.readBinaryFile(file):
            try:
                self.add(int(p[0]), p[1], p[2], p[3])
            except:
                pass

    def AddBooksInRepositoryDatabase(self, c, conn):
        c.execute('SELECT * FROM Books')
        for row in c.fetchall():
            try:
                self.add(int(row[0]), row[1], row[2], row[3])
            except:
                pass
        conn.commit()

    def writeBooksDatabase(self, c, conn):
        try:
            c.execute('DROP TABLE Books')
        except:
            pass
        c.execute('CREATE TABLE Books(bookID INTEGER, title TEXT, description TEXT, author TEXT)')
        for i in self.__data:
            c.execute("INSERT INTO Books (bookID, title, description, author) VALUES  (?, ?, ? ,?)", (i.bookID, i.title, i.description, i.author))
        conn.commit()


    @staticmethod
    def readBinaryFile(fileName):
        '''Reading from a binary file'''
        result = []
        try:
            f = open(fileName, "rb")
            return pickle.load(f)
        except EOFError:
            """
                This is raised if input file is empty
            """
            return []
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers
            """
            print("An error occured - " + str(e))
            raise e

        return result

    def writeBooksPickle(self, fileName):
        '''
        fileName = the name of the file
        books = the list of items
        '''
        books = []
        for i in self.__data:
            books.append([i.bookID, i.title, i.description, i.author])
        f = open(fileName, "wb")
        pickle.dump(books, f)
        f.close()

    def AddBooksInRepositoryTXT(self, file):
        with open(file) as f:
            content = f.read().splitlines()
            for line in content:
                words = line.split(";")
                try:
                    self.add(int(words[0]), words[1], words[2], words[3])
                except:
                    pass

    def writeBooksText(self, fileName):
        f = open(fileName, "w")
        try:
            for p in self.__data:
                pString = str(p.bookID) + ";" + p.title + ";" + p.description + ";" + p.author +"\n"
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))

    def AddBooksInRepository(self):
        self.add(1, "Faust", "NAN", "Ghoethe")
        self.add(2, "Agonie si extaz", "NAN", "Irving Stone")
        self.add(3, "Romanul adolescentului miop", "NAN", "Mircea Eliade")
        self.add(4, "Invitație la vals", "NAN", "Mihail Drumeș")
        self.add(5, "Exerciții de echilibru", "NAN", "Tudor Chirilă")
        self.add(6, "Maitreyi", "NAN", "Mircea Eliade")
        self.add(7, "Cismigiu et comp", "NAN", "Grigore Băjenaru")
        self.add(8, "Jurnal 2003 – 2009", "NAN", "Oana Pellea")
        self.add(9, "Pânza de păianjen", "NAN", "Cella Serghi")
        self.add(10, "You are not so smart", "NAN", "David McRainey")
        self.add(11, "Gândire rapidă, gândire lentă", "NAN", "Daniel Kahneman")
        self.add(12, "A da și a lua", "NAN", "Adam Grant")
        self.add(13, "Adevărul cinstit despre necinste", "NAN", "Dan Ariely")
        self.add(14, "This will make you smarter", "NAN", "John Brockman")
        self.add(15, "The Power of habit", "NAN", "Charles Duhigg")
        self.add(16, "Musai List", "NAN", "Octavian Pantiș")
        self.add(17, "Startup de 100$", "NAN", "Chris Guillebea")
        self.add(18, "The Personal MBA", "NAN", "Josh Kaufman")
        self.add(19, "O singură școală pentru toată lumea", "NAN", "Salman Khan")
        self.add(20, "Toate sfârșiturile sunt la fel", "NAN", "Andrei Cioată")
        self.add(21, "Confesiunile unui vorbitor în public", "NAN", "Scott Berkun")
        self.add(22, "The Element", "NAN", "Sir Ken Robinson")
        self.add(23, "Memoria inteligentă", "NAN", "Joshua Foer")
        self.add(24, "The Paleo Solution", "NAN", "Robb Wolf")
        self.add(25, "Open", "NAN", "Tudor Chirilă")
        self.add(26, "Kitchen Confidential", "NAN", "Anthony Bourdain")
        self.add(27, "Quiet", "NAN", "Susan Cain")
        self.add(28, "Starea de flux", "NAN", "Oana Pellea")
        self.add(29, "The Inner Game of Tennis", "NAN", "Cella Serghi")
        self.add(30, "Toate sfârșiturile sunt la fel", "NAN", "Andrei Cioată")
        self.add(31, "Faust", "NAN", "Ghoethe")
        self.add(32, "Agonie si extaz", "NAN", "Irving Stone")
        self.add(33, "Romanul adolescentului miop", "NAN", "Mircea Eliade")
        self.add(34, "Invitație la vals", "NAN", "Mihail Drumeș")
        self.add(35, "Exerciții de echilibru", "NAN", "Tudor Chirilă")
        self.add(36, "Maitreyi", "NAN", "Mircea Eliade")
        self.add(37, "Cismigiu et comp", "NAN", "Grigore Băjenaru")
        self.add(38, "Jurnal 2003 – 2009", "NAN", "Oana Pellea")
        self.add(39, "Pânza de păianjen", "NAN", "Cella Serghi")
        self.add(40, "Mastery ", "NAN", "Andrei Cioată")
        self.add(41, "Codul talentului", "NAN", "Ghoethe")
        self.add(42, "Agonie si extaz", "NAN", "Irving Stone")
        self.add(43, "Romanul adolescentului miop", "NAN", "Mircea Eliade")
        self.add(44, "Invitație la vals", "NAN", "Mihail Drumeș")
        self.add(45, "Exerciții de echilibru", "NAN", "Tudor Chirilă")
        self.add(46, "Buzz Marketing", "NAN", "Mircea Eliade")
        self.add(47, "Cismigiu et comp", "NAN", "Grigore Băjenaru")
        self.add(48, "Jurnal 2003 – 2009", "NAN", "Oana Pellea")
        self.add(49, "Pânza de păianjen", "NAN", "Cella Serghi")
        self.add(50, "Toate sfârșiturile sunt la fel", "NAN", "Andrei Cioată")

    def add(self, bookID, title, description, author):
        """
        Add a book to the repository
        """
        # self.__data.extend(1)
        self.__data.append(BookRepository(bookID, title, description, author))

    def remove(self, id):
        '''
        Remove a book from the repository
        '''
        for i in range(len(self.__data) - 1, -1, -1):
            if self.__data[i].id == id:
                del self.__data[i]

    def updateID(self, oldID, newID):
        """
        Update the ID of a client
        """
        for i in self.__data:
            if i.id == oldID:
                i.id = newID

    def updateTitle(self, ID, newTitle):
        '''
        Update the name of a client
        '''
        for i in self.__data:
            if i.id == ID:
                i.title = newTitle

    def updateDescription(self, ID, newDescription):
        '''
        Update the name of a client
        '''
        for i in self.__data:
            if i.id == ID:
                i.description = newDescription

    def updateAuthor(self, ID, newAuthor):
        '''
        Update the name of a client
        '''
        for i in self.__data:
            if i.id == ID:
                i.author = newAuthor

    def ItemsInRepo(self, newRepo):
        self.__data = newRepo

    def CheckId(self, id):
        '''checks if there is a given id into the list'''
        for i in self.__data:
            if id == i.id:
                return False
        return True

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data

    def lastItem(self):
        '''
        Returns the last item from __data
        '''
        return self.__data[len(self.__data) - 1]

    def getID(self):
        '''
        Returns the id
        '''
        return self.bookID

    def IncrementRentals(self):
        '''
        Increments the number of rentals
        '''
        self.rentals += 1

    def StatisticUpdate(self, theID):
        ok = False
        for i in self.__data:
            if i.id == theID:
                i.IncrementRentals()
                ok = True
        if ok == True:
            return True
        else:
            return False

    def sortByRentals(self):
        '''
        Sorts the list by rentals
        '''
        self.__data.sort(key=lambda  __data : __data.rentals, reverse= True)
        return self.__data

    def sortByAuthors(self):
        '''
        Sorts the list by rentals
        '''
        self.__data.sort(key=lambda __data: __data.author, reversed=True)
        return self.__data


    def getRentals(self):
        '''
        Returns the number of rentals
        '''
        return self.rentals







