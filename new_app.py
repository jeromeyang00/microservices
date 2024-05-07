from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api

# Initialize Flask App
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dbpass1234@34.230.58.127/eece-queue-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Smorest API
api = Api(app)

# Configure Swagger UI
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "EECE_Queuing_System"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Import and register blueprints
from student import student_blp

api.register_blueprint(student_blp)

if __name__ == "__main__":
    app.run(debug=True)
