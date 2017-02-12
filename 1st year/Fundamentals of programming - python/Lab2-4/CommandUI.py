from Functions import AddApartment, removeApartment,readCommand,replaceExpense,filterApartments, shrink, sumExpense, undo, AddApartments, PrintInfo


def listApartments(ApartmentList, cmd):
    '''
    Lists the apartmets
    Input: ApartmentList, cmd
    Output: -
    '''
    if len(cmd) == 0:
        PrintInfo(ApartmentList)
    elif len(cmd) == 2:
        try:
            cmd[1] = int(cmd[1])
        except:
            print("Invalid input. Nothing happened")
            return
        for i in range(len(ApartmentList) - 1, -1, -1):
            if ApartmentList[i].apartment == cmd[1]:
                print(ApartmentList[i])
    elif len(cmd) == 3:
        try:
            cmd[2] = int(cmd[2])
        except:
            print("Invalid input. Nothing happened")
            return
        if cmd[1] == "<":
            ok = True
            for i in ApartmentList:
                if i.amount < cmd[2]:
                    print(i)
        if cmd[1] == ">":
            ok = True
            for i in ApartmentList:
                if i.amount > cmd[2]:
                    print(i)
        if cmd[1] == "=":
            ok = True
            for i in ApartmentList:
                if i.amount == cmd[2]:
                    print(i)
        if ok == False:
            print("Invalid input. Nothing happened")
            return
    else:
        print("Invalid input. Nothing happened")
        return


def maxExpense(ApartmentList, cmd):
    '''
    Write the maximum amount per each expense type for a given apartment
    Input: ApartmentList, cmd
    Output: -
    '''
    maxim = -1
    listExpense = []
    lastType = ''
    if len(cmd) != 2:
        print("Invalid input. Nothing happened")
        return
    try:
        cmd[1] = int(cmd[1])
    except:
        print("Invalid input. Nothing happened")
        return
    for i in ApartmentList:
        if i.apartment == cmd[1]:
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
            print("Apartment : " + str(listExpense[i].apartment) + ", type of expense : " + lastType + ", with the amount : " + str(maxim))
            maxim = listExpense[i].amount
            lastType = listExpense[i].typeOfApartment
            continue
        if maxim < listExpense[i].amount:
            maxim = listExpense[i].amount
    print("Apartment : " + str(
        listExpense[i].apartment) + ", type of expense : " + lastType + ", with the amount : " + str(maxim))


def sort(ApartmentList, cmd):
    '''
   Sorts the apartments according to the amount of expense they have
   Input: ApartmentList
   Output : -
   '''
    if len(cmd) != 2:
        print("Invalid input. Nothing happened")
        return
    if cmd[1] == "apartment":
        newList = []
        newList = shrink(ApartmentList, newList)
        newList.sort(key=lambda newList: newList.amount)
        PrintInfo(newList)
    elif cmd[1] == "type":
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
            lista)  # last category will never get a chance to get printed because the loop ends before the category changes
    else:
        print("Invalid input. Nothing happened")
        return



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

def HelpMenu():
    '''
    Prints the help menu for the problem
    input: -
    output: the menu is printed in the console
    '''
    str = "\nAvailable commands :\n"
    str += "\tadd <apartment> <type> <amount>\n"
    str += "\tremove <apartment>\n"
    str += "\tremove <start apartment> to <end apartment>\n"
    str += "\tremove <type>\n"
    str += "\treplace <apartment> <type> with <amount>\n"
    str += "\tlist\n"
    str += "\tlist <apartment>\n"
    str += "\tlist [ < | = | > ] <amount>\n"
    str += "\tsum <type>\n"
    str += "\tmax <apartment>\n"
    str += "\tsort <apartment>\n"
    str += "\tsort type\n"
    str += "\tfilter <type>\n"
    str += "\tfilter <value>\n"
    str += "\tundo\n"
    str += "\t help\n"
    str += "\texit"
    print(str)


def mainCommand():
    ApartmentList = []
    UndoList = []
    AddApartments(ApartmentList)
    #testAddApartment(ApartmentList)
    #testRemoveApartment(ApartmentList)
    while True:
        cmd = readCommand()
        command = cmd[0]
        params = cmd[1]

        if command == 'add':
            AddApartment(ApartmentList, params, UndoList)
        elif command == 'remove':
            removeApartment(ApartmentList, params, UndoList)
        elif command == 'list':
            listApartments(ApartmentList, params)
        elif command == 'replace':
            replaceExpense(ApartmentList, params, UndoList)
        elif command == 'sum':
            sumExpense(ApartmentList, params)
        elif command == 'max':
            maxExpense(ApartmentList, params)
        elif command == 'sort':
            sort(ApartmentList, params)
        elif command == 'filter':
            filterApartments(ApartmentList, params, UndoList)
        elif command == 'undo':
            ApartmentList = undo(ApartmentList,UndoList)
        elif command == 'help':
            HelpMenu()
        elif command == 'exit':
            break
        else:
            print("Invalid command!")




def testAddApartment(ApartmentList):
    params = ['add', '18', 'petrol', '18']
    AddApartment(ApartmentList, params)
    assert (len(ApartmentList) == 12)
    params = ['add', 'a18', 'water', '18']
    AddApartment(ApartmentList, params)
    assert (len(ApartmentList) == 12)

def testRemoveApartment(ApartmentList):
    params = ['remove', '17']
    removeApartment(ApartmentList, params)
    assert (len(ApartmentList) == 11)
    params = ['remove', '19']
    removeApartment(ApartmentList, params)
    assert (len(ApartmentList) == 11)
    params = ['remove', '20', 'to', '30']
    removeApartment(ApartmentList, params)
    assert (len(ApartmentList) == 11)
    params = ['remove', '16', 'to', '18']
    removeApartment(ApartmentList, params)
    assert (len(ApartmentList) == 9)
    params = ['remove', 'gas']
    removeApartment(ApartmentList, params)
    assert (len(ApartmentList) == 4)


