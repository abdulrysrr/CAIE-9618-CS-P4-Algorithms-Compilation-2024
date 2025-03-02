def binary_search(Arr, Start, End, Item):
    if Start < End:
        middle = (Start + End) // 2
        if Arr[middle] == Item:
            return middle
        else:
            if Item > Arr[middle]:
                return binary_search(Arr, middle + 1, End, Item)
            else:
                return binary_search(Arr, Start, middle - 1, Item)
    else:
        return -1
    
print(binary_search([1,2,3,4,5,6,7,8,9,10], 0, 9, 5))
    