from Functions import AddApartment, removeApartment,readCommand,replaceExpense,filterApartments, shrink, sumExpense, undo, AddApartments, PrintInfo


def AddApartmentUI(ApartmentList, UndoList):
    '''
    Prints an apartment
    Input: ApartmentList
    Output: -
    '''
    while True:
        try:
            apartment = input("Please type the apartment : ")
            apartment = int(apartment)
            break
        except:
            print("Error ! Please type correctly")

    typeOfExpense = input("Please type the type of expense : ")
    while True:
        try:
            amount = input("Please type the amount : ")
            amount = int(amount)
            break
        except:
            print("Error ! Please type correctly")
    AddApartment(ApartmentList,['', apartment,typeOfExpense,amount], UndoList)


def RemoveMenuUI(ApartmentList, UndoList):
    '''
    Prints the remove menu
    input: -
    output: the menu is printed at the console
    '''
    str = "\nIn Order to modify the apartment list, you must select one of the options below:\n"
    str += "\t1 - to remove the information about a specific apartment\n"
    str += "\t2 - to remove the information about a specific type of apartment\n"
    str += "\t3 - to remove all the expenses from apartments between given values\n"
    str += "\t4 - to replace the value of a certain apartment\n"
    str += "\t0 - to exit the menu\n"
    while True:
        print(str)
        command = input("Enter the command :")
        if validInputCommand(command, "RemoveMenu"):
            if command == "0":
                break
            if command == "1":
                RemoveApartmentUI(ApartmentList, UndoList)
            if command == "2":
                RemoveTypeOfApartmentUI(ApartmentList, UndoList)
            if command == "3":
                RemoveSeveralApartmentsUI(ApartmentList, UndoList)
            if command == "4":
                ReplaceAmountUI(ApartmentList, UndoList)


def RemoveApartmentUI(ApartmentList, UndoList):
    '''
    Removes an apartment
    Input: ApartmentList
    Output: -
    '''
    while True:
        try:
            apartment = input("Please type the apartment : ")
            apartment = int(apartment)
            break
        except:
            print("Error ! Please type correctly")
    removeApartment(ApartmentList, ['', apartment], UndoList)


def RemoveTypeOfApartmentUI(ApartmentList, UndoList):
    '''
    Removes all the apartments of a certain type
    Input: ApartmentList
    Output: -
    '''
    typeOfApartment = input("Please type the type of expense : ")
    removeApartment(ApartmentList, ['', typeOfApartment], UndoList)

def RemoveSeveralApartmentsUI(ApartmentList, UndoList):
    '''
    Removes several apartments between two given values
    Input: ApartmentList
    Output: -
    '''
    while True:
        try:
            argumentOne = input("Please type the start apartment : ")
            argumentOne = int(argumentOne)
            break
        except:
            print("Error ! Please type correctly")
    while True:
        try:
            argumentTwo = input("Please type the end apartment : ")
            argumentTwo = int(argumentTwo)
            break
        except:
            print("Error ! Please type correctly")
    removeApartment(ApartmentList, ['', argumentOne, 'to', argumentTwo], UndoList)


def ReplaceAmountUI(ApartmentList, UndoList):
    '''
    Replaces the amount of expanse of a certain apartment
    Input: ApartmentList
    Output: -
    '''
    while True:
        try:
            apartment = input("Please type the apartment : ")
            apartment = int(apartment)
            break
        except:
            print("Error ! Please type correctly")
    typeOfExpense = input("Please type the type of expense : ")
    while True:
        try:
            amount = input("Please type the amount : ")
            amount = int(amount)
            break
        except:
            print("Error ! Please type correctly")
    replaceExpense(ApartmentList,["",apartment,typeOfExpense,"with",amount], UndoList)




def ListMenu(ApartmentList):
    '''
    Prints the list menu
    input: -
    output: the menu is printed at the console
    '''
    str = "\nIn Order to view the apartment list, you must select one of the options below:\n"
    str += "\t1 - to list all the apartments\n"
    str += "\t2 - to list a specific apartment\n"
    str += "\t3 - to write all the apartments having total expenses [ < | = | > ] of a given value\n"
    str += "\t0 - to exit the menu\n"
    while True:
        print(str)
        command = input("Enter the command :")
        if validInputCommand(command, "List Menu"):
            if command == "0":
                break
            if command == "1":
                PrintInfo(ApartmentList)
            if command == "2":
                ListAnApartment(ApartmentList)
            if command == "3":
                ListExpanses(ApartmentList)


def ListAnApartment(ApartmentList):
    '''
    Prints an apartment
    Input: ApartmentList
    Output: -
    '''
    while True:
        try:
            apartment = input("Please type the apartment : ")
            apartment = int(apartment)
            break
        except:
            print("Error ! Please type correctly")

    for i in range(len(ApartmentList) - 1, -1, -1):
        if ApartmentList[i].apartment == apartment:
            print(ApartmentList[i])


def ListExpanses(ApartmentList):
    '''
    Prints the apartments with a certain characteristic
    Input: ApartmentList
    Output: -
    '''
    while True:
        operator = input("Please input one of the the operators [ < | = | > ] : ")
        if operator == "<" or operator == "=" or operator == ">":
            break
        else:
            print("Error ! Please type correctly")

    while True:
        try:
            amount = input("Please type the amount : ")
            amount = int(amount)
            break
        except:
            print("Error ! Please type correctly")
    if operator == "<":
        for i in ApartmentList:
            if i.amount < amount:
                print(i)
    if operator == ">":
        for i in ApartmentList:
            if i.amount > amount:
                print(i)
    if operator == "=":
        for i in ApartmentList:
            if i.amount == amount:
                print(i)


def SumMaxSortList(ApartmentList):
    '''
    Prints the sum,max and sort menu
    input: -
    output: the menu is printed at the console
    '''
    str = "\nAvailable commands\n"
    str += "\t1 - to write the total amount for a given expense\n"
    str += "\t2 - to write the maximum amount per each expense type for given apartment\n"
    str += "\t3 - to write the list of apartments sorted ascending by total amount of expenses\n"
    str += "\t4 - to write the total amount of expenses for each type, sorted ascending by amount of money\n"
    str += "\t0 - to exit the menu\n"
    while True:
        print(str)
        command = input("Enter the command :")
        if validInputCommand(command, "Sum, Max, Sort Menu"):
            if command == "0":
                break
            if command == "1":
                Sum(ApartmentList)
            if command == "2":
                Max(ApartmentList)
            if command == "3":
                SortApartment(ApartmentList)
            if command == "4":
                SortType(ApartmentList)


def Max(ApartmentList):
    maxim = -1
    listExpense = []
    lastType = ''
    while True:
        try:
            apartment = input("Please type the apartment : ")
            apartment = int(apartment)
            break
        except:
            print("Error ! Please type correctly")
    for i in ApartmentList:
        if i.apartment == apartment:
            listExpense.append(i)
    if len(listExpense) == 0:
        print("Invalid Apartment")
        return
    if len(listExpense) == 1:
        print(listExpense[0])
        return
    listExpense.sort(key=lambda Expense: Expense.typeOfApartment, reverse=True)

    for i in range(len(listExpense) - 1, -1, -1):
        if i == len(listExpense) - 1:
            maxim = listExpense[i].amount
            lastType = listExpense[i].typeOfApartment
            continue
        if listExpense[i].typeOfApartment != listExpense[i + 1].typeOfApartment:
            print("Apartment : " + str(
                listExpense[i].apartment) + ", type of expense : " + lastType + ", with the amount : " + str(maxim))
            maxim = listExpense[i].amount
            lastType = listExpense[i].typeOfApartment
            continue
        if maxim < listExpense[i].amount:
            maxim = listExpense[i].amount
    print("Apartment : " + str(
        listExpense[i].apartment) + ", type of expense : " + lastType + ", with the amount : " + str(maxim))


def Sum(ApartmentList):
    '''
     Writes the total amount for a given expense
     Input: ApartmentList
     Output : -
    '''
    typeOfExpense = input("Please type the type of expense : ")
    sumExpense(ApartmentList, ['', typeOfExpense])

def SortApartment(ApartmentList):
    '''
    Sorts the apartments according to the amount of expense they have
    Input: ApartmentList
    Output : -
    '''

    newList = []
    newList = shrink(ApartmentList, newList)
    newList.sort(key=lambda newList: newList.amount)
    PrintInfo(newList)


def SortType(ApartmentList):
    '''
    Writes the total amount of expenses for each type, sorted ascending by amount of money
    Input: ApartmentList
    Output : -
    '''

    newList = []
    newList = shrink(ApartmentList, newList)
    newList.sort(key=lambda newList: newList.typeOfApartment)
    if len(ApartmentList) < 1:
        return
    lista = []
    lastType = newList[0].typeOfApartment  # set the last type to first one on first run
    for i in newList:
        if lastType != i.typeOfApartment:  # looks like this is a different type than last one
            lastType = i.typeOfApartment  # change last type for next iteration
            printList(lista)  # print the current list
            lista = []  # prepare the list for the new entries
            lista.append(i)  # since this entry didnt match the last one, already append it
        else:
            lista.append(i)  # no change here, just append
    printList(
        lista)  # last category will never get a chance to get printed because the loop ends before the category changes  # last category will never get a chance to get printed because the loop ends before the category changes



def printList(lista):
    '''
    Prints the list
    input: -
    output: the menu is printed in the console
    '''
    sum = 0
    for i in sorted(lista, key=lambda x: x.amount):
        print(i)
        sum += i.amount
    print("Total:", sum)


def filterMenuUI(ApartmentList, UndoList):
    '''
    Prints the filter menu
    input: ApartmentList
    output: the menu is printed at the console
    '''
    str = "\nAvailable commands\n"
    str += "\t1 - to filter by type\n"
    str += "\t2 - to filter by amount\n"
    str += "\t0 - to exit the menu\n"
    while True:
        print(str)
        command = input("Enter the command :")
        if validInputCommand(command, "Filter Menu"):
            if command == "0":
                break
            if command == "1":
                filterApartmentsTypeUI(ApartmentList, UndoList)
            if command == "2":
                filterApartmentsAmountUI(ApartmentList, UndoList)


def filterApartmentsTypeUI(ApartmentList, UndoList):
    '''
        Filter by type
        Input : ApartmentList, UndoList
        Output : -
    '''

    type = input("Please type the type of the apartment : ")
    filterApartments(ApartmentList, ['', type], UndoList)

def filterApartmentsAmountUI(ApartmentList, UndoList):
    '''
        Filter by amount
        Input : ApartmentList, UndoList
        Output : -
    '''
    while True:
        try:
            amount = input("Please type the amount of the apartment : ")
            amount = int(amount)
            break
        except:
            print("Error ! Please type correctly")
    filterApartments(ApartmentList, ['', amount], UndoList)


def PrintMenu():
    '''
    Prints the available menu for the problem
    input: -
    output: the menu is printed at the console
    '''
    str = "\nAvailable commands :\n"
    str += "\t1 - to add a new transaction to the list \n"
    str += "\t2 - to modify expenses from the list.\n"
    str += "\t3 - to write the expenses having different properties. \n"
    str += "\t4 - to obtain different characteristics of the expenses. \n"
    str += "\t5 - to filter\n"
    str += "\t6 - to undo the last operation that modified program data \n"
    str += "\t0 - to exit the menu"
    print(str)


def validInputCommand(command, typeOfMenu):
    '''
    Verify if the command is valid
    input: command
    output: true / false
    '''
    if typeOfMenu == "Principal Menu":
        availableCommands = ['1', '2', '3', '4', '5', '6', '0']
    if typeOfMenu == "List Menu":
        availableCommands = ['1', '2', '3', '0']
    if typeOfMenu == "RemoveMenu":
        availableCommands = ['1', '2', '3', '4', '0']
    if typeOfMenu == "Sum, Max, Sort Menu":
        availableCommands = ['1', '2', '3', '4', '5', '0']
    if typeOfMenu == "Filter Menu":
        availableCommands = ['1', '2', '0']

    return (command in availableCommands)



def mainMenu():
    ApartmentList = []
    AddApartments(ApartmentList)
    UndoList = []

    while True:
        PrintMenu()
        command = input("Enter the command: ")
        if validInputCommand(command, "Principal Menu"):
            if command == "0":
                break
            if command == "1":
                AddApartmentUI(ApartmentList, UndoList)
            if command == "2":
                RemoveMenuUI(ApartmentList, UndoList)
            if command == "3":
                ListMenu(ApartmentList)
            if command == "4":
                SumMaxSortList(ApartmentList)
            if command == "5":
                filterMenuUI(ApartmentList, UndoList)
            if command == "6":
                ApartmentList = undo(ApartmentList, UndoList)

