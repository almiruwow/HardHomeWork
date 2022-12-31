class Config():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # Хотел бы спросить, почему когда я пытаюсь указать путь к базе данных по адресу 'sqlite:////instance/database.db'
    #  у меня выходит ошибка подключения к базе данных ?
    SQLALCHEMY_TRACK_MODIFICATIONS = False
