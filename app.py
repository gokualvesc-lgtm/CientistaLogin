from flask import Flask, render_template, url_for, redirect, session, request

app = Flask(__name__)

app.secret_key = "DGHALKSFGBAS"

usuarios = {"Klever": "09121988",
            "klever": "09121988"}


@app.route("/")
def mainScreen():
    session.clear()
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():

    if request.method == "POST":

        user = request.form.get("usuario")
        senha = request.form.get("senha")

        try:
            if not usuarios[user]:
                return render_template("login.html")
        except:
            pass
        try:
            if usuarios[user] == senha:
                session["logado"] = True
                return redirect(url_for("index"))
        except:
                pass

    return render_template("login.html")


@app.route("/dashboard", methods=["POST", "GET"])
def index():
    if not "logado" in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/funcionarios")
def funcinarios():
    if not "logado" in session:
        return redirect(url_for("login"))
    return render_template("funcionarios.html")

@app.route("/mensagens")
def mensagens():
    if not "logado" in session:
        return redirect(url_for("login"))
    return render_template("mensagens.html")

@app.route("/registros")
def registros():
    if not "logado" in session:
        return redirect(url_for("login"))
    return render_template("registros.html")


@app.route("/relatorios")
def relatorio():
    if not "logado" in session:
        return redirect(url_for("login"))
    return render_template("relatorios.html")


if __name__ == "__main__":
    app.run(debug=True)

