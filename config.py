class Config(object):
    """
    Common configurations
    """
    # common configurations


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = False #True
    

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
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

serv_url='http://depemp-service.herokuapp.com'