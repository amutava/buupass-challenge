import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    WTF_CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(object):
    DEBUG = True
    DEVELOPMENT = True

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(object):
    DEBUG = False

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True

    @staticmethod
    def init_app(app):
        pass


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
