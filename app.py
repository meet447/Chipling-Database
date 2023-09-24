from flask import Flask, request, redirect, render_template, session
from users.login import create_useracc, retrive_useracc, get_uid
from users.projects import create_project
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
    if "username" in session:
        return f"Welcome, {session['username']}!"
    return redirect("/login")

@app.route("/create")
def create_page():
    return render_template("database.html")

@app.route("/create_database", methods=["POST"])
def create_project_route():
    id = secrets.token_hex(6) 
    key = request.form.get("key")
    name = request.form.get("name")
    username = session["username"]
    uid = get_uid(username=username)
    create_user(id=id, key=key, uid=uid, username=username)
    create_project(id, key, name=name)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
