# Implementation of Stack using class (OOP)


class Stack:
    def __init__(self, length):
        self.length = length #integer
        self.stack = [None] * length #1d array of datatype integer
        self.top_pointer = 0 #integer
    
    def is_empty(self):
        return self.top_pointer == 0
    
    def is_full(self):
        return self.top_pointer == self.length
    
    def push(self, item):
        if self.is_full():
            print("Stack is full.")
        else:
            self.stack[self.top_pointer] = item
            self.top_pointer += 1
            print(f"{item} pushed into stack")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            self.top_pointer -= 1
            print(f"{self.stack[self.top_pointer]} popped from stack.")
            self.stack[self.top_pointer] = None
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents:")
            for index in range(self.top_pointer):
                print(f"Data : {self.stack[index]}")

# Menu-driven program loop
def menu():
    while True:
        print("\n---- Stack Operations ----")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")  # Get user choice
        if choice == '1':
            Item = input("Enter item to push: ")  # Get item from user
            stack.push(Item)  # Call push method to push item onto stack
        elif choice == '2':
            stack.pop()  # Call pop method to pop item from stack
        elif choice == '3':
            stack.display()  # Call display method to show stack contents
        elif choice == '4':
            print("Exiting...")  # Exit the program
            break
        else:
            print("Invalid choice! Please enter a valid option.")  # Display error message for invalid input

# Create a Stack object with a length of 5
stack = Stack(5)
menu()  # Call the menu function to start the program
