ArrayNodes=[[0 for X in range(3)] for Y in range(20)]
RootPointer = -1
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the Data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1: # Add to start
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode


def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print("CurrentPointer: {} | LeftPointer: {} | Data: {} | RightPointer: {}".format(RootNode,ArrayNodes[RootNode][0],ArrayNodes[RootNode][1],ArrayNodes[RootNode][2]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])
        
def PrintAll(ArrayNodes):
    for X in range(0, 20):
        print(str(ArrayNodes[X][0]), " ", str(ArrayNodes[X][1])," ", str(ArrayNodes[X][2]))

for X in range(0,12):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes,RootPointer,FreeNode)
#PrintAll(ArrayNodes)
InOrder(ArrayNodes,0)
