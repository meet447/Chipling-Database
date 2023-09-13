from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route()
def get_request():
    print("hello")
    return "ok"


