# Implementation of queue using (OOP)

class CircularQueue:
    def __init__(self, length):
        # Constructor to initialize the circular queue
        self.length = length  # Length of the circular queue
        self.queue = [None] * length  # Initialize the queue with 'None' values
        self.Front = 0  # Front pointer of the queue
        self.Rear = 0  # Rear pointer of the queue
        
    def is_empty(self):
        # Method to check if the queue is empty
        return self.Rear == self.Front
    
    def is_full(self):
        # Method to check if the queue is full
        return (self.Rear + 1) % self.length == self.Front
    
    def enqueue(self, item):
        # Method to add an item to the queue (enqueue operation)
        if self.is_full():  # Check if the queue is full
            return "Queue is full"  # If full, return a message indicating so
        self.queue[self.Rear] = item  # Add the item to the rear of the queue
        self.Rear = (self.Rear + 1) % self.length  # Update the rear pointer, considering circular behavior
        return "Enqueued"  # Return a message indicating successful enqueue operation
    
    def dequeue(self):
        # Method to remove an item from the queue (dequeue operation)
        if self.is_empty():  # Check if the queue is empty
            return "Empty"  # If empty, return a message indicating so
        item = self.queue[self.Front]  # Get the item at the front of the queue
        self.queue[self.Front] = None  # Set the front item to None (removed from queue)
        self.Front = (self.Front + 1) % self.length  # Update the front pointer, considering circular behavior
        return item  # Return the dequeued item
    
    def Print(self):
        # Method to print the elements of the queue
        if self.is_empty():  # Check if the queue is empty
            return "Queue is empty"  # If empty, return a message indicating so
        current_index = self.Front  # Start from the front of the queue
        print("Elements in the queue:")  # Print a message indicating the start of queue elements
        while current_index != self.Rear:  # Loop through queue until reaching the rear
            print(self.queue[current_index])  # Print the element at the current index
            current_index = (current_index + 1) % self.length  # Move to the next index, considering circular behavior

# Create a CircularQueue object with a length of 6
queue = CircularQueue(6)

# Menu-driven program loop
while True:
    print("\n---- Circular Queue Operations ----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Print Queue")
    print("4. Exit")
    choice = input("Enter your choice: ")  # Get user choice
    if choice == '1':
        item = input("Enter element to enqueue: ")  # Get item from user
        print(queue.enqueue(item))  # Call enqueue method and print result
    elif choice == '2':
        print("Element dequeued: ", queue.dequeue())  # Call dequeue method and print result
    elif choice == '3':
        print(queue.Print())  # Call Print method to display queue elements
    elif choice == '4':
        print("Exiting...")  # Exit the program
        break
    else:
        print("Invalid choice! Please enter a valid option.")  # Display error message for invalid input
