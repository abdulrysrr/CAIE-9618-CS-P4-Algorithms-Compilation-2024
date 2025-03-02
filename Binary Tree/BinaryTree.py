# Insert Function
def insert(data):
    global FreeNode
    
    # If the tree is empty
    if FreeNode == 0:
        Array.append([-1,data,-1])  # Initialize the tree with the root node
    else:
        Array.append([-1,data,-1])  # Add a new node to the tree
        # Traversing to find the correct position for the new node
        Placed = False  # Boolean flag to indicate if the node has been placed
        CurrentNode = 0  # Integer to keep track of the current node being visited
        while not Placed:
            if data < Array[CurrentNode][1]:
                # Go left
                if Array[CurrentNode][0] == -1:  # If left child is empty
                    Array[CurrentNode][0] = FreeNode  # Set left child to new node
                    Placed = True  # Node has been placed
                else:
                    CurrentNode = Array[CurrentNode][0]  # Move to the left child
            else:
                # Go right
                if Array[CurrentNode][2] == -1:  # If right child is empty
                    Array[CurrentNode][2] = FreeNode  # Set right child to new node
                    Placed = True  # Node has been placed
                else:
                    CurrentNode = Array[CurrentNode][2]  # Move to the right child
    FreeNode += 1  # Increment the FreeNode pointer

# Search Function
def Search(Root, Value):
    global Array
    
    if Array[Root][1] == Value:  # If the value is found at the root node
        print("Found")
        print(f"Current Pointer : {Root}, Left Pointer : {Array[Root][0]}, Data: {Array[Root][1]}, Right Pointer : {Array[Root][2]}")
    elif Value < Array[Root][1] and Array[Root][0] != -1:  # If value is less than the root value and there is a left child
        Search(Array[Root][0], Value)  # Recursively search in the left subtree
    elif Value > Array[Root][1] and Array[Root][2] != -1:  # If value is greater than the root value and there is a right child
        Search(Array[Root][2], Value)  # Recursively search in the right subtree
    else:
        print("Not found")  # Value not found
        

# In Order Traversal Function - LNR
def InOrder(RootNode):
    # Visit left subtree recursively
    if Array[RootNode][0] != -1:
        InOrder(Array[RootNode][0])
    
    # Visit current node
    print(f"Current Pointer : {RootNode}, Left Pointer : {Array[RootNode][0]}, Data: {Array[RootNode][1]}, Right Pointer : {Array[RootNode][2]}")
    
    # Visit right subtree recursively
    if Array[RootNode][2] != -1:
        InOrder(Array[RootNode][2])

# Pre Order Traversal Function - NLR
def PreOrder(RootNode):
    # Visit current node
    print(f"Current Pointer : {RootNode}, Left Pointer : {Array[RootNode][0]}, Data: {Array[RootNode][1]}, Right Pointer : {Array[RootNode][2]}")
    
    # Visit left subtree recursively
    if Array[RootNode][0] != -1:
        PreOrder(Array[RootNode][0])
    
    # Visit right subtree recursively
    if Array[RootNode][2] != -1:
        PreOrder(Array[RootNode][2])

# Post Order Traversal Function - LRN
def PostOrder(RootNode):
    # Visit left subtree recursively
    if Array[RootNode][0] != -1:
        PostOrder(Array[RootNode][0])
    
    # Visit right subtree recursively
    if Array[RootNode][2] != -1:
        PostOrder(Array[RootNode][2])
    
    # Visit current node
    print(f"Current Pointer : {RootNode}, Left Pointer : {Array[RootNode][0]}, Data: {Array[RootNode][1]}, Right Pointer : {Array[RootNode][2]}")
    
        
# Main Program
Array = []  # 2D array for binary tree 
RootNode = 0  # Integer to store the root node index
FreeNode = 0  # Integer to track the next free node index


# Main menu loop
while True:
    # Display menu options
    print("\nMenu:")
    print("1. Insert")
    print("2. Search")
    print("3. In Order Traversal")
    print("4. Pre Order Traversal")
    print("5. Post Order Traversal")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))  # Get user input
    
    # Execute the chosen option
    if choice == 1:
        data = int(input("Enter data to insert: "))
        insert(data)  # Call insert function
    elif choice == 2:
        value = int(input("Enter value to search: "))
        Search(RootNode, value)  # Call search function
    elif choice == 3:
        print("In Order Traversal:")
        InOrder(RootNode)  # Call in order traversal function
    elif choice == 4:
        print("Pre Order Traversal:")
        PreOrder(RootNode)  # Call pre order traversal function
    elif choice == 5:
        print("Post Order Traversal:")
        PostOrder(RootNode)  # Call post order traversal function
    elif choice == 6:
        print("Exiting program.")
        break  # Exit the program
    else:
        print("Invalid choice. Please try again.")  # Display error message for invalid input
