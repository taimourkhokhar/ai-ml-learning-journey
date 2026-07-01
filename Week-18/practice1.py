import sys
import os

#simple student management system

class StudentManagement:
    def __init__(self, filename="student.txt"):
        self.filename = filename
        # Create the file automatically if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass

    def add_student(self):
        student_name = input("Enter the name of the student: ").strip()
        if student_name:
            # "a" mode appends to the file instead of overwriting it
            with open(self.filename, "a") as file:
                file.write(student_name + "\n")
            print(f"'{student_name}' added successfully!")
        else:
            print("Name cannot be empty.")

    def view_students(self):
        print("\n--- Student List ---")
        with open(self.filename, "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("No students found.")
        else:
            for index, line in enumerate(lines, 1):
                # .strip() removes the invisible '\n' at the end of each line
                print(f"{index}. {line.strip()}")
        print("--------------------")

    def search_student(self):
        user_query = input("Enter student name you want to search: ").strip()
        found = False
        
        with open(self.filename, "r") as file:
            for line in file:
                if line.strip().lower() == user_query.lower():
                    found = True
                    break
                    
        if found:
            print(f"Yes, student '{user_query}' exists.")
        else:
            print(f"Student '{user_query}' does not exist.")

    def delete_student(self):
        user_query = input("Enter student name you want to delete: ").strip()
        
        # Read all current students
        with open(self.filename, "r") as file:
            lines = file.readlines()
            
        # Filter out the student to be deleted
        updated_lines = []
        found = False
        for line in lines:
            if line.strip().lower() == user_query.lower():
                found = True  # Found the student, skip adding them back
            else:
                updated_lines.append(line)
                
        if found:
            # Overwrite the file with the remaining students
            with open(self.filename, "w") as file:
                file.writelines(updated_lines)
            print(f"'{user_query}' has been deleted successfully.")
        else:
            print(f"Student '{user_query}' not found.")

# Create the object instance
sm = StudentManagement()

while True:
    print("\n=== Student Management System ===")
    print("1. Add student")
    print("2. View students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    try:
        choice = int(input("Enter an operation number: "))
        if choice == 1:
            sm.add_student()
        elif choice == 2:
            sm.view_students()
        elif choice == 3:
            sm.search_student()
        elif choice == 4:
            sm.delete_student()
        elif choice == 5:
            print("Exiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid input. Please choose a number from 1 to 5.")
    except ValueError:
        print("Error: Please enter a valid integer number.")