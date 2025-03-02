def PrintArray(DataArray):
    output = ""
    for X in range(0, len(DataArray)):
        output = output + str((DataArray[X])) + " "
    print(output)

def LinearSearch(DataArray, DataToFind):
    Count = 0
    for X in range(0, len(DataArray)):
        if(DataArray[X] == DataToFind):
            Count +=1
    return Count

DataArray = [0]*25
try:
    NumFile = open("Data.txt",'r')
    for Line in NumFile:
        DataArray.append(int(Line))
    NumFile.close()
except IOError:
    print("Could not find file")
PrintArray(DataArray)

DataToFind = int(input("Enter a number to find "))
while DataToFind < 0 or DataToFind > 100:
    DataToFind = int(input("Enter a number to find "))
NumberTimes = LinearSearch(DataArray, DataToFind)
print("The number", DataToFind, "is found", NumberTimes, "times")