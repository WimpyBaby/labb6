"Code that allows user to register students and view registered students"
import os


def get_letters_input(text):
    """Function that takes a string as input and returns it if it only contains letters"""
    while True:
        try:
            user_input = input(text)
            # if user_input.isalpha() hämtat från stackoverflow där isalpha() används för att kolla om en sträng endast innehåller bokstäver
            if user_input.isalpha():
                return user_input
            else:
                print("\nInvalid input! Please enter only letters.")
        except ValueError:
            print("\nInvalid input! Please enter only letters.")


def get_number_input(text):
    """Function that takes a string as input and returns it if it only contains numbers"""
    while True:
        try:
            user_input = input(text)
            # if user_input.isdigit() hämtat från stackoverflow där isdigit() används för att kolla om en sträng endast innehåller siffror
            if user_input.isdigit():
                return user_input
            else:
                print("\nInvalid input! Please enter only numbers.")
        except ValueError:
            print("\nInvalid input! Please enter only numbers.")


class Student:
    """Class that represents a student"""

    def __init__(self, name, lastname, personalnumber):
        # Initialize the attributes name, lastname and personalnumber
        self.name = name
        self.lastname = lastname
        self.personalnumber = personalnumber

    def __str__(self):
        # Return a string representation of the student
        return f"{self.name} {self.lastname} {self.personalnumber}"


class School:
    def __init__(self):
        # Initialize the attribute students
        self.students = []

    def add_student(self, student):
        # Add a student to the list of students
        self.students.append(student)

    def view_students(self):
        # Print all students in the list of students if there are any
        if not self.students:
            print("\nNo students registered in this school.")
        else:
            print(f"\nRegistered students:")
            # Loop through the list of students and print each student
            for student in self.students:
                print(
                    f"Name: {student.name} {student.lastname} Personal Number: {student.personalnumber}"
                )


# Create an instance of the School class
registered_school = School()


def read_student_data(file_path):
    """Function that reads student data from a text file and returns a list of Student objects"""
    students = []

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for i in range(0, len(lines), 3):
            personalnumber = lines[i].strip()
            lastname = lines[i + 1].strip()
            firstname = lines[i + 2].strip()

            student = Student(firstname, lastname, personalnumber)
            students.append(student)

    return students


def write_student_data(file_path, students):
    """Function that writes student data to a text file"""
    with open(file_path, "w", encoding="utf-8") as file:
        for student in students:
            file.write(student.personalnumber + "\n")
            file.write(student.lastname + "\n")
            file.write(student.name + "\n")


# Create an instance of the School class
registered_school = School()

# Prompt the user for a valid file path
while True:
    file_path = input("Enter the path to the text file: ")

    if os.path.exists(file_path):
        break
    else:
        print("Invalid file path. Please enter a valid path.")

# Read student data from the provided text file
students_from_file = read_student_data(file_path)
registered_school.students.extend(students_from_file)

while True:
    # Print the menu
    print("\nOptions: \n")
    print("1. Register student")
    print("2. View registered students")
    print("3. Exit")

    # Get the user's choice
    choice = input("\nEnter your choice: ")

    if choice == "1":
        # Get the student's name, lastname and personalnumber if chosen to register a student
        name = get_letters_input("Enter student's first name: ")
        lastname = get_letters_input("Enter student's last name: ")
        personalnumber = get_number_input("Enter student's personal number: ")
        # Create an instance of the Student class
        student = Student(name, lastname, personalnumber)
        registered_school.add_student(student)
        print("\nStudent registered!\n")

        # Write the student data to the provided text file (append)
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n" + personalnumber + "\n")
            file.write(lastname + "\n")
            file.write(name)

    elif choice == "2":
        # function viewstudent som skriver ut alla studenter från listan students i klassen School
        registered_school.view_students()

    elif choice == "3":
        break
    else:
        print("Invalid choice")
