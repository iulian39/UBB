import configparser
from Repos import *
import sqlite3

class Config:
    def __init__(self, BookRepo, ClientRepo, RentalRepo):
        self.__ui = -1
        self.settings = configparser.ConfigParser()
        self.settings._interpolation = configparser.ExtendedInterpolation()
        self.settings.read('properties.ini')
        if self.settings['DATA']['repository'] == 'INMEMORY':
            BookRepo.AddBooksInRepository()
            ClientRepo.AddClientsInRepository()
            RentalRepo.AddRentalsIsRepository(BookRepo, ClientRepo)
            if self.settings['DATA']['ui'] == '1':
                self.setUi(1)
            else:
                self.setUi(0)
        elif self.settings['DATA']['repository'] == 'TEXT':
            BookRepo.AddBooksInRepositoryTXT(self.settings['DATA']['Books'])
            ClientRepo.AddClientsInRepositoryTXT(self.settings['DATA']['Clients'])
            RentalRepo.AddRentalsInRepositoryTXT(self.settings['DATA']['Rentals'], BookRepo, ClientRepo)
            if self.settings['DATA']['ui'] == '1':
                self.setUi(1)
            else:
                self.setUi(0)
        elif self.settings['DATA']['repository'] == 'PICKLE':
            BookRepo.AddBooksInRepositoryPickle(self.settings['DATA']['Books'])
            ClientRepo.AddClientsInRepositoryPickle(self.settings['DATA']['Clients'])
            RentalRepo.AddRentalsInRepositoryPickle(self.settings['DATA']['Rentals'], BookRepo, ClientRepo)
            if self.settings['DATA']['ui'] == '1':
                self.setUi(1)
            else:
                self.setUi(0)
        elif self.settings['DATA']['repository'] == 'DATABASE':
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS Clients(clientId INTEGER, name TEXT)')
            c.execute('CREATE TABLE IF NOT EXISTS Books(bookID INTEGER, title TEXT, description TEXT, author TEXT)')
            c.execute('CREATE TABLE IF NOT EXISTS Rentals(rentalID INTEGER, clientID INTEGER, bookID INTEGER, rentedDate TEXT, dueDate TEXT, returnedDate TEXT)')
            BookRepo.AddBooksInRepositoryDatabase(c, conn)
            ClientRepo.AddClientsInRepositoryDatabase(c, conn)
            RentalRepo.AddRentalsInRepositoryDatabase(c, conn,BookRepo, ClientRepo)
            c.close()
            conn.close()
            if self.settings['DATA']['ui'] == '1':
                self.setUi(1)
            else:
                self.setUi(0)
        else:
            BookRepo.AddBooksInRepository()
            ClientRepo.AddClientsInRepository()
            RentalRepo.AddRentalsIsRepository(BookRepo, ClientRepo)
            self.setUi(0)



    def setUi(self, ui):
        self.__ui = ui

    def getUI(self):
        return self.__ui

    def GetTypeOfRepo(self):
        return self.settings['DATA']['repository']

    def GetBookFile(self):
        return self.settings['DATA']['Books']

    def GetClientFile(self):
        return self.settings['DATA']['Clients']

    def GetRentalFile(self):
        return self.settings['DATA']['Rentals']



