from functools import wraps

from flask import request
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

parser = api_book.parser()
parser.add_argument("X-API-KEY", location="headers")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if "X-API-KEY" in request.headers:
            token = request.headers["X-API-KEY"]

        if not token:
            return {"message": "Token is missing"}, 401

        if token != "myToken":
            return {"message": "Your token is wrong, wrong, wrong !!!"}, 401
        return f(*args, **kwargs)

    return decorated


@api_book.doc(
    responses={
        200: "Success",
        401: "token missing or token wrong",
        400: "Error connection database",
    },
    security="apiKey",
)
@api_book.header("X-API-KEY")
@api_book.route("/languages")
@api_book.expect(parser)
class Languages(Resource):
    @token_required
    def get(self):
        return languages

    @token_required
    @api_book.expect(lang_model)
    def post(self):
        Langage.insert(languages=languages)
        return {"result": "language added"}, 201
