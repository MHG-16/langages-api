from flask import Flask, Blueprint
from flask_restx import Api, Resource, fields

app = Flask(__name__)
blueprint = Blueprint('Api' , __name__, url_prefix="/swagger")
api = Api(blueprint , doc="/documentation")
app.register_blueprint(blueprint)

app.config["SWAGGER_UI_JSONEDITOR"] = True

lang_model = api.model("Languages", {"languages": fields.String("JAVASCRIPT")})
languages = [{"languages": "Python", "id": 1}]


@api.route("/languages")
class Languages(Resource):
    @api.marshal_with(lang_model, envelope = 'Languages')
    def get(self):
        return languages

    @api.expect(lang_model)
    def post(self):
        new_language = api.payload
        new_language["id"] = len(languages) + 1
        languages.append(new_language)
        return {"result": "language added"}, 201


if __name__ == "__main__":
    app.run(debug=True)
