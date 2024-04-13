import database 
from deps.dep import Dep

class DepDAO:
    connexion=database.connexionDB()
    cursor=connexion.cursor()

    def __init__(self):
        pass

    @classmethod
    #Ajouter un employé
    def creat(cls,emp:Dep):
        sql="insert into dep (nom,emplacement) values(%s,%s)"
        try:
            DepDAO.cursor.execute(sql, (emp.nom, emp.emplacement))
            DepDAO.connexion.commit()
            message=f"Le nouveau departement {emp.emplacement} est ajouté avec succès"
        except  Exception as error:
            message = f"Erreur lors de la creation"
           # print(error)
        return message

    @classmethod
    def read(cls):
        sql = "select * from employes"
        DepDAO.cursor.execute(sql)
        liste_employes = DepDAO.cursor.fetchall()
        return liste_employes
        
    @classmethod
    def update(cls,emp:Dep):
        sql = "update dep set nom=%s, emplacement=%s"
        DepDAO.cursor.execute(sql, (emp.nom, emp.emplacement))
        DepDAO.connexion.commit()

    @classmethod
    def delete(cls,emp:Dep):
        sql = "delete from dep where id=%s"
        DepDAO.cursor.execute(sql,(emp.emplacement,))
        DepDAO.connexion.commit()

