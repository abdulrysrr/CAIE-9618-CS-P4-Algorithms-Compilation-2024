# Implementation of queue using a 1d array

# Enqueue Function: Adds data to the queue
def enqueue(data):
    global Queue, FrontPointer, RearPointer
    # Check whether the queue is full
    if (RearPointer + 1) % Length == FrontPointer:
        print('Queue is full.')
    else:
        Queue[RearPointer] = data
        RearPointer = (RearPointer + 1) % Length
        print(f"{data} added to queue.")

# Dequeue Function: Removes data from the queue
def dequeue():
    global Queue, FrontPointer, RearPointer
    
    # Check whether the queue is empty
    if FrontPointer == RearPointer:
        print('Queue is empty.')
    else:
        print(f"{Queue[FrontPointer]} removed from queue.")
        Queue[FrontPointer] = None
        FrontPointer = (FrontPointer + 1) % Length

# Display Function: Displays the contents of the queue
def display():
    global Queue, FrontPointer, RearPointer

    # Iterate through the queue and print its contents
    count = FrontPointer
    while count != RearPointer:
        print(f'{Queue[count]}')
        count = (count + 1) % Length

# Main Program
Length = 5 + 1 # Length of the queue (if we need 5 items initialise to 6)
Queue = [None] * Length  # Queue initialized to a length
FrontPointer = 0  # Front pointer of the queue
RearPointer = 0  # Rear pointer of the queue



# Menu-driven program loop
while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))  # Get user input
    
    # Execute the chosen option
    if choice == 1:
        data = input("Enter data to enqueue: ")
        enqueue(data)  # Call enqueue function
    elif choice == 2:
        dequeue()  # Call dequeue function
    elif choice == 3:
        print(Queue)
        print("Queue contents:")
        display()  # Call display function
    elif choice == 4:
        print("Exiting program.")
        break  # Exit the program
    else:
        print("Invalid choice. Please try again.")  # Display error message for invalid input
