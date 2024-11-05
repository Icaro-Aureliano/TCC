import os
class Config:
    SECRET_KEY = '75461'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '01234567'
    MYSQL_DB = 'Air_Control'
    MYSQL_HOST = 'localhost'
    UP_CONFIG = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
