def LinearSearch(Value):
    global Array  # Access the global variable Array
    
    Index = 0  # Initialize Index to 0
    Found = False  # Initialize Found flag to False
    while Found == False and Index < len(Array):  # Loop until Found is True or Index exceeds the length of Array
        if Array[Index] == Value:  # If the current element of Array matches the search Value
            Found = True  # Set Found flag to True
            break  # Exit the loop since the value is found
        Index += 1  # Move to the next index
    return Found, Index  # Return the Found flag and the index where the value was found or the end of the array


Array = [10,8,9,1,4,7,66,31,4,85,0]  # Define an example array
print(f"Array : {Array}")

while True:  # Start an infinite loop
    searchValue = int(input("Enter a value to search for (-1 to exit): "))  # Prompt user for input
    if searchValue == -1:  # If user enters -1, exit the loop
        print("Bye!")
        break
    else:
        Found, Index = LinearSearch(searchValue)  # Call LinearSearch function to search for the entered value
        if Found == True:
            print(f"Value {searchValue} found at index {Index}")  # If the value is found, print its index
        else:
            print("Value not found.")  # If the value is not found, print a message
