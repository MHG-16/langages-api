from flask import Blueprint
from flask import Flask
from flask_restx import Api

from language.views import api_book

app = Flask(__name__)
blueprint = Blueprint("Api", __name__, url_prefix="/swagger")
api = Api(
    blueprint,
    doc="/documentation",
    title="Language Api",
    description="Tuto Api documentation",
)
app.register_blueprint(blueprint)
api.add_namespace(api_book)

app.config["SWAGGER_UI_JSONEDITOR"] = True


if __name__ == "__main__":
    app.run(debug=True)
