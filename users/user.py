class User:
    def __init__(self ,nom , username, password,hash):
        self.__nom = nom
        self.__username= username
        self.__password = password
        self.__hash = hash

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def hash(self):
        return self.__hash

    @nom.setter
    def hash(self, value):
        self.__hash = value
