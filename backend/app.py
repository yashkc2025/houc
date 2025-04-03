import os
from flask import Flask, make_response, g
from dotenv import load_dotenv
from database.models import SessionLocal
from flask_cors import CORS
from controller.user import userController
from controller.manage import adminController
from controller.general import generalController

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["API_KEY"] = os.getenv("API_KEY")
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "files")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

db_session = SessionLocal()

CORS(app, supports_credentials=True, origins=["http://localhost:8080"])


@app.route("/")
def home():
    return "Hello, World!"


@app.before_request
def before_request():
    g.db_session = db_session


@app.teardown_appcontext
def teardown_appcontext(exception):
    response = make_response()
    if hasattr(g, "db_session"):
        g.db_session.close()
    return response


app.register_blueprint(userController)
app.register_blueprint(adminController)
app.register_blueprint(generalController)

if __name__ == "__main__":
    app.run(debug=True)
