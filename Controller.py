from DB import DB
from Faculty import Faculty
from Student import Student
class Controller:
    def __init__(self):

        self.DB = DB("localhost", "root", "bsit2020", "fcit")

    def register_faculty(self, username, password, designation, subject):
        faculty = Faculty(username=username, password=password, designation=designation, subject=subject)
        return self.DB.register_faculty(faculty)

    def register_student(self, username, password, smester, cgpa, major):
        student_data = Student(username=username, password=password, smester=smester, cgpa=cgpa, major=major)
        return self.DB.register_student(student_data)


    def get_faculty(self, username, password):
        return self.DB.get_faculty(username, password)

    def get_student(self, username, password):
        return self.DB.get_student(username, password)

    def update_student(self, student_id, student_data):
        return self.DB.update_student(student_id, student_data)

    def update_faculty(self, faculty_id, faculty_data):
        return self.DB.update_faculty(faculty_id, faculty_data)

    def delete_faculty(self, faculty_id):
        return self.DB.delete_faculty(faculty_id)

    def delete_student(self, student_id):
        return self.DB.delete_student(student_id)
