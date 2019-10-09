from . import bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, url_for, redirect, request
from app.models import *
import html


# 发布文章
@bp.route('/article', methods=['POST'])
@jwt_required
def post_article():

    title = request.json.get('title', None)
    content = request.json.get('content', None)
    tags = request.json.get('tags', None, )
    # 对客户端输入进行安全转义
    title = html.escape(title)
    content = html.escape(content)
    author_id = get_jwt_identity()
    article = Article(author_id=author_id, title=title, content=content)
    db.session.add(article)
    for tag in tags:
        tag = Tag(tag=tag, type=1, f_id=author_id)
        db.session.add(tag)
    db.session.commit()

    return jsonify(msg='ok', code=1, data={}), 200


# 获取文章
@bp.route('/article/<article_id>:int', methods=['GET'])
def get_article(article_id):
    try:
        article = Article.query.filter_by(id=article_id).first()
        if article is not None:
            data = article.to_dict()
            return jsonify(msg='ok', code=1, data=data), 200
        else:
            return jsonify(msg='ok', code=1, data='此文章不存在或者已经删除！'), 404
    except:
        data = '数据查询失败！'
        return jsonify(msg='error', code=500, data=data), 500


# 获取文章列表
@bp.route('/articles', methods=['GET'])
def get_articles():
    limit = request.json.get('limit', 50)  # 文章数量
    offset = request.json.get('offset', 0)
    articles = Article.query.limit(limit).offset(offset).all()
    print(articles)
    return jsonify({
        'data': [article.to_dict() for article in articles]
    }), 200


# 评论文章
@bp.route('/article/comment', methods=['POST'])
@jwt_required
def post_comment():
    if request.method == 'POST':
        user_id = get_jwt_identity()

        article_id = request.json.get('article_id', None)
        content = request.json.get('content', None)
        parent_id = request.json.get('parent_id', None)
        comment = Comment(commentator_id=user_id, content=content, article_id=article_id)
        if parent_id:
            parent = Comment.query.filter_by(id=parent_id).first()
            print(parent)
            parent.append(comment)
        else:
            db.session.add(comment)
            print(comment)
        db.session.commit()
        return jsonify({
            'data': comment.id
        }), 200


# 获取评论
@bp.route('/articles/<id>/comments', methods=['GET'])
def get_comments(id):
    limit = request.json.get('limit', 50)  # 文章数量
    offset = request.json.get('offset', 0)
    article = Article.query.get(id)
    comments = article.comments(limit=limit, offset=offset)
    return jsonify({
        "items": [comment.to_dict()  for comment in comments],
        "counts":len(comments)
    })
