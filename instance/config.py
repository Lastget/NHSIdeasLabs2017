import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY= b"9\xc2\xee\xf6x*\xca\x92t\x9b\xe9\x19z\xbf'\x84\xef\x81\xc0\xde\x92\xab\x85\xb3"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + TOP_LEVEL_DIR + '\db\main.db'
