from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login, app
from flask_jwt_extended import get_jwt_identity
from json import dumps


# 创建全文联合索引
# CREATE FULLTEXT INDEX ft_index ON article1000(title) WITH PARSER ngram;
# Index('my_index', 'article.c.title', mysql_prefix='FULLTEXT',mysql_with_parser="ngram"))

class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 被关注者id
    followed_id = db.Column(db.Integer)
    # 粉丝id
    follower_id = db.Column(db.Integer)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    nickname = db.Column(db.String(64), default=username)
    phone = db.Column(db.String(11), index=True)
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    lastseen = db.Column(db.DateTime, default=datetime.utcnow())
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    sex = db.Column(db.Enum('F', 'M', 'Na'), default='M')
    birthday = db.Column(db.DateTime)
    address = db.Column(db.String(120))
    hometown = db.Column(db.String(120))
    school = db.Column(db.String(120))
    company = db.Column(db.String(120))
    signature = db.Column(db.Text(), default="等我下完这把自走棋再写个签！")  # 个签
    status = db.Column(db.SmallInteger(), default=1)  # 用户状态 1：正常 2：禁用 3：在线 4：离线  5：忙碌

    # region methods
    def __repr__(self):
        return '<User username:{},user id :{} >'.format(self.username, self.id)

    def avatar(self):
        avatar = Img.query.filter_by(owner_id=self.id, owner_type=1).first()
        if avatar:
            return avatar.url
        else:
            return "https://huyaimg.msstatic.com/avatar/1094/9c/9bd826292dbe3a174fc81b5a6e781f_180_135.jpg?1559034850"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, followed_id):
        follower = Follower(followed_id=followed_id, follower_id=self.id)
        db.session.add(follower)
        db.session.commit()

    def unfollow(self, followed_id):
        follower = Follower.query.filter_by(followed_id=followed_id, follower_id=self.id).first()
        if follower:
            db.session.delecte(follower)
            db.session.commit()

    def followers(self, limit=50, offset=0):
        followers = Follower.query.filter_by(followed_id=self.id).limit(limit).offset(offset).all()
        if followers:
            return followers
        else:
            return []

    def followed(self, limit=50, offset=0):
        followers = Follower.query.filter_by(follower_id=self.id).limit(limit).offset(offset).all()
        if followers:
            return followers
        else:
            return []

    def followed_count(self):
        count = Follower.query.filter_by(follower_id=self.id).count()
        return count

    def follower_count(self):
        count = Follower.query.filter_by(followed_id=self.id).count()
        return count

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.username,
            'nickname': self.nickname,
            'sex': self.sex,
            'signature': self.signature,
            'lastseen': self.lastseen.isoformat() + 'Z',
            'followed': self.followed_count(),
            'followers': self.follower_count(),
            'avatar': self.avatar()
        }
        return data

    def card(self):
        return {
            'name': self.username,
            'nickname': self.nickname,
            'sex': self.sex,
            'followed': self.followed_count(),
            'followers': self.follower_count(),
            'signature': self.signature,
            'avatar': self.avatar()
        }
    # endregion

    # region staticmethods

    # endregion


@login.user_loader
def load_user(id):
    return get_jwt_identity()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    receiver_id = db.Column(db.Integer)
    body = db.Column(db.Text())
    send_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.SmallInteger, default=0)  # 消息状态 0：未读 1 ：已读

    def __repr__(self):
        return '<Message {}>'.format(self.body)

    def to_dict(self):
        return {
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "body": self.body,
            "send_time": self.send_time,
            "status": self.status,
        }


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer)
    title = db.Column(db.String(140))
    content = db.Column(db.Text())
    publish_time = db.Column(db.DateTime, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, default=datetime.utcnow)
    like = db.Column(db.Integer, default=0)
    dislike = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Article {}>'.format(self.content)

    def to_dict(self):
        data = {
            'id': self.id,
            'author_id': self.author_id,
            'title': self.title,
            'content': self.content,
            'publish_time': self.publish_time,
            'modify_time': self.modify_time,
            'like': self.like,
            'dislike': self.dislike,
            'comments': self.comments()
        }
        return data

    def comments(self, limit=50, offset=0):
        comments = Comment.query.filter_by(article_id=self.id).limit(limit).offset(offset).all()
        if comments:
            return comments
        else:
            return []


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30))
    type = db.Column(db.SmallInteger, default=1)  # 标签类型 1：文章 2：用户
    f_id = db.Column(db.Integer)  # 标签对应的用户或者文章id


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commentator_id = db.Column(db.Integer)  # 评论者 id
    article_id = db.Column(db.Integer)  # 文章id
    content = db.Column(db.Text())
    comment_time = db.Column(db.DateTime, default=datetime.utcnow)
    like = db.Column(db.Integer, default=0)
    dislike = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Comment {}>'.format(self.content)

    def to_dict(self):
        data = {
            'id': self.id,
            'commentator_id': self.commentator_id,
            'article_id': self.article_id,
            'content': self.content,
            'comment_time': self.comment_time,
            'like': self.like,
            'dislike': self.dislike,
        }
        return data


# u = User.query.filter_by(username='goobai').first()
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(120))


class Permission(db.Model):
    __tablename__ = 'permission'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(120))


class UserRole(db.Model):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)
    description = db.Column(db.String(120))
    status = db.Column(db.SmallInteger, default=0)


class RolePermission(db.Model):
    __tablename__ = 'role_permission'
    id = db.Column(db.Integer(), primary_key=True)
    role_id = db.Column(db.Integer)
    permission_id = db.Column(db.Integer)


class Operation(db.Model):
    __tablename__ = 'operation'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer)
    operation_time = db.Column(db.DateTime, default=datetime.utcnow)
    operation_type = db.Column(db.String(20))
    operation_ip = db.Column(db.String(15))


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    modify_time = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.BigInteger)  # 图片拥有者id
    owner_type = db.Column(db.SmallInteger, default=3)  # 图片拥有者分类 1：用户 2：文章 3:商品sku图片 4：详情图片 5:商品spu图片
