import pickle

# Function to read data from TextFile.txt and create a .dat file
def ReadAndCopy():
    try:
        # Open the text file for reading
        with open('TextFile.txt', 'r') as f:
            # Open the .dat file for writing binary data
            with open('NewFile.dat', 'wb') as j:
                # Loop through each line in the text file
                while True:
                    # Read a line from the text file and remove leading/trailing whitespaces
                    line = f.readline().strip()
                    # If the line is empty, exit the loop
                    if line == '':
                        break
                    
                    # Split the line into a list using comma and space as delimiter
                    line = line.split(', ')
                    # Extract data from the line
                    Name = line[0]  # Student Name (string)
                    Class = line[1]  # Class (string)
                    Age = int(line[2])  # Age (integer)
                    Percentage = eval(line[3])  # Percentage (real)
                    
                    # Serialize and save the data to the .dat file
                    pickle.dump([Name, Class, Age, Percentage], j)

    except FileNotFoundError:
        print("TextFile.txt not found.")

# Function to read data from the .dat file and print it
def ReadRandomFile():
    try:
        # Load data from the .dat file
        with open("NewFile.dat", "rb") as f:
            # Loop to read and print each data item until the end of file (EOF)
            while True:
                try:
                    # Load and print the data
                    loaded_data = pickle.load(f)
                    print(loaded_data)
                # Handle EOFError (end of file reached)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found")

# Call the function to read data from TextFile.txt and create a .dat file
ReadAndCopy()

# Call the function to read and print data from the .dat file
ReadRandomFile()
