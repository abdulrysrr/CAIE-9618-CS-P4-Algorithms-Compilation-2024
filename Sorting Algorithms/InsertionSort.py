def InsertionSort(Array):
    j = 1  # Start from the second element (index 1)
    while j < len(Array):  # Iterate over the array starting from the second element
        k = j  # Initialize k to the current index j
        while Array[k] < Array[k - 1] and k > 0:  # Iterate backwards from k to 0 and swap elements if necessary
            Array[k], Array[k - 1] = Array[k - 1], Array[k]  # Swap the current element with its predecessor
            k = k - 1  # Move to the previous element
        j += 1  # Move to the next element in the array
    return Array  # Return the sorted array

Array = [10, 8, 9, 1, 4, 7, 66, 31, 4, 85, 0]  # Define an example array

# Print the sorted array using InsertionSort function
print(InsertionSort(Array))
