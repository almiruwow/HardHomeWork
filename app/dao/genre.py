from app.dao.model.genres import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def create(self, data):
        genre = Genre(**data)

        self.session.add(genre)
        self.session.commit()

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
