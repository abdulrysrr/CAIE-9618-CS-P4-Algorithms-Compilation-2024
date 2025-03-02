# Iterative binary search
def BinarySearch(Value):
    global Array
    
    # Set initial upper and lower bounds
    upperbound = len(Array)
    lowerbound = 0
    found = False
    
    mid = 0  # Initialize mid variable
    while upperbound >= lowerbound and found == False:  # Loop until upperbound is greater than or equal to lowerbound and the value is not found
        mid = (upperbound + lowerbound) // 2  # Calculate the middle index
        
        if Array[mid] == Value:  # If the middle element is equal to the search value
            found = True  # Set found to True
            break  # Exit the loop
        elif Array[mid] < Value:  # If the middle element is less than the search value
            lowerbound = mid + 1  # Update lowerbound to mid + 1
        else:  # If the middle element is greater than the search value
            upperbound = mid - 1  # Update upperbound to mid - 1
    
    return found, mid  # Return whether the value is found and the index where it was found

# Recursive binary search
def BinarySearch_Recursive(Value, upperbound, lowerbound):
    global Array
    
    mid = (upperbound + lowerbound) // 2  # Calculate the middle index

    if Array[mid] == Value:  # If the middle element is equal to the search value
        return True, mid  # Return True and the index where it was found
    elif Array[mid] < Value:  # If the middle element is less than the search value
        return BinarySearch_Recursive(Value, upperbound, mid + 1)  # Recur on the right half of the array
    elif Array[mid] > Value:  # If the middle element is greater than the search value
        return BinarySearch_Recursive(Value, mid - 1, lowerbound)  # Recur on the left half of the array
    else:  # If the value is not found
        return False, mid  # Return False and the last checked index


    
    
Array = [0, 1, 4, 4, 7, 8, 9, 10, 31, 66] # Define an example array
print(f"Array : {Array}")

while True:  # Start an infinite loop
    searchValue = int(input("Enter a value to search for (-1 to exit): "))  # Prompt user for input
    if searchValue == -1:  # If user enters -1, exit the loop
        print("Bye!")
        break
    else:
        Found, Index = BinarySearch_Recursive(searchValue)  # Call LinearSearch function to search for the entered value
        if Found == True:
            print(f"Value {searchValue} found at index {Index}")  # If the value is found, print its index
        else:
            print("Value not found.")  # If the value is not found, print a message