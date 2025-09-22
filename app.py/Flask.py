from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return "<p>Olá Flask</p>"

@app.route("/")
def Sobre():
    return render_template ("Sobre.html")

@app.route("/")
def Contato():
    return render_template ("Contato.html")
