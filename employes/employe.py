class Employe:
    def __init__(self,nom, prenom, marticule,fonction,dep):
        self.__matricule= marticule
        self.__nom = nom
        self.__prenon= prenom
        self.__fonction = fonction
        self.__dep = dep

    @property
    def matricule(self):
        return self.__matricule

    @matricule.setter
    def matricule(self, value):
        self.__matricule = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenon

    @prenom.setter
    def prenom(self, value):
        self.__prenon = value

    @property
    def fonction(self):
        return self.__fonction

    @fonction.setter
    def fonction(self, value):
        self.__fonction = value

    @property
    def dep(self):
        return self.__dep

    @dep.setter
    def dep(self, value):
        self.__dep = value