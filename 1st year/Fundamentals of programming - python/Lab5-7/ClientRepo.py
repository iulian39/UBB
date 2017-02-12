import datetime
import pickle

class ClientRepository:
    __data = []
    clientId = 0
    name = ""
    days = 0

    def __init__(self):
        """
        Constructor for ClientRepository class
        """
        self.__data = []

    def __init__(self, clientId=0, name=""):
        self.clientId = clientId
        self.name = name
        self.days = 0

    def __str__(self):
        return "Client id : %s,name : %s" % (self.clientId, self.name)

    @property
    def id(self):
        return self.clientId

    @id.setter
    def id(self, arg):
        self.clientId = arg

    def AddClientsInRepositoryPickle(self, file):
        for p in self.readBinaryFile(file):
            try:
                self.add(int(p[0]), p[1])
            except:
                pass

    def AddClientsInRepositoryDatabase(self, c, conn):
        c.execute('SELECT * FROM Clients')
        for row in c.fetchall():
            try:
                self.add(int(row[0]), row[1])
            except:
                pass
        conn.commit()

    def writeClientsDatabase(self, c, conn):
        try:
            c.execute('DROP TABLE Clients')
        except:
            pass
        c.execute('CREATE TABLE Clients(clientId INTEGER, name TEXT)')
        for i in self.__data:
            c.execute("INSERT INTO Clients (clientId, name) VALUES  (?, ?)", (i.clientId, i.name))
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

    def writeClientsPickle(self, fileName):
        '''
        fileName = the name of the file
        books = the list of items
        '''
        clients = []
        for i in self.__data:
            clients.append([i.clientId, i.name])
        f = open(fileName, "wb")
        pickle.dump(clients, f)
        f.close()

    def AddClientsInRepositoryTXT(self, file):
        with open(file) as f:
            content = f.read().splitlines()
            for line in content:
                words = line.split(";")
                try:
                    self.add(int(words[0]), words[1])
                except:
                    pass

    def writeClientsText(self, fileName):
        f = open(fileName, "w")
        try:
            for p in self.__data:
                pString = str(p.clientId) + ";" + p.name + "\n"
                f.write(pString)
            f.close()
        except Exception as e:
            print("An error occured -" + str(e))

    def AddClientsInRepository(self):
        self.add(1, "George")
        self.add(2, "Vasile")
        self.add(3, "Grigore")
        self.add(4, "Ionel")
        self.add(5, "Costel")
        self.add(6, "Ana")
        self.add(7, "Adina")
        self.add(8, "Gabriela")
        self.add(9, "Daniel")
        self.add(10, "Delia")
        self.add(11, "George")
        self.add(12, "Vasile")
        self.add(13, "Grigore")
        self.add(14, "Daniel")
        self.add(15, "Costel")
        self.add(16, "Ana")
        self.add(17, "Adina")
        self.add(18, "Fergus")
        self.add(19, "Georgeta")
        self.add(20, "Delia")
        self.add(21, "George")
        self.add(22, "Vasile")
        self.add(23, "Grigore")
        self.add(24, "Ionel")
        self.add(25, "Costel")
        self.add(26, "Ana")
        self.add(27, "Adina")
        self.add(28, "Daniel")
        self.add(29, "Fergus")
        self.add(30, "Delia")
        self.add(31, "George")
        self.add(32, "Vasile")
        self.add(33, "Grigore")
        self.add(34, "Ionel")
        self.add(35, "Costelus")
        self.add(36, "Anton")
        self.add(37, "Adin")
        self.add(38, "Yuri")
        self.add(39, "Norbert")
        self.add(40, "Alice")
        self.add(41, "Suciu")
        self.add(42, "Vasilica")
        self.add(43, "Daniel")
        self.add(44, "Ion")
        self.add(45, "Costica")
        self.add(46, "Ananas")
        self.add(47, "Adina D")
        self.add(48, "Gabriela B")
        self.add(49, "Georget")
        self.add(50, "Fergus")

    def add(self, clientId, name):
        """
        Add a client to the repository
        """
        self.__data.append(ClientRepository(clientId, name))

    def remove(self, id):
        '''
        Remove a client from the repository
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

    def updateName(self, ID, newName):
        '''
        Update the name of a client
        '''
        for i in self.__data:
            if i.id == ID:
                i.name = newName

    def CheckId(self, id):
        '''
        checks if there is a given id into the list
        '''
        for i in self.__data:
            if id == i.id:
                return False
        return True

    def removeAll(self):
        """
        Remove all data from repository
        """
        self.__data.clear()

    def ItemsInRepo(self, newRepo):
        self.__data = newRepo

    def getAll(self):
        """
        Return all repository data
        Returns the live list of the repository
        """
        return self.__data


    # def setAll(self, UndoList):
    #     self.__data.clear()
    #     self.__data = UndoList
    #     return self.__data

    def get(self, index):
        """
        Get a number from the repository
        index - Index of the number
        RepositoryException - If an invalid position is given
        """
        return self.__data[index]

    def StatisticUpdate(self, TheID, dayz):
        ok = False
        for i in self.__data:
            if i.id == TheID:
                i.IncrementDays(dayz)
                ok = True
        if ok == True:
            return True
        return False

    def IncrementDays(self, _days):
        '''
        Increments active days of a client
        '''
        self.days += _days + 1

