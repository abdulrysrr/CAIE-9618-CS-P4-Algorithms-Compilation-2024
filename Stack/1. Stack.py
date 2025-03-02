# Implementation of Stack using 1D Array

# Push Function: Adds an item to the stack
def Push(Item):
    global Stack, TopPointer
    
    # Check if the stack is full
    if TopPointer == Length:
        print("Stack is full.")
    else:
        # Add item to the stack
        Stack[TopPointer] = Item
        TopPointer += 1
        print(f"{Item} pushed into stack")

# Pop Function: Removes an item from the stack
def Pop():
    global Stack, TopPointer
    
    # Check if the stack is empty
    if TopPointer == 0:
        print("Stack is empty.")
    else:
        # Remove item from the stack
        print(f"{Stack[TopPointer-1]} popped from stack.")
        Stack[TopPointer-1] = None
        TopPointer -= 1

# Display Function: Displays the contents of the stack
def display():
    if TopPointer == 0:
        print("Stack is empty.")
    else:
        # Print stack contents
        for index in range(TopPointer):
            print(f"Data : {Stack[index]}")
        

Length = 5  # Length of the stack
Stack = [None] * Length  # 1D array for stack
TopPointer = 0  # Pointer to top of the stack

# Menu-driven program loop
while True:
    print("\n---- Stack Operations ----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice: ")  # Get user choice
    if choice == '1':
        Item = input("Enter item to push: ")  # Get item from user
        Push(Item)  # Call Push function to push item onto stack
    elif choice == '2':
        Pop()  # Call Pop function to pop item from stack
    elif choice == '3':
        display()  # Call display function to show stack contents
    elif choice == '4':
        print("Exiting...")  # Exit the program
        break
    else:
        print("Invalid choice! Please enter a valid option.")  # Display error message for invalid input
