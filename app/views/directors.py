from flask_restx import Resource, Namespace
from app.container import director_service
from app.dao.model.directors import DirectorSchema
from flask import request

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):

        all_genres = director_service.get_all()

        return directors_schema.dump(all_genres), 200

    def post(self):

        req_json = request.get_json()

        director_service.create(req_json)

        return "Добавили сущность", 201


@director_ns.route('/<int:did>')
class DirectorsDidView(Resource):
    def get(self, did: int):
        return director_schema.dump(director_service.get_one(did)), 200

    def put(self, did: int):
        req_json = request.get_json()
        if 'id' not in req_json:
            req_json['id'] = did

        director_service.update(req_json)

        return "", 204

    def delete(self, did: int):
        director_service.delete(did)

        return "", 204
