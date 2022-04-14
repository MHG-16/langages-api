from flask_restx import fields
from flask_restx import Namespace
from flask_restx import Resource

from .models import Langage


python = Langage(1, "Java", "Spring boot")
languages = [python.get()]

api_book = Namespace("language")

lang_model = api_book.model(
    "Languages",
    {
        "language": fields.String("JavaScript"),
        "framework": fields.String("React Native"),
    },
)


@api_book.route("/languages")
class Languages(Resource):
    @api_book.doc(
        responses={
            200: "Success",
            401: "Error internal server",
            400: "Error connection database",
        }
    )
    def get(self):
        return languages

    @api_book.expect(lang_model)
    def post(self):
        Langage.insert(languages=languages)
        return {"result": "language added"}, 201
