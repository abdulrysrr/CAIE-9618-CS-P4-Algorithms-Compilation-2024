# Bubble sort implementation with optimizations

def BubbleSort(array):
    sorted = True
    top = len(array) - 1
    while sorted == True and top > 0:
        sorted = False
        for index in range(0, top):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                sorted = True
        top = top - 1
    return array


# Shorter version of bubble sort
def BubbleSort_Short(Array):
    for x in range(0, len(Array)-1):  # Iterate over the array
        for y in range(0, len(Array)-1):  # Iterate over each element in the array
            if Array[y] > Array[y+1]:  # If the current element is greater than the next element
                Array[y], Array[y+1] = Array[y+1], Array[y]  # Swap the elements
    return Array  # Return the sorted array

Array = [10,8,9,1,4,7,66,31,4,85,0]  # Define an example array
            
# Print the sorted arrays using both BubbleSort and BubbleSort_Short functions

print(BubbleSort(Array))
