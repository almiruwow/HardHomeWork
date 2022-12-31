from flask_restx import Resource, Namespace
from app.container import genre_service
from app.dao.model.genres import GenreSchema
from flask import request


genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class DirectorsView(Resource):
    def get(self):

        all_genres = genre_service.get_all()

        return genres_schema.dump(all_genres), 200

    def post(self):

        req_json = request.get_json()

        genre_service.create(req_json)

        return "Добавили сущность", 201


@genre_ns.route('/<int:gid>')
class DirectorsDidView(Resource):
    def get(self, gid):
        return genre_schema.dump(genre_service.get_one(gid)), 200

    def put(self, gid: int):
        req_json = request.get_json()
        if 'id' not in req_json:
            req_json['id'] = gid

        genre_service.update(req_json)

        return "", 204

    def delete(self, gid: int):

        genre_service.delete(gid)

        return "", 204