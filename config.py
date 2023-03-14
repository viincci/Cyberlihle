class Config:
    DEBUG = False
    SECRET_KEY = b'\xfem\xa2\xd1\xd8\xc9=\x08)\x95}\xdfv\xd6F\x17'

class ProductionConfig(Config):
    ENV = 'production'
