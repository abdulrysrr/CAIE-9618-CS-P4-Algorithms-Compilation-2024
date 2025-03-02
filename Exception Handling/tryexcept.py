
# Example 1: Handling File Not Found Error
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")


# Example 2: Handling ZeroDivisionError
try:
    
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Example 3: Handling ValueError
try:
   
    number = int("abc")
    print("Number:", number)
except ValueError:
    print("Invalid input. Could not convert to integer.")


# Example 4: Handling KeyError
try:
    
    my_dict = {"name": "John", "age": 30}
    print(my_dict["address"])
except KeyError:
    print("Key does not exist in the dictionary.")


# Example 5: Handling Multiple Exceptions
try:
    
    result = 10 / 0
    number = int("abc")
    my_dict = {"name": "John", "age": 30}
    print(my_dict["address"])
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Could not convert to integer.")
except KeyError:
    print("Key does not exist in the dictionary.")


# Example 6: Raising an Exception
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


# Example 7: Handling IOError while writing to a file
def write_to_file(filename, content):
    try:
        # Attempt to open the file for writing
        with open(filename, 'w') as file:
            # Write the content to the file
            file.write(content)
        print("Content successfully written to", filename)
    except IOError as e:
        # If an IOError occurs, print an error message
        print(f"Error writing to file '{filename}': {e}")
        
        
# Example 8 : EOF Error
with open("non-existent.dat", "rb") as f:
    # Loop to read and print each data item until the end of file (EOF)
    while True:
        try:
            # Load and print the data
            # loaded_data = pickle.load(f)
            print("loaded_data")
        # Handle EOFError (end of file reached)
        except EOFError:
            break