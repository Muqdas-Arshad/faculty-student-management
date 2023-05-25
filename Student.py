from User import User

class Student(User):
    def __init__(self, id=None, username='', password='', stid=None, smester=0, cgpa=0.0, major='', user_id=None):
        super().__init__(id, username, password)
        self.__id = stid
        self.__smester = smester
        self.__cgpa = cgpa
        self.__major = major
        self.__user_id = user_id

    @property
    def smester(self):
        return self.__smester

    @property
    def cgpa(self):
        return self.__cgpa

    @property
    def major(self):
        return self.__major

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @smester.setter
    def smester(self, sem):
        if sem is not None and sem != '':
            self.__smester = sem
        else:
            self.__smester = 0
            print("ERROR! Please enter a valid input")

    @cgpa.setter
    def cgpa(self, cgpa):
        if cgpa is not None and cgpa != '':
            self.__cgpa = cgpa
        else:
            self.__cgpa = 0.0
            print("ERROR! Please enter a valid input")

    @major.setter
    def major(self, mj):
        if mj is not None and mj != '':
            self.__major = mj
        else:
            self.__major = ''
            print("ERROR! Please enter a valid input")

    @id.setter
    def id(self, id):
        if id is not None and id != 0:
            self.__id = id
        else:
            self.__id = None
            print("ERROR! Please enter a valid input")

    @user_id.setter
    def user_id(self, usrid):
        if usrid is not None and usrid != 0:
            self.__user_id = usrid
        else:
            self.__user_id = None
            print("ERROR! Please enter a valid input")
