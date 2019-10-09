import os, sys
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://mysql:Goobai!1@192.168.16.129/aipycms?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://mysql:Goobai!1@192.168.16.129/aipycms?charset=utf8"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://mysql:Goobai!1@localhost/aipycms?charset=utf8mb4"
    # SQLALCHEMY_ECHO = True  # 打印执行sql
    SQLALCHEMY_POOL_SIZE = 10  # 数据库连接 池的大小。默认是5
    # SQLALCHEMY_ECHO = False  # 不打印执行sql
    JWT_SECRET_KEY = 'u can''t get this word'
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_DB_QUERY_TIMEOUT = 3
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # redis://[:password]@host:port/db # TCP连接
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://:goobai777@192.168.16.129/0'
    # REDIS_URL = os.environ.get('REDIS_URL') or 'redis://:goobai777@localhost/0'
    # REDIS_URL = os.environ.get('REDIS_URL') or 'redis://:goobai777@176.122.160.143/0'

    # REDIS_PASSWORD = 'rediS123rooT'
    # Redis Config
    # REDIS_HOST = os.environ.get('REDIS_HOST', '176.122.160.143')
    # REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
    # REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', 'rediS123rooT')
    POSTS_PER_PAGE = 25
    BASE_DIR = os.environ.get('BASE_DIR') or basedir
    FONT_DIR = os.environ.get('FONT_DIR') or os.path.join(basedir, 'resource', 'fonts', 'arial.ttf')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or os.path.join(basedir, 'resource', 'uploaded_folder')
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG'])

    AppKey = 'c5983e289a03f7db22f4779998d42b0c'
    AppSecret = 'c50af7e0638e'
    Sms_Url = 'https://api.netease.im/sms/sendcode.action'

    # celery配置
    # CELERY_BROKER_URL = 'amqp://goobai:Goobai!1@localhost:5672/goobai_vhost'  # rabbitmq broker
    CELERY_BROKER_URL = 'redis://:rediS123rooT@95.181.190.215/2'  # redis broker
    CELERY_BACKEND_URL = 'redis://:rediS123rooT@95.181.190.215/3'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    # flask mail 配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.163.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '15208177009@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'goobai1'
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None or True
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or '15208177009@163.com'
    MAIL_MAX_EMAILS = os.environ.get('MAIL_MAX_EMAILS') or 10
    JWT_TOKEN_LOCATION = ("headers", "json", "query_string")

    WePay = {}
