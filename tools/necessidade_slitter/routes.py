from flask import Blueprint, render_template
from .service import mensagem_necessidade_slitter

necessidade_slitter = Blueprint(
    "necessidade_slitter",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/necessidade_slitter"
)

@necessidade_slitter.route("/")
def pagina_necessidade_slitter():
    msg = mensagem_necessidade_slitter()
    return render_template("necessidade_slitter.html", msg=msg)