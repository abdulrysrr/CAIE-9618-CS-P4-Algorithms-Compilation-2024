class node:
    def __init__(self, theData, nextNodeNumber):
        self.data = theData
        self.nextNode = nextNodeNumber

def addNode(linkedList, currentPointer, emptyList):
    dataToAdd = input("Enter the data to add: ")
    if emptyList <0 or emptyList > 9:
        return False
    else:
        newNode = node(int(dataToAdd), -1)
        linkedList[emptyList] = newNode
        previousPointer = 0
        while(currentPointer != -1):
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
    return True

def outputNodes(linkedList, currentPointer):
        while(currentPointer != -1):
            print(str(linkedList[currentPointer].data))
            currentPointer = linkedList[currentPointer].nextNode
        
linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,7),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5
outputNodes(linkedList, startPointer)
returnValue = addNode(linkedList, startPointer, emptyList)
if returnValue == True:
    print("Item successfully added")
else:
    print("Item not added, list full")
outputNodes(linkedList, startPointer)