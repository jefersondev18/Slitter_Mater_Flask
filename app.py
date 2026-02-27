from flask import Flask, render_template, request, jsonify
from logic.home_logic import obter_mensagem_home



app = Flask(__name__)

@app.route("/")
def home():
    mensagem = obter_mensagem_home()
    return render_template("home.html")


@app.route("/plano_corte")
def plano_corte():
    return render_template("plano_corte.html")

@app.route("/necessidade_prod")
def necessidade_prod():
    return render_template("necessidade_prod.html")

@app.route("/config")
def config():
    return render_template("config.html")



if __name__ == "__main__":
    app.run(debug=True)