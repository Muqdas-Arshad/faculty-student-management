class User:
    def __init__(self, id=None, username='', password=''):
        self.__id = id
        self.__username = username
        self.__password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def id(self):
        return self.__id

    @username.setter
    def username(self, cpyname):
        if cpyname != None and cpyname != '':
            self.__username = cpyname
        else:
            self.__username = ''
            print("ERROR! Please enter a valid input")

    @password.setter
    def password(self, passwd):
        if passwd != None and passwd != '':
            self.__password = passwd
        else:
            self.__password = ''
            print("ERROR! Please enter a valid input")

    @id.setter
    def id(self, id):
        if id != None and id != 0:
            self.__id = id
        else:
            self.__id = None
            print("ERROR! Please enter a valid input")
