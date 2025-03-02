QueueArray = ['','','','','','','','','',''] #string
QueueHeadPointer = 0 #integer
QueueTailPointer = 0 #integer
NumberOfItems = 0 #integer

def Enqueue(Queue, Head, Tail, NumItems, InputData):
    if NumItems >= 10:
        return (False, Queue, Head, Tail, NumItems)
    Queue[Tail] = InputData
    if Tail >= 9:
        Tail = 0
    else:
        Tail = Tail + 1
    NumItems = NumItems + 1
    return (True, Queue, Head, Tail, NumItems)

def Dequeue(Queue, Head, Tail, NumItems):
    if NumItems == 0:
        return (False, Queue, Head, Tail, NumItems)
    else:
        ReturnValue = Queue[Head]
        Head = Head + 1
        if Head >= 9:
            Head = 0
        NumItems = NumItems - 1
        return(ReturnValue, Queue, Head, Tail, NumItems)

for x in range(0, 11):
    InputString = input("Enter a string: ")
    ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Enqueue(QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems, InputString)
    if ReturnValue == True:
        print("Successful")
    else:
        print("Unsuccessful")
ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Dequeue(QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems)
print(ReturnValue)
ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Dequeue(QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems)
print(ReturnValue)