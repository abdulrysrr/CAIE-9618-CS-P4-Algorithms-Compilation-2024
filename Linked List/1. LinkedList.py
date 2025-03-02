# Linked list implementation using an ADT (Node Class) and an Array


class node():
    def __init__(self, data, pointer):
        self.data = data  # Data stored in the node
        self.pointer = pointer  # Pointer to the next node in the linked list

# Display function to print the contents of the linked list
def display():
    global LinkedList
    CurrentPointer = StartPointer
    while CurrentPointer != -1:
        # Print index, data, and pointer of each node
        print(f"Index : {CurrentPointer} | Data : {LinkedList[CurrentPointer].data} | Pointer : {LinkedList[CurrentPointer].pointer}")
        CurrentPointer = LinkedList[CurrentPointer].pointer

# Insert function to insert a new node at the end of the linked list
def insert():
    global LinkedList, FreePointer, StartPointer
    
    data = int(input("Enter data to insert into the linked list: "))

    # If there's a limit on linked list, handle it here
    # if FreePointer == 20:
    #     print("Linked List is full")
    
    if FreePointer == 0:
        LinkedList.append(node(data, -1))  # Append node to the end of the list
    else:
        CurrentPointer = StartPointer
        while CurrentPointer != -1:
            prevPointer = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer].pointer
        LinkedList.append(node(data,-1))  # Append node to the end of the list
        LinkedList[prevPointer].pointer = FreePointer  # Update pointer of the previous node
    FreePointer += 1  # Increment FreePointer    

# InsertAt function to insert a new node at a specific index in the linked list
def insertAt():
    global LinkedList, FreePointer, StartPointer
    
    data = int(input("Enter data to insert into the linked list: "))
    index = int(input("Enter the index you wish to insert data at: "))
    
    # If inserting at the start
    if index == 0:
        EntryPointer = len(LinkedList)
        LinkedList.append(node(data,-1))
        LinkedList[EntryPointer].pointer = StartPointer
        StartPointer = EntryPointer
        FreePointer += 1
        return

    EntryPointer = len(LinkedList)
    LinkedList.append(node(data,-1))
    
    # Traverse to find the node before the specified index
    count = 1
    CurrentPointer = StartPointer
    while CurrentPointer != -1 and count <= index:
        count += 1
        prevPointer = CurrentPointer
        CurrentPointer = LinkedList[CurrentPointer].pointer
   
    LinkedList[prevPointer].pointer = EntryPointer
    LinkedList[EntryPointer].pointer = CurrentPointer    
    FreePointer += 1
    
# Remove function to remove a node with specific data from the linked list
def remove():
    global LinkedList, FreePointer, StartPointer
    
    data = int(input("Enter data you wish to search in the linked list: "))
    if len(LinkedList) == 0:
        print("Linked List is empty")
    else:
        # Traverse to find the node to be removed
        CurrentPointer = StartPointer
        prevPointer = -1
        while CurrentPointer != -1:
            if LinkedList[CurrentPointer].data == data:
                break
            prevPointer = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer].pointer
        
        if prevPointer == -1:  # If the data is in the first node
            StartPointer = LinkedList[CurrentPointer].pointer
        else:
            LinkedList[prevPointer].pointer = LinkedList[CurrentPointer].pointer
        
# Search function to search for a specific data value in the linked list
def search():
    
    data = int(input("Enter data you wish to search in the linked list: "))

    # Traverse to find the specified data value
    CurrentPointer = StartPointer
    found = False
    while CurrentPointer != -1 and found == False:
        if LinkedList[CurrentPointer].data == data:
            found = True
            break
        CurrentPointer = LinkedList[CurrentPointer].pointer

    if found:
        print(f"{data} found at index {CurrentPointer}.")
    else:
        print(f"Not found.")
        
StartPointer = 0
FreePointer = 0        
LinkedList = []

# Menu Driven Program for better understanding

functions = [insert, insertAt, remove, search, display]
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
    if option >= 1 and option <= 6:
        functions[option-1]()  # Call the respective function based on user input
    else:
        break
