class MovieService:

    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get('id')

        movie = self.dao.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')

        movie = self.dao.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)

    def search_director(self, data):
        if 'director_id' in data:
            return self.dao.search_director(data['director_id'])
        if 'genre_id' in data:
            return self.dao.search_genre(data['genre_id'])
        if 'year' in data:
            return self.dao.search_year(data['year'])



