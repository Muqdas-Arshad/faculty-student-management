from Controller import Controller

class View:

    def __init__(self):
        self.controller = Controller()

    def display_menu(self):
        print("Welcome to the Student Management System!")
        while True:
            print("\nPlease select an option:")
            print("1. Register a faculty member")
            print("2. Register a student")
            print("3. Authenticate a faculty member")
            print("4. Authenticate a student")
            print("5. Update a faculty member")
            print("6. Update a student")
            print("7. Delete a faculty member")
            print("8. Delete a student")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                try:
                    username = input("Enter username: ")
                    password = input('Enter password: ')
                    designation = input("Enter designation: ")
                    subject = input("Enter subject: ")
                    result = self.controller.register_faculty(username, password, designation, subject)
                    print(result)
                    return result
                except ValueError:
                    print("Invalid user ID. Please enter a valid integer.")
                except Exception as e:
                    print("An error occurred:", e)



            elif choice == "2":

                try:
                    print("Enter student details: ")
                    username = input("Enter username: ")
                    password = input('Enter password: ')
                    smester = int(input("Enter semester: "))
                    if smester < 1 or smester > 8:
                        raise ValueError(
                            "Invalid input. Please enter a valid number  for semester (>= 1) and less than 8")
                    cgpa = float(input("Enter CGPA: "))
                    if cgpa < 0 or cgpa > 4:
                        raise ValueError(
                            "Invalid input. Please enter a valid float for CGPA (between 0 and 4).")

                    major = input("Enter major: ")
                    result = self.controller.register_student(username, password, smester, cgpa, major)
                    print(result)
                    return result
                except ValueError:
                    print("Invalid input, please enter a valid number or float for semester and CGPA.")
                except Exception as e:
                    print("An error occurred:", e)


            elif choice == "3":
                try:
                    username = input("Enter faculty member username: ")
                    password = input("Enter faculty member password: ")
                    result = self.controller.get_faculty(username, password)
                    print(result)
                except ValueError:
                    print("Invalid input. Please try again.")
                except Exception as e:
                    print("An error occurred:", e)


            elif choice == "4":
                try:
                    username = input("Enter student username: ")
                    password = input("Enter student password: ")
                    result = self.controller.get_student(username, password)
                    print(result)
                except ValueError:
                    print("Invalid input. Please try again.")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")

            elif choice == "5":
                try:
                    faculty_id = int(input("Enter faculty ID: "))
                    faculty_username = input("Enter new username (or leave blank to skip): ")
                    faculty_password = input("Enter new password (or leave blank to skip): ")
                    faculty_designation = input("Enter new designation (or leave blank to skip): ")
                    faculty_subject = input("Enter new subject (or leave blank to skip): ")
                    faculty_data = {
                        "username": faculty_username,
                        "password": faculty_password,
                        "designation": faculty_designation,
                        "subject": faculty_subject,
                    }
                    result = self.controller.update_faculty(faculty_id, faculty_data)
                    print(result)
                except ValueError:
                    print("Invalid input. Please try again.")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")

            elif choice == "6":
                try:
                    student_id = int(input("Enter student ID: "))
                    student_username = input("Enter new username (or leave blank to skip): ")
                    student_password = input("Enter new password (or leave blank to skip): ")
                    student_semester = input("Enter new semester (or leave blank to skip): ")
                    if student_semester:
                        student_semester = int(student_semester)
                        if student_semester < 1 or student_semester > 8:
                            raise ValueError(
                                "Invalid input. Please enter a valid number for semester (>= 1) and less than 8")
                    student_cgpa = input("Enter new CGPA (or leave blank to skip): ")
                    if student_cgpa:
                        student_cgpa = float(student_cgpa)
                        if student_cgpa < 0 or student_cgpa > 4:
                            raise ValueError(
                                "Invalid input. Please enter a valid float for CGPA (between 0 and 4).")
                    student_major = input("Enter new major (or leave blank to skip): ")
                    student_data = {
                        "username": student_username,
                        "password": student_password,
                        "semester": student_semester,
                        "cgpa": student_cgpa,
                        "major": student_major
                    }
                    result = self.controller.update_student(student_id, student_data)
                    print(result)
                except ValueError:
                    print("Invalid input. Please try again.")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
            elif choice == "7":
                try:
                    faculty_id = int(input("Enter faculty member ID: "))
                    result = self.controller.delete_faculty(faculty_id)
                    print(result)
                except ValueError:
                    print("Invalid input. Please try again.")
            elif choice == "8":
                try:
                    student_id = int(input("Enter student ID: "))
                    result = self.controller.delete_student(student_id)
                    print(result)
                except ValueError:
                    print("Invalid input. Please try again.")
            elif choice == "0":
                print("Thank you for using the Student Management System!")
                break
            else:
                print("Invalid choice, please try again.")

