from flask import Flask
from flask_restx import Api

from app.config import Config
# from app.dao.model.movies import Movie
# from app.dao.model.genres import Genre
# from app.dao.model.directors import Director
from app.setup_db import db
from app.views.movies import movie_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
#     create_data(app, db)
#
# def create_data(app, db):
#     with app.app_context():
#
#         direct1 = Director(name='Карина')
#         genre1 = Genre(name='Ужасы')
#         mov1 = Movie(title='Фильм', description='Описание', trailer='есть', year=2000, rating=2, genre=genre1, director=direct1)
#
#         with db.session.begin():
#             db.session.add([mov1])


app = create_app(Config())

if __name__ == '__main__':
    app.run(host="localhost", port=10001)
