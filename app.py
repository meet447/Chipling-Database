from flask import Flask, request, redirect, render_template, session
from users.login import create_useracc, retrive_useracc, get_uid
from users.projects import create_project, search_projects, get_project, retrive_project
from users.data import create_user
import secrets

app = Flask(__name__)
app.secret_key = "Hellossss"

@app.route("/")
def index():
    return redirect("/home")

@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = retrive_useracc()  # Call the function to retrieve users
        for user in users:
            if user["username"] == username:
                return "Username already in use"
        
        uid = secrets.token_hex(6)
        create_useracc(username, password, uid=uid)
        return redirect("/login")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users = retrive_useracc()
        for user in users:
            if user["username"] == username and user["password"] == password:
                session["username"] = username
                return redirect("/home")
        return "Invalid login credentials"
    return render_template("login.html")

@app.route("/home")
def home():
    if session["username"]:
       username = session["username"]
       print(username)
       uid = get_uid(username=username) 
       projects = search_projects(uid=uid)
       return render_template("home.html", projects=projects)
    else:
       return redirect("/register")

@app.route("/create")
def create_page():
    return render_template("database.html")

@app.route("/create_database", methods=["POST"])
def create_project_route():
    id = secrets.token_hex(6) 
    key = request.form.get("key")
    name = request.form.get("name")
    username = session["username"]
    print(username)
    uid = get_uid(username=username)
    create_user(id=id, key=key, uid=uid, username=username)
    create_project(id, key, name=name, uid=uid)
    return redirect("/")

@app.route("/logout")
def logout():
    # Remove the user's session data, if it exists
    session.pop("username", None)
    return redirect("/login")

@app.route("/project/<id>")
def projects_place(id):
    id = id
    data = get_project(id=id)
    name = data[0]["name"]
    project = retrive_project(id=id, name=name, key="")
    return project

if __name__ == "__main__":
    app.run(debug=True)
