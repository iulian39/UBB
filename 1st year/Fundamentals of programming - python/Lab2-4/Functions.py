import copy

class Expanse:
    apartment = 0
    typeOfApartment = ""
    amount = 0

    def __init__(self, apartment = 0, typeOfApartment = "", amount = 0):
        self.apartment = apartment
        self.typeOfApartment = typeOfApartment
        self.amount = amount

    def __str__(self):
        return "Apartment : %s,type of expense : %s,amount : %s" % (self.apartment, self.typeOfApartment, self.amount)

def AddApartments(ApartmentList):
    ApartmentList.append(Expanse(10, "gas", 449))
    ApartmentList.append(Expanse(11, "gas", 465))
    ApartmentList.append(Expanse(12, "water", 14))
    ApartmentList.append(Expanse(12, "water", 80))
    ApartmentList.append(Expanse(12, "gas", 14))
    ApartmentList.append(Expanse(12, "gas", 74))
    ApartmentList.append(Expanse(13, "gas", 450))
    ApartmentList.append(Expanse(14, "water", 13))
    ApartmentList.append(Expanse(15, "soda", 15))
    ApartmentList.append(Expanse(16, "soda", 17))
    ApartmentList.append(Expanse(17, "petrol", 250))


def AddApartment(ApartmentList, cmd, UndoList):
    '''
    Adds an apartment
    Input: ApartmentList, cmd
    Output: -
    '''
    if len(cmd) != 4:
        return "Invalid input. Apartment was not added"
    try:
        cmd[1] = int(cmd[1])
        cmd[3] = int(cmd[3])
    except:
        return "Invalid input. Apartment was not added"
    save = copy.deepcopy(ApartmentList)
    UndoList.append(save)
    ApartmentList.append(Expanse(cmd[1], cmd[2], cmd[3]))
    return "Apartment was added successfully"

def removeApartment(ApartmentList, cmd, UndoList):
    '''
    Removes an apartment
    Input: ApartmentList, cmd
    Output: -
    '''
    cnt = 0
    if len(cmd) == 2:
        try:
            cmd[1] = int(cmd[1])
        except:
            for i in range(len(ApartmentList) - 1, -1, -1):
                if ApartmentList[i].typeOfApartment == cmd[1]:
                    cnt += 1
                    del ApartmentList[i]
            if cnt != 0:
                return "Apartments successfully removed : " + str(cnt)
            else:
                return "No removal happened !"
            return
        save = copy.deepcopy(ApartmentList)
        UndoList.append(save)
        for i in range(len(ApartmentList) - 1, -1, -1):
            if ApartmentList[i].apartment == cmd[1]:
                cnt += 1
                del ApartmentList[i]
        if cnt != 0:
            return "Apartments successfully removed : " + str(cnt)
        else:
            UndoList.pop()
            return "No removal happened !"
    elif len(cmd) == 4:
        if cmd[2] == "to" or cmd[2] == "TO":
            try:
                cmd[1] = int(cmd[1])
                cmd[3] = int(cmd[3])
            except:
                return "Invalid input. No removal happened"
        save = copy.deepcopy(ApartmentList)
        UndoList.append(save)
        for i in range(len(ApartmentList) - 1, -1, -1):
            if ApartmentList[i].apartment >= cmd[1] and ApartmentList[i].apartment <= cmd[3]:
                cnt += 1
                del ApartmentList[i]
        if cnt != 0:
            return "Apartments successfully removed : " + str(cnt)
        else:
            UndoList.pop()
            return "No removal happened !"
    else:
        return "Invalid input. Nothing happened"

def replaceExpense(ApartmentList, cmd, UndoList):
    '''
    Replaces the amount of the expense
    Input: ApartmentList, cmd
    Output: -
    '''
    if len(cmd) != 5:
        return "Invalid input. Nothing happened"
    if cmd[3] == "with" or cmd[3] == "WITH":
        try:
            cmd[1] = int(cmd[1])
            cmd[4] = int(cmd[4])
        except:
            return "Invalid input. Nothing happened"
    else:
        return "Invalid input. Nothing happened"
    save = copy.deepcopy(ApartmentList)
    UndoList.append(save)
    for i in range(len(ApartmentList) - 1, -1, -1):
        if ApartmentList[i].apartment == cmd[1] and ApartmentList[i].typeOfApartment == cmd[2]:
            ApartmentList[i].amount = cmd[4]
            ok = True
    if ok == False:
        UndoList.pop()
        return "No modify happened"
    else:
        return "Operation done successfully"

def shrink(ApartmentList, newList):
    newList = []
    ApartmentList.sort(key=lambda Apartment: Apartment.apartment)
    sum = 0
    for i in range(0, len(ApartmentList)):
        if i + 1 == len(ApartmentList):
            newList.append(Expanse(ApartmentList[i].apartment, ApartmentList[i].typeOfApartment, ApartmentList[i].amount))
            continue
        if ApartmentList[i].apartment == ApartmentList[i + 1].apartment and ApartmentList[i].typeOfApartment == ApartmentList[i + 1].typeOfApartment:
            sum += ApartmentList[i].amount
        else:
            newList.append(Expanse(ApartmentList[i].apartment, ApartmentList[i].typeOfApartment, ApartmentList[i].amount + sum))
            sum = 0
    return newList

def undo(ApartmentList, UndoList):
    if len(UndoList)== 0:
        print("There is nothing to undo")
        return ApartmentList
    ApartmentList=UndoList[len(UndoList)-1]
    UndoList.pop()
    return ApartmentList

def sumExpense(ApartmentList, cmd):
    '''
    Write the total amount for the given expenses
    Input: ApartmentList, cmd
    Output: -
    '''
    if len(cmd) != 2:
        return "Invalid input. Nothing happened"
    sumOfExpanses = 0
    for i in ApartmentList:
        if i.typeOfApartment == cmd[1]:
            sumOfExpanses += i.amount
    return "The total amount for the expenses having type '" + str(cmd[1]) + "' is : " + str(sumOfExpanses)

def filterApartments(ApartmentList, cmd, UndoList):
    if len(cmd) != 2:
        return "Invalid input. Nothing happened"
    try:
        cmd[1] = int(cmd[1])
    except:
        save = copy.deepcopy(ApartmentList)
        UndoList.append(save)
        cnt = 0
        for i in range(len(ApartmentList) - 1, -1, -1):
            if ApartmentList[i].typeOfApartment != cmd[1]:
                del ApartmentList[i]
                cnt += 1
        if cnt == 0:
            UndoList.pop()
        else:
            newList = []
            newList = shrink(ApartmentList, newList)
            PrintInfo(newList)
        return
    cnt = 0
    save = copy.deepcopy(ApartmentList)
    UndoList.append(save)
    for i in range(len(ApartmentList) - 1, -1, -1):
        if ApartmentList[i].amount > cmd[1]:
            cnt += 1
            del ApartmentList[i]
    if cnt == 0:
        UndoList.pop()
    else:
        newList = []
        newList = shrink(ApartmentList, newList)
        PrintInfo(newList)



def PrintInfo(ApartmentList):
    '''
    Prints all the list
    Input: ApartmentList
    Output: -
    '''
    for i in ApartmentList:
        print(i)

def readCommand():
    '''
    Read and parse user commands
    input: -
    output: (command, params) tuple, where:
            command is user command
            params are parameters
    '''
    cmd = input("Plese input the command: ")
    if cmd.find(" ") == -1:
        command = cmd
        params = ""
    else:
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(" "):]
        params = params.split(" ")
        for i in range(0, len(params)):
            params[i] = params[i].strip()
    return (command, params)