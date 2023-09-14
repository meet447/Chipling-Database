from flask import Flask, request, redirect, render_template, session
from users.login import create_useracc, retrive_useracc
from users.projects import create_project
from users.data import create_user

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
        create_useracc(username, password)
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
    id = request.form.get("id")
    key = request.form.get("key")
    name = request.form.get("name")
    create_user(id=id, name=name, key=key)
    create_project(id, key, name)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
