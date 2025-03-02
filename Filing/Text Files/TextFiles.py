# Function to read data from ReadingFile.txt and store it in an array
def ReadFile():
    try:
        # Open the text file for reading
        with open('ReadingFile.txt', 'r') as f:
            # Loop to read each line in the file
            while True:
                # Read a line from the file and remove leading/trailing whitespaces
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

                # Append the extracted data to the StudentData array
                StudentData.append([Name, Class, Age, Percentage])
                                
    except FileNotFoundError:
        print("ReadingFile.txt not found.")

# Function to write data from StudentData to a new file with updated grades
def WriteFile():
    # Open the new file for writing
    with open("NewFile.txt", 'w') as f:
        # Loop through each student's data in StudentData
        for x in range(len(StudentData)):
            # Extract percentage from the student's data
            Percentage = StudentData[x][3]  # Real
            Grade = 'U'  # Initialize grade as 'U'
            # Determine the grade based on the percentage
            if Percentage >= 90:
                Grade = 'A*'
            elif Percentage >= 80:
                Grade = 'A'
            elif Percentage >= 70:
                Grade = 'B'
            elif Percentage >= 60:
                Grade = 'C'
            elif Percentage >= 50:
                Grade = 'D'
            
            # Append the grade to the student's data
            StudentData[x].append(Grade)
            
            try:
                # Write the student's data (including the grade) to the file
                f.write(f"{StudentData[x][0]}, {StudentData[x][1]}, {StudentData[x][2]}, {StudentData[x][3]}, {StudentData[x][4]}\n")
            except IOError:
                print("Error occurred while writing")
                return
            
    print("All Student Data with new grades stored in new file.")    

# Function to append extra data to NewFile.txt
def AppendData():
    # Open the new file for appending
    with open("NewFile.txt", 'a') as f:
        # Get input from user for new student data
        Name = input("Enter student name : ")  # String
        Class = input("Enter student's class : ")  # String
        Age = int(input("Enter student's age : "))  # Integer
        Percentage = eval(input("Enter student's percentage'"))  # Real
        
        # Determine grade for the new student based on percentage
        Grade = 'U'  # Initialize grade as 'U'
        if Percentage >= 90:
            Grade = 'A*'
        elif Percentage >= 80:
            Grade = 'A'
        elif Percentage >= 70:
            Grade = 'B'
        elif Percentage >= 60:
            Grade = 'C'
        elif Percentage >= 50:
            Grade = 'D'
        
        try:
            # Write the new student's data (including the grade) to the file
            f.write(f"{Name}, {Class}, {Age}, {Percentage}, {Grade}\n")
        except IOError:
            print("Error occurred while writing")
            return
        
    print("New student data with new grades appended to new file.")    

# 2D array to store all the student data
StudentData = []

# Call the functions to read, write, and append data
ReadFile()
WriteFile()
AppendData()
