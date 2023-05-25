import pymysql
from Faculty import Faculty
from Student import Student
from User import User
class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database= database

    def register_faculty(self, faculty):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = conn.cursor()
            query = "INSERT INTO user (username, password) VALUES (%s, %s)"
            values = (faculty.username, faculty.password)
            cursor.execute(query, values)
            user_id = cursor.lastrowid  # Get the ID of the last inserted row
            conn.commit()

            query = "INSERT INTO faculty (designation, subject, user_id) VALUES (%s, %s, %s)"
            values = (faculty.designation, faculty.subject, user_id)
            cursor.execute(query, values)
            conn.commit()

            print("Faculty registered successfully.")
        except Exception as e:
            conn.rollback()
            print("Error occurred while registering faculty:", e)

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def register_student(self, student):

            conn = None
            cursor = None
            try:
                conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                cursor = conn.cursor()
                query = "INSERT INTO user (username, password) VALUES (%s, %s)"
                values = (student.username, student.password)
                cursor.execute(query, values)
                user_id = cursor.lastrowid  # Get the ID of the last inserted row
                conn.commit()

                query = "INSERT INTO student (smester, cgpa, major, user_id) VALUES (%s, %s, %s, %s)"
                values = (student.smester, student.cgpa, student.major, user_id)
                cursor.execute(query, values)
                conn.commit()

                print("Student registered successfully.")
            except Exception as e:
                conn.rollback()
                print("Error occurred while registering faculty:", e)

            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()

    def get_faculty(self, username, password):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            query = "SELECT * FROM user INNER JOIN faculty ON faculty.user_id=user.id WHERE user.username=%s AND user.password=%s"
            values = (username, password)
            cursor = conn.cursor()
            cursor.execute(query, values)
            faculty_data = cursor.fetchone()
            if faculty_data is not None:
                print('Found faculty member:')
                faculty = Faculty(userid=faculty_data[3], username=faculty_data[1], password=faculty_data[2],
                                  id=faculty_data[6], designation=faculty_data[4], subject=faculty_data[5])

                return faculty_data
            else:
                return None
        except pymysql.Error as e:
            print("An error occurred:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def get_student(self, username, password):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            query="SELECT * FROM user INNER JOIN student ON student.user_id=user.id WHERE user.username=%s AND user.password=%s"

            values = (username, password)
            cursor = conn.cursor()
            cursor.execute(query, values)
            student_data = cursor.fetchone()
            if student_data is not None:
                print('Found Student member:')
                student = Student(stid=student_data[3], username=student_data[1], password=student_data[2],
                                  id=student_data[7], semester=student_data[4], cgpa=student_data[5],major=student_data[6])

                return student_data
            else:
                return None
        except pymysql.Error as e:
            print("An error occurred:", e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def delete_faculty(self, user_id):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            sql = "DELETE FROM faculty WHERE user_id = %s"
            values = (user_id,)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            #faculty_data = cursor.fetchone()
            sql = "DELETE FROM user WHERE id = %s"
            values = (user_id,)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            print("Faculty with id ", user_id, " has been deleted.")
        except:
            print("Error deleting faculty with id ", user_id)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def delete_student(self, user_id):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            sql = "DELETE FROM student WHERE user_id = %s"
            values = (user_id,)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            # faculty_data = cursor.fetchone()
            sql = "DELETE FROM user WHERE id = %s"
            values = (user_id,)
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            print("Student with id ", user_id, " has been deleted.")
        except:
            print("Error deleting student with id ", user_id)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_faculty(self, faculty_id, faculty):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = conn.cursor()

            # Get the existing faculty record
            query = "SELECT * FROM faculty WHERE id = %s"
            arg = (faculty_id,)
            cursor.execute(query, arg)
            fac_row = cursor.fetchone()

            if fac_row is not None:
                # Update the designation if present in the input data
                if 'designation' in faculty and faculty['designation'] != "":
                    fac_designation = faculty['designation']
                else:
                    fac_designation = fac_row[1]

                # Update the subject if present in the input data
                if 'subject' in faculty and faculty['subject'] != "":
                    fac_subject = faculty['subject']
                else:
                    fac_subject = fac_row[2]

                # Update the user record with the new username and password
                if 'username' in faculty and faculty['username'] != "":
                    query = "UPDATE user SET username = %s WHERE id = %s"
                    arg = (faculty['username'], fac_row[3])
                    cursor.execute(query, arg)

                if 'password' in faculty and faculty['password'] != "":
                    query = "UPDATE user SET password = %s WHERE id = %s"
                    arg = (faculty['password'], fac_row[3])
                    cursor.execute(query, arg)

                # Update the faculty record with the new designation and subject
                query = "UPDATE faculty SET designation = %s, subject = %s WHERE id = %s"
                arg = (fac_designation, fac_subject, faculty_id)
                cursor.execute(query, arg)

                # Commit the changes to the database
                conn.commit()
                print("Successfully updated.")

            else:
                print(f"No faculty record found with id {faculty_id}.")

        except Exception as e:
            print(str(e))

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def update_student(self, student_id, student):
        conn = None
        cursor = None
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            cursor = conn.cursor()

            # Get the existing student record
            query = "SELECT * FROM user JOIN student ON user.id = student.user_id WHERE student.user_id = %s"
            arg = (student_id,)
            cursor.execute(query, arg)
            std_row = cursor.fetchone()

            if std_row is not None:
                # Update the username if present in the input data
                if 'username' in student and student['username'] != "":
                    std_username = student['username']
                else:
                    std_username = std_row[1]

                # Update the password if present in the input data
                if 'password' in student and student['password'] != "":
                    std_password = student['password']
                else:
                    std_password = std_row[2]

                # Update the semester if present in the input data
                if 'semester' in student and student['semester'] != "":
                    std_semester = student['semester']
                else:
                    std_semester = std_row[4]

                # Update the cgpa if present in the input data
                if 'cgpa' in student and student['cgpa'] != "":
                    std_cgpa = student['cgpa']
                else:
                    std_cgpa = std_row[5]

                # Update the major if present in the input data
                if 'major' in student and student['major'] != "":
                    std_major = student['major']
                else:
                    std_major = std_row[6]

                # Update the user record with the new username and password
                query = "UPDATE user SET username = %s, password = %s WHERE id = %s"
                arg = (std_username, std_password, std_row[0])
                cursor.execute(query, arg)

                # Update the student record with the new semester, cgpa, major, and user_id
                query = "UPDATE student SET smester = %s, cgpa = %s, major = %s, user_id = %s WHERE user_id = %s"
                arg = (std_semester, std_cgpa, std_major, std_row[0], student_id)
                cursor.execute(query, arg)

                # Commit the changes to the database
                conn.commit()

        except Exception as e:
            print(str(e))

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()


