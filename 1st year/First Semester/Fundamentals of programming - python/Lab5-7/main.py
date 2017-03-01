from BookClass import Book
from BookRepo import BookRepository
from ClientClass import Client
from ClientRepo import ClientRepository
from RentalClass import Rental
from RentalRepo import RentalRepository
from config import Config
from MenuUI import MenuUI
import tkinter as tk
from gui import MainClass
#import sqlite3



def main():
    ClientRepo = ClientRepository()
    BookRepo = BookRepository()
    RentalRepo = RentalRepository()
    Settings = Config(BookRepo, ClientRepo, RentalRepo)
    TheClientList = Client(ClientRepo)
    TheBookList = Book(BookRepo)
    TheRentalList = Rental(RentalRepo)
    UndoList = []
    RedoList = []

    if Settings.getUI() == 1:
        root = tk.Tk()
        app = MainClass(root, TheBookList, TheClientList, TheRentalList, UndoList, RedoList, Settings)
        root.mainloop()
        # conn = sqlite3.connect('database.db')
        # c = conn.cursor()
        # TheBookList.saveDB(c, conn)
        # TheClientList.saveDB(c, conn)
        # TheRentalList.saveDB(c, conn)
        # c.close()
        # conn.close()
    else:
        Ui = MenuUI(TheBookList, TheClientList, TheRentalList, UndoList, RedoList, Settings)
    # while True:
    #     command = input("Please input the command : ")
    #     if command == "1":
    #         Ui = MenuUI(TheBookList, TheClientList, TheRentalList, UndoList, RedoList)
    #         break
    #     if command == "2":
    #         root = tk.Tk()
    #         app = MainClass(root, TheBookList, TheClientList, TheRentalList, UndoList, RedoList)
    #         root.mainloop()
    #         break





main()