# config.py
class Config(object):
    """
    Common configurations
    """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_ECHO = False
    FLASK_LOG_LEVEL = 'DEBUG'
    SEND_FILE_MAX_AGE_DEFAULT = 5  # sets cache timeout


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
    FLASK_LOG_LEVEL = 'CRITICAL'
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
