import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patrick:201400@localhost/blog'
    SECRET_KEY = 'huwezi sahau'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}