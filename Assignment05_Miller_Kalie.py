# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#  Kalie Miller,2/8/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants

import json

FILE_NAME: str = "Enrollments.json"

# file = open(FILE_NAME, "r")
# students_load = json.load(file)
# file.close()

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
row: dict = {}
table: list = []

row = {"First Name": "Kalie","Last Name":"Miller", "Course Name":"Python 100"}
table.append(row)

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Error! Please check that there are no numbers written in the first name.")
        except ValueError as e:
            print(e)
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Error! Please check that there are no numbers written in the last name.")
        except ValueError as e:
            print(e)
        course_name = input("Please enter the name of the course: ")
                # student_data = ['student_first_name', 'student_last_name', 'course_name']
        row = {"First Name": student_first_name, "Last Name": student_last_name, "Course Name": course_name}
        table.append(row)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        for each_row in table:
            print(each_row)
            print(each_row["First Name"], each_row["Last Name"], each_row["Course Name"])

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
        except FileNotFoundError as e:
            if file.closed == False:
                file.close ()
            print("File must exist before running the file.")
        except Exception as e:
            if file.closed == False:
                file.close()
            print("There was a non-specific error.")
        json.dump(table, file)
        file.close()
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")
print("Program Ended")



