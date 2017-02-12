import configparser
import pickle
import datetime


# def writeBooksPickle(fileName, books):
#     '''
#     fileName = the name of the file
#     books = the list of items
#     '''
#     f = open(fileName, "wb")
#     pickle.dump(books, f)
#     f.close()

def AddBooksInRepositoryPickle(BookRepo, file):
    for p in readBinaryFile(file):
        try:
            BookRepo.add(int(p[0]), p[1], p[2], p[3])
        except:
            pass


def AddClientsInRepositoryPickle(ClientRepo, file):
    for p in readBinaryFile(file):
        try:
            ClientRepo.add(int(p[0]), p[1])
        except:
            pass


def AddBooksInRepositoryTXT(BookRepo, file):
    with open(file) as f:
        content = f.read().splitlines()
        for line in content:
            words = line.split(";")
            try:
                BookRepo.add(int(words[0]), words[1], words[2], words[3])
            except:
                pass



def AddClientsInRepositoryTXT(ClientRepo, file):
    with open(file) as f:
        content = f.read().splitlines()
        for line in content:
            words = line.split(";")
            try:
                ClientRepo.add(int(words[0]), words[1])
            except:
                pass



# with open("books.txt") as f:
#     '''
#     Creating the pickle file
#     '''
#     content = f.read().splitlines()
#     list = []
#     for line in content:
#         words = line.split(";")
#         x = [words[0], words[1], words[2], words[3]]
#         list.append(x)
#     writeBooksPickle("books.pickle", list)
#
# with open("clients.txt") as f:
#     '''
#     Creating the pickle file
#     '''
#     content = f.read().splitlines()
#     list = []
#     for line in content:
#         words = line.split(";")
#         x = [words[0], words[1]]
#         list.append(x)
#     writeBooksPickle("clients.pickle", list)

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

def AddBooksInRepository(BookRepo):
    BookRepo.add(1, "Faust", "NAN", "Ghoethe")
    BookRepo.add(2, "Agonie si extaz", "NAN", "Irving Stone")
    BookRepo.add(3, "Romanul adolescentului miop", "NAN", "Mircea Eliade")
    BookRepo.add(4, "Invitație la vals", "NAN", "Mihail Drumeș")
    BookRepo.add(5, "Exerciții de echilibru", "NAN", "Tudor Chirilă")
    BookRepo.add(6, "Maitreyi", "NAN", "Mircea Eliade")
    BookRepo.add(7, "Cismigiu et comp", "NAN", "Grigore Băjenaru")
    BookRepo.add(8, "Jurnal 2003 – 2009", "NAN", "Oana Pellea")
    BookRepo.add(9, "Pânza de păianjen", "NAN", "Cella Serghi")
    BookRepo.add(10, "You are not so smart", "NAN", "David McRainey")
    BookRepo.add(11, "Gândire rapidă, gândire lentă", "NAN", "Daniel Kahneman")
    BookRepo.add(12, "A da și a lua", "NAN", "Adam Grant")
    BookRepo.add(13, "Adevărul cinstit despre necinste", "NAN", "Dan Ariely")
    BookRepo.add(14, "This will make you smarter", "NAN", "John Brockman")
    BookRepo.add(15, "The Power of habit", "NAN", "Charles Duhigg")
    BookRepo.add(16, "Musai List", "NAN", "Octavian Pantiș")
    BookRepo.add(17, "Startup de 100$", "NAN", "Chris Guillebea")
    BookRepo.add(18, "The Personal MBA", "NAN", "Josh Kaufman")
    BookRepo.add(19, "O singură școală pentru toată lumea", "NAN", "Salman Khan")
    BookRepo.add(20, "Toate sfârșiturile sunt la fel", "NAN", "Andrei Cioată")
    BookRepo.add(21, "Confesiunile unui vorbitor în public", "NAN", "Scott Berkun")
    BookRepo.add(22, "The Element", "NAN", "Sir Ken Robinson")
    BookRepo.add(23, "Memoria inteligentă", "NAN", "Joshua Foer")
    BookRepo.add(24, "The Paleo Solution", "NAN", "Robb Wolf")
    BookRepo.add(25, "Open", "NAN", "Tudor Chirilă")
    BookRepo.add(26, "Kitchen Confidential", "NAN", "Anthony Bourdain")
    BookRepo.add(27, "Quiet", "NAN", "Susan Cain")
    BookRepo.add(28, "Starea de flux", "NAN", "Oana Pellea")
    BookRepo.add(29, "The Inner Game of Tennis", "NAN", "Cella Serghi")
    BookRepo.add(30, "Toate sfârșiturile sunt la fel", "NAN", "Andrei Cioată")
    BookRepo.add(31, "Faust", "NAN", "Ghoethe")
    BookRepo.add(32, "Agonie si extaz", "NAN", "Irving Stone")
    BookRepo.add(33, "Romanul adolescentului miop", "NAN", "Mircea Eliade")
    BookRepo.add(34, "Invitație la vals", "NAN", "Mihail Drumeș")
    BookRepo.add(35, "Exerciții de echilibru", "NAN", "Tudor Chirilă")
    BookRepo.add(36, "Maitreyi", "NAN", "Mircea Eliade")
    BookRepo.add(37, "Cismigiu et comp", "NAN", "Grigore Băjenaru")
    BookRepo.add(38, "Jurnal 2003 – 2009", "NAN", "Oana Pellea")
    BookRepo.add(39, "Pânza de păianjen", "NAN", "Cella Serghi")
    BookRepo.add(40, "Mastery ", "NAN", "Andrei Cioată")
    BookRepo.add(41, "Codul talentului", "NAN", "Ghoethe")
    BookRepo.add(42, "Agonie si extaz", "NAN", "Irving Stone")
    BookRepo.add(43, "Romanul adolescentului miop", "NAN", "Mircea Eliade")
    BookRepo.add(44, "Invitație la vals", "NAN", "Mihail Drumeș")
    BookRepo.add(45, "Exerciții de echilibru", "NAN", "Tudor Chirilă")
    BookRepo.add(46, "Buzz Marketing", "NAN", "Mircea Eliade")
    BookRepo.add(47, "Cismigiu et comp", "NAN", "Grigore Băjenaru")
    BookRepo.add(48, "Jurnal 2003 – 2009", "NAN", "Oana Pellea")
    BookRepo.add(49, "Pânza de păianjen", "NAN", "Cella Serghi")
    BookRepo.add(50, "Toate sfârșiturile sunt la fel", "NAN", "Andrei Cioată")


def AddClientsInRepository(ClientRepo):
    ClientRepo.add(1, "George")
    ClientRepo.add(2, "Vasile")
    ClientRepo.add(3, "Grigore")
    ClientRepo.add(4, "Ionel")
    ClientRepo.add(5, "Costel")
    ClientRepo.add(6, "Ana")
    ClientRepo.add(7, "Adina")
    ClientRepo.add(8, "Gabriela")
    ClientRepo.add(9, "Daniel")
    ClientRepo.add(10, "Delia")
    ClientRepo.add(11, "George")
    ClientRepo.add(12, "Vasile")
    ClientRepo.add(13, "Grigore")
    ClientRepo.add(14, "Daniel")
    ClientRepo.add(15, "Costel")
    ClientRepo.add(16, "Ana")
    ClientRepo.add(17, "Adina")
    ClientRepo.add(18, "Fergus")
    ClientRepo.add(19, "Georgeta")
    ClientRepo.add(20, "Delia")
    ClientRepo.add(21, "George")
    ClientRepo.add(22, "Vasile")
    ClientRepo.add(23, "Grigore")
    ClientRepo.add(24, "Ionel")
    ClientRepo.add(25, "Costel")
    ClientRepo.add(26, "Ana")
    ClientRepo.add(27, "Adina")
    ClientRepo.add(28, "Daniel")
    ClientRepo.add(29, "Fergus")
    ClientRepo.add(30, "Delia")
    ClientRepo.add(31, "George")
    ClientRepo.add(32, "Vasile")
    ClientRepo.add(33, "Grigore")
    ClientRepo.add(34, "Ionel")
    ClientRepo.add(35, "Costelus")
    ClientRepo.add(36, "Anton")
    ClientRepo.add(37, "Adin")
    ClientRepo.add(38, "Yuri")
    ClientRepo.add(39, "Norbert")
    ClientRepo.add(40, "Alice")
    ClientRepo.add(41, "Suciu")
    ClientRepo.add(42, "Vasilica")
    ClientRepo.add(43, "Daniel")
    ClientRepo.add(44, "Ion")
    ClientRepo.add(45, "Costica")
    ClientRepo.add(46, "Ananas")
    ClientRepo.add(47, "Adina D")
    ClientRepo.add(48, "Gabriela B")
    ClientRepo.add(49, "Georget")
    ClientRepo.add(50, "Fergus")

def AddRentalsIsRepository(RentalRepo, Books, Clients):
    date = datetime.date(2016, 11, 15)
    notReturned = datetime.date(1, 1, 1)
    d = datetime.timedelta(days=7)
    RentalRepo.add(1, 1, 1, date - d, date, date)
    RentalRepo.add(2, 2, 2, date, date + d, date)
    RentalRepo.add(3, 3, 3, date - 2 * d, date + d, date + d)
    RentalRepo.add(4, 4, 4, date- 2*d, date - d, notReturned)
    RentalRepo.add(5, 5, 5, date- 3*d, date - 2*d, notReturned)
    RentalRepo.add(6, 6, 6, date- 2*d, date, notReturned)
    Books.UpdateStatistics(1)
    Books.UpdateStatistics(2)
    Books.UpdateStatistics(3)
    Books.UpdateStatistics(4)
    Books.UpdateStatistics(5)
    Books.UpdateStatistics(6)
    Clients.UpdateStatistics(1, 7)
    Clients.UpdateStatistics(2, 0)
    Clients.UpdateStatistics(3, 21)
    #Clients.UpdateStatistics(4, 0)


# with open("rentals.txt") as f:
#     content = f.read().splitlines()
#     for line in content:
#         print(line)
#         words = line.split(";")
#         print(words)

# with open("rentals.txt") as f:
#     content = f.read().splitlines()
#     for line in content:
#         words = line.split(";")
#
#         date1 = words[3].split('-')
#         date2 = words[4].split('-')
#         date3 = words[5].split('-')
#         rentD = datetime.date(date1[0], date1[1], date1[2])
#         dueD = datetime.date(date2[0], date2[1], date2[2])
#         returnedD = datetime.date(date3[0], date3[1], date3[2])
#         print(words, rentD, dueD, returnedD)

# for p in readBinaryFile("rentals.pickle"):
#     try:
#         print(p)
#     except:
#         pass
#
# with open("rentals.txt") as f:
#     content = f.read().splitlines()
#     for line in content:
#         words = line.split(";")
#         try:
#             print(words)
#         except:
#             pass

# date = datetime.date(2016, 11, 15)
# notReturned = datetime.date(1, 1, 1)
# d = datetime.timedelta(days=7)
# print((date + 2 * d - date).days)



# import sqlite3
#
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
# # def create_table():
# #     c.execute('CREATE TABLE IF NOT EXISTS ads(unix INTEGER, datestamp TEXT, keyword TEXT, value INTEGER)')
# #
# # def data_entry():
# #     c.execute("INSERT INTO ads VALUES (1451656468, '2016-12-22', 'Python', 5)")
# #     conn.commit()
# #     #c.close()
# #     #conn.close()
# #
# # def daa():
# #     c.execute("INSERT INTO ads (unix, datestamp, keyword, value) VALUES  (?, ?, ? ,?)", (123, '2015-01-01', 'CACA', 798465))
# #     conn.commit()
# #
# # def read_from_db():
# #     c.execute('SELECT * FROM ads')
# #     for row in c.fetchall():
# #         print(row[0])
# #     #data = c.fetchall()
# #     #print(data)
# #
# # create_table()
# # data_entry()
# # daa()
# # read_from_db()
# # try:
# #     c.execute('DROP TABLE fas')
# # except:
# #     pass
# # create_table()
# # data_entry()
# # daa()
# # read_from_db()
# # c.execute('DROP TABLE ads')
