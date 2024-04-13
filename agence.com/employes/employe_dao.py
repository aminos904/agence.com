import database 
from employes.employe import Employe

class EmployeDao:
    connexion=database.connexionDB()
    cursor=connexion.cursor()

    def __init__(self):
        pass

    @classmethod
    #Ajouter un employé
    def creat(cls,emp:Employe):
        sql="insert into employes (matricule,nom,prenom,fonction,dep) values(%s,%s,%s,%s,%s)"
        try:
            EmployeDao.cursor.execute(sql, (emp.nom, emp.prenom, emp.matricule, emp.fonction, emp.dep))
            EmployeDao.connexion.commit()
            message=f"l'employé avec l'imatricule {emp.matricule} est ajouté avec succès"
        except  Exception as error:
            message = f"Erreur lors de la creation"
           # print(error)
        return message

    @classmethod
    def read(cls):
        sql = "select * from employes"
        EmployeDao.cursor.execute(sql)
        liste_employes = EmployeDao.cursor.fetchall()
        return liste_employes
        
    @classmethod
    def update(cls,emp:Employe):
        sql = "update employes set nom=%s, prenom=%s, fonction=%s, dep=%s where matricule=%s"
        EmployeDao.cursor.execute(sql,(emp.nom, emp.prenom, emp.fonction, emp.dep))
        EmployeDao.connexion.commit()

    @classmethod
    def delete(cls,matricule:Employe):
        sql = "delete from employes where matricule=%s"
        EmployeDao.cursor.execute(sql,(matricule.matricule,))
        EmployeDao.connexion.commit()

    @classmethod
    def get_one(cls, matricule ):
        sql= "SELECT * FROM employe WHERE natricule=/s"
        try:
            EmployeDao.cursor.execute(sql, (matricule, ))
            message= "secces"
            employe=EmployeDao.cursor.fetchone()
        except :
            employe=None
            message="erreur"
        return {"message":message,"data":employe }  