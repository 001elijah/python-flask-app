class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "1jgjg01qweijq2nacvghaik4t"

    DB_NAME = "prod-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    IMAGE_UPLOADS = "/Users/illiazolotukha/Documents/GitHub/python-flask-app/app/static/img/uploads"
    ALLOWED_IMAGE_EXTENSIONS = ["PNG", "JPG", "JPEG", "GIF"]
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024

    CLIENT_IMAGES = "/Users/illiazolotukha/Documents/GitHub/python-flask-app/app/static/client/img"
    CLIENT_CSV = "/Users/illiazolotukha/Documents/GitHub/python-flask-app/app/static/client/csv"
    CLIENT_PDF = "/Users/illiazolotukha/Documents/GitHub/python-flask-app/app/static/client/pdf"
    CLIENT_REPORTS = "/Users/illiazolotukha/Documents/GitHub/python-flask-app/app/static/client/reports"

    SESSION_COOKIE_SECURE = True



class Production(Config):
    pass


class Development(Config):
    DEBUG = True

    DB_NAME = "dev-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    UPLOADS = "/home/username/projects/flask_test/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False


class Testing(Config):
    TESTING = True

    DB_NAME = "dev-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "password"

    SESSION_COOKIE_SECURE = False
