import database
from users.user import User

class UserDAO:
    connexion = database.connexionDB()
    cursor = connexion.cursor()

    def __init__(self):
        pass
    
    @classmethod
    def creat(cls, emp: User):
        sql = "INSERT INTO users (nom, username, password, hash) VALUES (%s, %s, %s,%s)"
        try:
            UserDAO.cursor.execute(sql, (emp.nom, emp.username, emp.password,emp.hash))
            UserDAO.connexion.commit()
            message = f"Le nouvel utilisateur {emp.nom} est ajouté avec succès"
        except Exception as error:
            message = f"Erreur lors de la création : {error}"
        print(message)
        return message

    @classmethod
    def read(cls):
        sql = "SELECT * FROM users"
        UserDAO.cursor.execute(sql)
        liste = UserDAO.cursor.fetchall()
        return liste
        
    @classmethod
    def update(cls, emp: User):
        sql = "UPDATE users SET nom = %s, username = %s, password = %s WHERE id_utilisateur = %s"
        UserDAO.cursor.execute(sql, (emp.nom, emp.username, emp.password,))
        UserDAO.connexion.commit()

    @classmethod
    def delete(cls, emp: User):
        sql = "DELETE FROM users WHERE id_utilisateur = %s"
        UserDAO.cursor.execute(sql, (emp.nom,))
        UserDAO.connexion.commit()

    @classmethod
    def get_one(cls, username, password):
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        try:
            UserDAO.cursor.execute(sql, (username, password))
            user = UserDAO.cursor.fetchone()
            if user:
                message = "success"
            else:
                message = "failure"
        except Exception as e:
            user = None
            message = "Erreur"
          
        return message, user
    