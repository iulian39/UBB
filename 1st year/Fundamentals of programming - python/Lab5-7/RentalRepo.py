import datetime
import pickle

class RentalRepository:
    __data = []
    rentalID = 0
    clientID = 0
    bookID = 0
    rentedDate = datetime.date(2016, 1, 1)
    dueDate = datetime.date(2016, 1,1)
    returnedDate = datetime.date(2016, 1, 1)
    def __init__(self):
        """
        Constructor for RentalRepository class
        """
        self.__data = []


    def __init__(self, rentalID = 0, clientID = 0, bookID = 0, rentedDate = datetime.date(2016,1,1), dueDate = datetime.date(2016,1,1), returnedDate = datetime.date(2016,1,1)):
        self.rentalID = rentalID
        self.clientID = clientID
        self.bookID = bookID
        self.rentedDate = rentedDate
        self.dueDate = dueDate
        self.returnedDate = returnedDate

    def __str__(self):
        return "Rental id : %s,client id : %s,book id : %s,rented date : %s,due date : %s,returned date : %s" % (self.rentalID, self.clientID, self.bookID, self.rentedDate, self.dueDate, self.returnedDate)


    @property
    def id(self):
        return self.rentalID

    def writeRentalsText(self, fileName):
        f = open(fileName, "w")
        try:
            for p in self.__data:
                pString = str(p.rentalID) + ";" + str(p.clientID) + ";" + str(p.bookID) + ";" + str(p.rentedDate) + ";" + str(p.dueDate) + ";" + str(p.returnedDate) +"\n"
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))

    def removeBookId(self, ID):
        '''
        Remove the rentals with a certain bookid
        '''
        for i in range(len(self.__data) - 1, -1, -1):
            if self.__data[i].bookID == ID:
                del self.__data[i]

    def removeClientId(self, ID):
        '''
        Remove the rentals with a certain clientId
        '''
        for i in range(len(self.__data) - 1, -1, -1):
            if self.__data[i].clientID == ID:
                del self.__data[i]

    def AddRentalsInRepositoryTXT(self, file, Books, Clients):
        with open(file) as f:
            content = f.read().splitlines()
            for line in content:
                words = line.split(";")
                try:
                    date1 = words[3].split('-')
                    date2 = words[4].split('-')
                    date3 = words[5].split('-')
                    rentD = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
                    dueD = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
                    returnedD = datetime.date(int(date3[0]), int(date3[1]), int(date3[2]))
                    notReturned = datetime.date(1, 1, 1)
                    if returnedD != notReturned and Books.StatisticUpdate(int(words[2])) and Clients.StatisticUpdate(int(words[1]), (returnedD - rentD).days):
                        self.add(int(words[0]), int(words[1]), int(words[2]), rentD, dueD, returnedD)
                    elif returnedD == notReturned and Books.StatisticUpdate(int(words[2])):
                        self.add(int(words[0]), int(words[1]), int(words[2]), rentD, dueD, returnedD)

                except:
                    print("DE CE MA URASTI ??")

    def AddRentalsIsRepository(self, Books, Clients):
        date = datetime.date(2016, 11, 15)
        notReturned = datetime.date(1, 1, 1)
        d = datetime.timedelta(days=7)
        self.add(1, 1, 1, date - d, date, date)
        self.add(2, 2, 2, date, date + d, date)
        self.add(3, 3, 3, date - 2 * d, date + d, date + d)
        self.add(4, 4, 4, date - 2 * d, date - d, notReturned)
        self.add(5, 5, 5, date - 3 * d, date - 2 * d, notReturned)
        self.add(6, 6, 6, date - 2 * d, date, notReturned)
        Books.StatisticUpdate(1)
        Books.StatisticUpdate(2)
        Books.StatisticUpdate(3)
        Books.StatisticUpdate(4)
        Books.StatisticUpdate(5)
        Books.StatisticUpdate(6)
        Clients.StatisticUpdate(1, 7)
        Clients.StatisticUpdate(2, 0)
        Clients.StatisticUpdate(3, 21)

    def writeRentalsPickle(self, fileName):
        '''
        fileName = the name of the file
        Rentals = the list of items
        '''
        Rentals = []
        for i in self.__data:
            Rentals.append([str(i.rentalID), str(i.clientID), str(i.bookID), str(i.rentedDate), str(i.dueDate), str(i.returnedDate)])
        f = open(fileName, "wb")
        pickle.dump(Rentals, f)
        f.close()

    def AddRentalsInRepositoryPickle(self, file, Books, Clients):
        for p in self.readBinaryFile(file):
            try:
                date1 = p[3].split('-')
                date2 = p[4].split('-')
                date3 = p[5].split('-')
                rentD = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
                dueD = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
                returnedD = datetime.date(int(date3[0]), int(date3[1]), int(date3[2]))
                notReturned = datetime.date(1, 1, 1)

                if returnedD == notReturned and Books.StatisticUpdate(int(p[2])):
                    self.add(int(p[0]), int(p[1]), int(p[2]), rentD, dueD, returnedD)
                if returnedD != notReturned and Books.StatisticUpdate(int(p[2])) and Clients.StatisticUpdate(int(p[1]), (returnedD - rentD).days):
                    self.add(int(p[0]), int(p[1]), int(p[2]), rentD, dueD, returnedD)
            except :
                print("DE CE MA URASTI ???")

    def AddRentalsInRepositoryDatabase(self, c, conn,Books, Clients):
        c.execute('SELECT * FROM Rentals')
        for p in c.fetchall():
            try:
                date1 = p[3].split('-')
                date2 = p[4].split('-')
                date3 = p[5].split('-')
                rentD = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
                dueD = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
                returnedD = datetime.date(int(date3[0]), int(date3[1]), int(date3[2]))
                notReturned = datetime.date(1, 1, 1)

                if returnedD == notReturned and Books.StatisticUpdate(int(p[2])):
                    self.add(int(p[0]), int(p[1]), int(p[2]), rentD, dueD, returnedD)
                if returnedD != notReturned and Books.StatisticUpdate(int(p[2])) and Clients.StatisticUpdate(int(p[1]), (returnedD - rentD).days):
                    self.add(int(p[0]), int(p[1]), int(p[2]), rentD, dueD, returnedD)
            except :
                print("DE CE MA URASTI ???")
        conn.commit()

    def writeRentalsDatabase(self, c, conn):
        try:
            c.execute('DROP TABLE Rentals')
        except:
            pass
        c.execute('CREATE TABLE Rentals(rentalID INTEGER, clientID INTEGER, bookID INTEGER, rentedDate TEXT, dueDate TEXT, returnedDate TEXT)')
        for i in self.__data:
            c.execute("INSERT INTO Rentals (rentalID, clientID, bookID, rentedDate, dueDate, returnedDate) VALUES  (?, ?, ?, ?, ?, ?)", (i.rentalID, i.clientID, i.bookID, str(i.rentedDate), str(i.dueDate), str(i.returnedDate)))
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

    def add(self, rentalID, clientID, bookID, rentedDate, dueDate, returnedDate):
        """
        Add a client to the repository
        """
        self.__data.append(RentalRepository(rentalID, clientID, bookID, rentedDate, dueDate, returnedDate))

    def CheckId(self, id):
        '''checks if there is a given id into the list'''
        for i in self.__data:
            if id == i.id:
                return False
        return True

    def ItemsInRepo(self, newRepo):
        self.__data = newRepo

    def removeAll(self):
        """
        Remove all data from repository
        """
        self.__data.clear()

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data

    def sortByDueDate(self):
        return self.__data.sort(key=lambda __data: __data.dueDate, reverse=True )

    def getClientID(self):
        return self.clientID

    def getRentedDate(self):
        return self.rentedDate

