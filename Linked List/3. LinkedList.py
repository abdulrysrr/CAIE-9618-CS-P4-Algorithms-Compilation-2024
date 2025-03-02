# Linked list implementation using a class for LinkedList 


class LinkedList:
    def __init__(self):
        self._LinkedList = []  # 2D array to store the linked list
        self._StartPointer = 0  # Pointer to the first node
        self._FreePointer = 0  # Pointer to the next available index in the array

    # Display function to print the contents of the linked list
    def display(self):
        current_pointer = self._StartPointer
        while current_pointer != -1:
            # Print index, data, and pointer of each node
            print(f"Index : {current_pointer} | Data : {self._LinkedList[current_pointer][0]} | Pointer : {self._LinkedList[current_pointer][1]}")
            current_pointer = self._LinkedList[current_pointer][1]

    # Insert function to insert a new node at the end of the linked list
    def insert(self):
        data = int(input("Enter data to insert into the linked list: "))

        if self._FreePointer == 0:
            self._LinkedList.append([data, -1])  # Append node to the end of the list
        else:
            current_pointer = self._StartPointer
            while current_pointer != -1:
                prev_pointer = current_pointer
                current_pointer = self._LinkedList[current_pointer][1]
            self._LinkedList.append([data, -1])  # Append node to the end of the list
            self._LinkedList[prev_pointer][1] = self._FreePointer  # Update pointer of the previous node
        self._FreePointer += 1  # Increment FreePointer    

    # InsertAt function to insert a new node at a specific index in the linked list
    def insertAt(self):
        data = int(input("Enter data to insert into the linked list: "))
        index = int(input("Enter the index you wish to insert data at: "))
        
        if index == 0:  # If inserting at the start
            entry_pointer = len(self._LinkedList)
            self._LinkedList.append([data, self._StartPointer])
            self._StartPointer = entry_pointer
            self._FreePointer += 1
            return

        entry_pointer = len(self._LinkedList)
        self._LinkedList.append([data, -1])
        
        # Traverse to find the node before the specified index
        count = 1
        current_pointer = self._StartPointer
        while current_pointer != -1 and count <= index:
            count += 1
            prev_pointer = current_pointer
            current_pointer = self._LinkedList[current_pointer][1]
       
        self._LinkedList[prev_pointer][1] = entry_pointer
        self._LinkedList[entry_pointer][1] = current_pointer
        self._FreePointer += 1
    
    # Remove function to remove a node with specific data from the linked list
    def remove(self):
        data = int(input("Enter data you wish to search in the linked list: "))
        if len(self._LinkedList) == 0:
            print("Linked List is empty")
        else:
            current_pointer = self._StartPointer
            prev_pointer = -1
            while current_pointer != -1:
                if self._LinkedList[current_pointer][0] == data:
                    break
                prev_pointer = current_pointer
                current_pointer = self._LinkedList[current_pointer][1]
            
            if prev_pointer == -1:
                self._StartPointer = self._LinkedList[current_pointer][1]
            else:
                self._LinkedList[prev_pointer][1] = self._LinkedList[current_pointer][1]
    
    # Search function to search for a specific data value in the linked list
    def search(self):
        data = int(input("Enter data you wish to search in the linked list: "))
        current_pointer = self._StartPointer
        found = False
        while current_pointer != -1 and not found:
            if self._LinkedList[current_pointer][0] == data:
                found = True
                break
            current_pointer = self._LinkedList[current_pointer][1]

        if found:
            print(f"{data} found at index {current_pointer}.")
        else:
            print("Not found.")
        
    
    def LinkedList(self):
        return self._LinkedList
    
    
    def FreePointer(self):
        return self._FreePointer
    
    def StartPointer(self):
        return self._StartPointer

# Menu Driven Program for better understanding
linked_list = LinkedList()
functions = [linked_list.insert, linked_list.insertAt, linked_list.remove, linked_list.search, linked_list.display]
while True:
    print("""
Choose from the following options: 
1. Insert a new item in the linked list
2. Insert a new item at a specific index in the linked list
3. Remove an item from linked list
4. Search an item in the linked list
5. Display the linked list

Type any other key to exit.
        
    """)
    option = int(input("Enter option: "))
    if option >= 1 and option <= 5:
        functions[option-1]()  # Call the respective method based on user input
    else:
        break
