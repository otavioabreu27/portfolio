from email.mime import application
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profissional")
def profissional():
    return render_template("profissional.html")

@app.route("/academico")
def academico():
    return render_template("academico.html")

@app.route("/tecnologias")
def tecnologias():
    return render_template("tecnologias.html")

if __name__ == "__main__":
     app.run(debug=True)