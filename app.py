from flask import Flask, render_template
from logic.home_logic import obter_mensagem_home

app = Flask(__name__)

@app.route("/")
def home():
    mensagem = obter_mensagem_home()
    return render_template("home.html", mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)