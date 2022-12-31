from flask_restx import Resource, Namespace
from app.dao.model.movies import MovieSchema
from app.container import movie_service
from flask import request

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        if len(request.args) > 0:
            return movies_schema.dump(movie_service.search_director(request.args)), 200

        all_movies = movie_service.get_all()

        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.get_json()

        movie_service.create(req_json)

        return "Добавили сущность", 201


@movie_ns.route('/<int:mid>')
class MoviesIdViews(Resource):
    def get(self, mid):
        one_movie = movie_service.get_one(mid)
        return movie_schema.dump(one_movie), 200

    def put(self, mid):
        req_json = request.get_json()

        if 'id' not in req_json:
            req_json['id'] = mid

        movie_service.update(req_json)

        return "", 204

    def patch(self, mid):
        req_json = request.get_json()

        if 'id' not in req_json:
            req_json['id'] = mid

        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)

        return "", 204

