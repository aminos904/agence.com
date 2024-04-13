class Dep:
    def __init__(self ,nom , emplacement):
        self.__nom = nom
        self.__emplacement= emplacement

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def emplacement(self):
        return self.__emplacement

    @emplacement.setter
    def emplacement(self, value):
        self.__emplacement = value


