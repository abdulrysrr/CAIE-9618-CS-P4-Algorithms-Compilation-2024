MyList = [3,5,8,9,13,16,27,0,0,0]

def delete(Index, Item):
    if MyList[Index] > 0:
        if MyList[Index] >= Item:
            MyList[Index] = MyList[Index + 1]
        delete(Index + 1, Item)
   


def delete_item(Index, Item):
    while MyList[Index] > 0:
        if MyList[Index] >= Item:
            MyList[Index] = MyList[Index + 1]
        Index += 1
        
        
delete_item(0, 9)
print(MyList)         
    