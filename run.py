from flask import Flask
from tools.necessidade_slitter.routes import necessidade_slitter
from home.routes import home_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home_bp)
    app.register_blueprint(necessidade_slitter)
    
    

    return app
#teste

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)