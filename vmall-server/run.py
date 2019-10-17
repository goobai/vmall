from app import create_app
from app.models import User, Article, Message, Comment
from app import db
import config
import gevent
app = create_app(config.Config)


@app.shell_context_processor
def make_shell_context():
    return {'User': User, 'Message': Message, 'db': db, 'Article': Article, 'Comment': Comment}


from gevent.pywsgi import WSGIServer
#
# if __name__ == '__main__':
#     http_server = WSGIServer(('127.0.0.1', 5000), app)
#     http_server.serve_forever()


if __name__ == '__main__':
    app.run(debug=True)
    # print('Serving on 5000...')
    # WSGIServer(('127.0.0.1', 5000), app).serve_forever()

    # import tornado.wsgi,tornado.httpserver
#
# container = tornado.wsgi.WSGIContainer(app)
# http_server = tornado.httpserver.HTTPServer(container)
# http_server.listen(8888)
# tornado.ioloop.IOLoop.current().start()

# flask db stamp heads
# manage.py db init
# manage.py db migrate
# manage.py db upgrade
# flask db init
# flask db migrate
# flask db upgrade
# python manage.py runserver --host 0.0.0.0
# pip freeze > requirements.txt 生成
# in windows
# $env:FLASK_APP = ".\microblog.py"
# in linux
# export FLASK_APP=microblog.py
# flask shell
# export DATABASE_URL="mysql+pymysql://mysql:Goobai!1@176.122.160.143/test?charset=utf8" 
# CREATE FULLTEXT INDEX ft_index ON article1000(title) WITH PARSER ngram; 全文索引创建


# add user 'jimmy' with password 'jimmy123'
# $ rabbitmqctl add_user jimmy jimmy123
# # add virtual host 'jimmy_vhost'
# $ rabbitmqctl add_vhost jimmy_vhost
# # add user tag 'jimmy_tag' for user 'jimmy'
# $ rabbitmqctl set_user_tags jimmy jimmy_tag
# # set permission for user 'jimmy' on virtual host 'jimmy_vhost'
# $ rabbitmqctl set_permissions -p jimmy_vhost jimmy ".*" ".*" ".*"
