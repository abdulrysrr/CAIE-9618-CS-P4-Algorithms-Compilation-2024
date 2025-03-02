class Node:
    def __init__(self):
        self.LeftPointer = -1
        self.Data = None
        self.RightPointer = -1
 
BinaryTree = [Node()]*8
FreePointer = 0
RootNode = 0

def AddData(NewData):
    global FreePointer, RootNode

    NewNode = Node()
    NewNode.Data = NewData
    BinaryTree[FreePointer] = NewNode
    PositionFound = False
    Pointer = RootNode
    print(BinaryTree[Pointer].LeftPointer," ",BinaryTree[Pointer].RightPointer)
    if FreePointer == 0:
        BinaryTree[FreePointer] = NewNode
    else:
        while not PositionFound:
            
            if NewNode.Data < BinaryTree[Pointer].Data:
                if BinaryTree[Pointer].LeftPointer == -1:
                    BinaryTree[Pointer].LeftPointer = FreePointer
                    PositionFound = True
                else:
                    Pointer = BinaryTree[Pointer].LeftPointer
            
            else:
                if BinaryTree[Pointer].RightPointer == -1:
                    BinaryTree[Pointer].RightPointer = FreePointer
                    PositionFound = True
                else:
                    Pointer = BinaryTree[Pointer].RightPointer
    print(Pointer)
    print(BinaryTree[Pointer].LeftPointer," ",BinaryTree[Pointer].RightPointer)
    FreePointer = FreePointer + 1

def InOrder(RootNode):
    if BinaryTree[RootNode].LeftPointer!= -1:
        InOrder(BinaryTree[RootNode].LeftPointer)
    print(str(BinaryTree[RootNode].Data))
    if BinaryTree[RootNode].RightPointer != -1:
        InOrder(BinaryTree[RootNode].RightPointer)

AddData(23)
print()
AddData(5)
print()
AddData(8)
print()
AddData(100)
print()
AddData(9)
print()
AddData(88)
print()
InOrder(0)

Node100 = Node()
Node100.Data = 100