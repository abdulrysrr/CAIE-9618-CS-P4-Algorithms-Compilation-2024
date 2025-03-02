def PrintArray():
    global StackPointer
    print("StackPointer is: ",StackPointer)
    for x in range (0, 10):
        print(StackData[x])

def Push(Data):
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = Data
        StackPointer = StackPointer + 1
        return True

def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        ReturnData = StackData[StackPointer - 1]
        StackPointer = StackPointer - 1
        return ReturnData

StackPointer = 0
StackData = [0 for x in range(10)]
for x in range(0, 11):
    TempNumber = int(input("Enter a number: "))
    if Push(TempNumber) == True:
        print("Stored")
    else:
        print("Stack full")
PrintArray()