from flask import Flask, render_template, request, redirect, url_for, session
from employes.employe import Employe
from employes.employe_dao import EmployeDao
from deps.dep import Dep
from deps.dep_dao import DepDAO
from users.user import User
from users.user_dao import UserDAO
from flask_bcrypt import  Bcrypt

app = Flask(__name__)
app.secret_key= "secret key"
bcrypt=Bcrypt(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_employe', methods=['GET', 'POST'])
def add_employe():
    message = None
    if request.method == "POST":
        req = request.form
        nom = req['nom']
        prenom = req['prenom']
        matricule = req['matricule']
        fonction = req['fonction']
        dep = req['dep']
        if nom == "" or prenom == "" or matricule == "" or fonction == "":
            message = "Error: All fields are required."
        else:
            employe = Employe(nom, prenom, matricule, fonction, dep)
            message = EmployeDao.creat(employe) 
    return render_template('add_employe.html', message=message)

@app.route('/list_employe')
def list_employe():
    if not session:
        return redirect(url_for("login"))
    else:
        employes = EmployeDao.read()
        return render_template("list_employe.html", employes=employes)

@app.route('/list_dep')
def list_dep():
    if not session:
        return  redirect(url_for("login"))
    else:
        deps = DepDAO.read()  
        return render_template("list_dep.html", deps=deps)

@app.route('/add_dep', methods=['GET', 'POST'])
def add_dep():
    if not session:
        return  redirect(url_for("login"))
    else:
        message = None
        if request.method == "POST":
            req = request.form
            nom = req["nom"]
            emplacement = req["emplacement"]
            if nom == "" or emplacement == "":
                message = "error"
            else:
                dep = Dep(nom, emplacement)
                message = DepDAO.creat(dep)  
                return render_template("add_dep.html", message=message)

@app.route('/list_user')
def list_user():  
    users = UserDAO.read()
    return render_template("list_user.html", users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        req = request.form
        username = req['username']
        password = req['password']
        if username == "" or password == "":
            message = "error"
        else:
            message, user = UserDAO.get_one(username, password)
            print(message, user)
            if message == 'success':
                session['username'] = user[2]
                session['nom'] = user[1]
                return redirect(url_for('home'))

    return render_template("login.html", message=message, user=None)

@app.route('/add_user' ,methods = ["GET","POST"])
def  add_user(): 
    message=""
    if request.method=="POST":
        req=request.form
        nom=req["nom"]
        username=req["username"]
        password=req["password"]
        print('1')
        if username == "" or password == "" or  nom == "":
           message="Veuillez remplir tout les champs." 

        else :
                message, user = UserDAO.get_one(username, password)
                print(message, user)
                hash=bcrypt.generate_password_hash(password)
                new_user = User(nom,username, password, hash)
                message = UserDAO.creat(new_user)
                print(hash)
                print('else')
                return redirect(url_for('login'))
        
    return render_template('add_user.html',message=message)

@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('login'))

