from User import User


class Faculty(User):
    def __init__(self, id=None, username='', password='', userid=None, designation="", subject="", user_id=None):
        super().__init__(id, username, password)
        self.__id = userid
        self.__designation = designation
        self.__subject = subject
        self.__user_id = user_id

    @property
    def designation(self):
        return self.__designation

    @property
    def subject(self):
        return self.__subject

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @designation.setter
    def designation(self, dsgntion):
        if dsgntion != None and dsgntion != '':
            self.__designation = dsgntion
        else:
            self.__designation = ''
            print("ERROR! Please enter a valid input")

    @subject.setter
    def subject(self, subj):
        if subj != None and subj != '':
            self.__subject = subj
        else:
            self.__subject = ''
            print("ERROR! Please enter a valid input")

    @id.setter
    def id(self, id):
        if id != None and id != 0:
            self.__id = id
        else:
            self.__id = None
            print("ERROR! Please enter a valid input")

    @user_id.setter
    def user_id(self, usrid):
        if usrid != None and usrid != 0:
            self.__user_id = usrid
        else:
            self.__user_id = 0
            print("ERROR! Please enter a valid input")
