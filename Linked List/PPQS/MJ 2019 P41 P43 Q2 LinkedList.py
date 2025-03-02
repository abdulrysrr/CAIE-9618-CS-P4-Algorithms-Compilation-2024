def insert(data):
    global currentPointer
    ListLength = len(LinkedList)
    if ListLength == 0: #if list does not have nodes
        LinkedList.append([data,-1]) #then append to list
    else:
        LinkedList.append([data,-1]) #append to list 
        EntryPointer = ListLength 
        LinkedList[currentPointer][1] = EntryPointer #then set pointer of previous node to newly added node
        currentPointer = EntryPointer #update global pointers

def insertAt(data,index):
    ListLength = len(LinkedList)
    if ListLength == 0: #if list does not have nodes
        print("Sorry, list does not exist.")
    elif index>=ListLength:
        print("Sorry, index is out of bounds.")
    else:
        currentPointer = headpointer 
        count = 1
        while count != index and currentPointer!= -1: #traerse list until 
            currentPointer = LinkedList[currentPointer][1] #then set pointer of previous node to newly added node
            count +=1
        LinkedList.append([data,-1]) #append to list 
        EntryPointer = ListLength 
        LinkedList[EntryPointer][1] = LinkedList[currentPointer][1]
        LinkedList[currentPointer][1] = EntryPointer
        OutputList()
        
def remove(data):

    if len(LinkedList) == 0:
        print("Sorry, list is empty.")
        return
    
    global headpointer
    if LinkedList[headpointer][0] == data: #if data exists in head
        headpointer = LinkedList[headpointer][1]
        print("Data {} found at head and deleted.".format(data))
        return

    Temp = headpointer
    Temp2 = headpointer   
    while Temp2 !=- 1:
        if(LinkedList[Temp2][0] == data):
            LinkedList[Temp][1] = LinkedList[Temp2][1] #if element one node after Temp has data, then node after Temp is equal to two nodes after Temp
            print("Data {} found at {} and deleted.".format(data,Temp2))
            if LinkedList[Temp][1] == -1: #for the case when data is deleted at currentPointer, the currentPointer needs to be updated
                global currentPointer
                currentPointer = Temp
            return
        Temp = Temp2 #if above condition not satisfied, then temp starts traversing until above condition satisfied
        Temp2 = LinkedList[Temp2][1]
    print("Data {} does not exist in list".format(data))
    return

def OutputList(): #traverse and print linked list
    currentPointer = headpointer
    if len(LinkedList) == 0:
        print("Sorry, list is empty.")
        return
    while(currentPointer != -1):
        print("CurrentPointer: {} | Data: {} | NextPointer: {}".format(currentPointer,LinkedList[currentPointer][0],str(LinkedList[currentPointer][1])))
        currentPointer = LinkedList[currentPointer][1]

def FindElement(data): #search element in linked list
    currentPointer = headpointer
    while(currentPointer != -1):
        if LinkedList[currentPointer][0] == data:
            print("Search Result: CurrentPointer: {} | Data: {} | NextPointer: {}".format(currentPointer,LinkedList[currentPointer][0],str(LinkedList[currentPointer][1])))
            return
        currentPointer = LinkedList[currentPointer][1]
    print("Data {} does not exist in list".format(data))


LinkedList = []
currentPointer = 0
headpointer = currentPointer
insert(99)
insert(125)
insert(121)
insert(97)
insert(109)
insert(95)
insert(135)
insert(149)
insertAt(10,7)
