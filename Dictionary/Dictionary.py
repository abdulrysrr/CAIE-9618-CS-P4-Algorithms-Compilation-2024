class MyDictionary:
    def __init__(self):
        self.dictionary = {}
    
    def insert(self, key, value):
        if key in self.dictionary:
            print("Key already exists. Updating value.")
        self.dictionary[key] = value
        print("Inserted successfully.")
    
    def delete(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            print("Deleted successfully.")
        else:
            print("Key not found.")
    
    def search(self, key):
        if key in self.dictionary:
            print(f"Key: {key}, Value: {self.dictionary[key]}")
        else:
            print("Key not found.")
    
    def display(self):
        if self.dictionary:
            print("Dictionary contents:")
            for key, value in self.dictionary.items():
                print(f"Key: {key}, Value: {value}")
        else:
            print("Dictionary is empty.")

# Creating a MyDictionary object
my_dict = MyDictionary()

# Inserting key-value pairs
my_dict.insert("apple", 10)
my_dict.insert("banana", 5)
my_dict.insert("orange", 8)

# Displaying the dictionary
my_dict.display()

# Searching for a key
my_dict.search("banana")
my_dict.search("grape")

# Deleting a key
my_dict.delete("apple")

# Displaying the dictionary after deletion
my_dict.display()
