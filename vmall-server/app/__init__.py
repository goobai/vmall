from flask import Flask, current_app, request
from config import Config
from flask_sqlalchemy import get_debug_queries
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_docs import ApiDoc
import logging
import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
jwt = JWTManager()
mail = Mail()
mail.init_app(app)
# redis_client = FlaskRedis(app)
redis_client = FlaskRedis(app, decode_responses=True)
ApiDoc(app)


# logging.basicConfig(filename="./log.txt", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def create_app(config_class=Config):
    # csrf.init_app(app)
    db.init_app(app)
    redis_client.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    jwt.init_app(app)
    '''重置数据库'''
    reset_db(app)
    log_slow_query(app)
    reg_blueprints(app)
    # excute_sql(app)
    return app


def excute_sql(app):
    conn = db.engine.raw_connection()
    cursor = conn.cursor()
    cursor.excute('select * from `user` where `id`=%s', args=('1'))
    data = cursor.fetchone()


def reg_blueprints(app):
    # region 蓝图

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.api_v1 import bp as api_bp

    app.register_blueprint(api_bp, url_prefix='/api')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    # endregion


def reset_db(app=None):
    @app.before_first_request
    def reset_tables():
        from app.models import Order, OrderPayment, OrderProduct, UserAddress, OrderShip, Cart, OrderProductComment, \
            RecommendProduct, Message, UserRole, User
        # db.drop_all()
        # db.create_all()

        # UserAddress.__table__.drop(db.engine)
        # UserAddress.__table__.create(db.engine)
        # Message.__table__.drop(db.engine)
        # Message.__table__.create(db.engine)
        # Cart.__table__.drop(db.engine)
        # Cart.__table__.create(db.engine)
        # UserRole.__table__.drop(db.engine)
        # UserRole.__table__.create(db.engine)
        # RecommendProduct.__table__.drop(db.engine)
        # RecommendProduct.__table__.create(db.engine)
        # OrderProduct.__table__.drop(db.engine)
        # OrderProduct.__table__.create(db.engine)
        # OrderPayment.__table__.drop(db.engine)
        # OrderPayment.__table__.create(db.engine)
        # # OrderProductComment.__table__.drop(db.engine)
        # OrderProductComment.__table__.create(db.engine)
        # UserAddress.__table__.create(db.engine)
        # OrderPayment.__table__.create(db.engine)
        # OrderProduct.__table__.create(db.engine)
        # OrderAddress.__table__.create(db.engine)
        # OrderShip.__table__.create(db.engine)
        # print(db.engine)
        # user = User(username='goobai', phone='15208177777', email='goobai@qq.com', sex='F', address='cheng du',
        #             birthday=datetime.datetime(1990, 2, 7).strftime('%Y-%m-%d %H:%M:%S'),
        #             hometown='sui ning', signature='渣男会呼吸，渣女蹦野迪')
        # user.set_password('1')
        # db.session.add(user)
        # user = User(username='goobai1', phone='15208177777', email='goobai@qq.com')
        # user.set_password('1')
        # db.session.add(user)
        # db.session.commit()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def log_slow_query(app=None):
    @app.after_request
    def after_request(response):
        for query in get_debug_queries():
            if query.duration >= current_app.config['FLASKY_DB_QUERY_TIMEOUT']:
                current_app.logger.warning('Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n' % (
                    query.statement, query.parameters, query.duration, query.context))

        if request.endpoint != 'static':
            return response
        # response.cache_control.max_age = 15552000
        return response
