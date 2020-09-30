import os
class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patrick:201400@localhost/blog'
    SECRET_KEY = 'huwezi sahau'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patrick:201400@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}