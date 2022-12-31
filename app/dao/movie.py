from app.dao.model.movies import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

    def search_director(self, data):
        return self.session.query(Movie).filter(Movie.director_id==data)

    def search_genre(self, data):
        return self.session.query(Movie).filter(Movie.genre_id == data)

    def search_year(self, data):
        return self.session.query(Movie).filter(Movie.year == data)