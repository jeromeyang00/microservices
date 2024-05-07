from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort

blp = Blueprint("login", "login", url_prefix="/login", description="Login operations")

@blp.route("/outlook_login")

class Login(MethodView):

    @blp.response(200)
    def get(self):
        return "Hello, World!"