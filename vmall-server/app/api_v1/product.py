from . import bp
from flask import jsonify, request
from app.models import *
from flask_jwt_extended import jwt_required, verify_jwt_in_request


@bp.route('/categories', methods=['GET', 'POST', 'PUT', 'DELETE'])
def categories():
    """根分类列表查询
    """
    sons = Category.query.filter_by(parent_id=0, index=1).all()
    s2list = [son.to_dict() for son in sons]
    return jsonify({
        'code': '1',
        'data': s2list
    })


@bp.route('/category', methods=['GET', 'POST', 'PUT', 'DELETE'])
def category():
    """分类列表查询
    """
    cid = request.args.get('id')
    # 根据根id查找出二级菜单
    sons = Category.query.filter_by(parent_id=cid, index=2).all()
    s2list = [son.to_dict() for son in sons]
    for son in s2list:
        grandsons = Category.query.filter_by(parent_id=son['id']).all()
        g2list = [grandson.to_dict() for grandson in grandsons]
        son['sons'] = g2list
    return jsonify({
        'code': '1',
        'data': s2list
    })


@bp.route('/products', methods=['GET', 'POST', 'PUT', 'DELETE'])
def products():
    """商品列表查询
    """
    search_type = request.args.get('type')
    if request.method == 'GET' and search_type == 'category':
        cid = request.args.get('cid')
        offset = request.args.get('offset', default=0)
        products_list = ProductSku.query.filter_by(cid=cid).limit(14).offset(offset).all()
        res = [product.to_dict() for product in products_list]
        return jsonify({
            'code': '1',
            'data': res
        })
    if request.method == 'GET' and search_type == 'search':
        offset = request.args.get('offset', default=0)
        keyword = request.args.get('keyword')
        products_list = ProductSku.query.filter(ProductSku.name.like("%" + keyword + "%")).limit(14).offset(
            offset).all()
        res = [product.to_dict() for product in products_list]
        return jsonify({
            'code': '1',
            'data': res
        })


@bp.route('/product/<int:id>/', methods=['GET', 'POST'])
def product_detail(id):
    """查看商品详情
    """
    sku = ProductSku.query.filter_by(id=id).first()
    if sku:
        return jsonify(code=1, data=sku.to_dict())
    else:
        return jsonify(code=0, data='没有相关数据')


@bp.route('/product/info', methods=['GET'])
def sku_info():
    data = {
        # // 所有sku规格类目与其值的从属关系，比如商品有颜色和尺码两大类规格，颜色下面又有红色和蓝色两个规格值。
        # // 可以理解为一个商品可以有多个规格类目，一个规格类目下可以有多个规格值。
        'tree': [
            {
                'k': '颜色',  # // skuKeyName：规格类目名称
                'v': [
                    {
                        'id': '30349',  # skuValueId：规格值 id
                        'name': '红色',  # skuValueName：规格值名称
                        'imgUrl': 'https://img.yzcdn.cn/1.jpg'  # 规格类目图片，只有第一个规格类目可以定义图片
                    },
                    {
                        'id': '1215',
                        'name': '蓝色',
                        'imgUrl': 'https://img.yzcdn.cn/2.jpg'
                    }
                ],
                'k_s': 's1'  # skuKeyStr：sku 组合列表（下方 list）中当前类目对应的 key 值，value 值会是从属于当前类目的一个规格值 id
            }
        ],
        # // 所有 sku 的组合列表，比如红色、M 码为一个 sku 组合，红色、S 码为另一个组合
        list: [
            {
                'id': 2259,  # // skuId，下单时后端需要
                'price': 100,  # // 价格（单位分）
                's1': '1215',  # // 规格类目 k_s 为 s1 的对应规格值 id
                's2': '1193',  # // 规格类目 k_s 为 s2 的对应规格值 id
                's3': '0',  # // 最多包含3个规格值，为0表示不存在该规格
                'stock_num': 110  # // 当前 sku 组合对应的库存
            }
        ],
        'price': '1.00',  # // 默认价格（单位元）
        'stock_num': 227,  # // 商品总库存
        'collection_id': 2261,  # // 无规格商品 skuId 取 collection_id，否则取所选 sku 组合对应的 id
        'none_sku': False,  # // 是否无规格商品
        'messages': [
            {
                # // 商品留言
                'datetime': '0',  # // 留言类型为 time 时，是否含日期。'1' 表示包含
                'multiple': '0',  # // 留言类型为 text 时，是否多行文本。'1' 表示多行
                'name': '留言',  # // 留言名称
                'type': 'text',  # // 留言类型，可选: id_no（身份证）, text, tel, date, time, email
                'required': '1'  # // 是否必填 '1' 表示必填
            }
        ],
        'hide_stock': False  # // 是否隐藏剩余库存
    }
    return jsonify(code=1, data=data)


@bp.route('/recommend/products')
def recommend_products():
    if request.method == "GET":
        offset = request.args.get('offset')
        recommend_type = request.args.get('type')  # 为你精选：1 促销推荐 ：2，热卖商品：3
        product_sku = RecommendProduct.query.filter_by(recommend_type=recommend_type).offset(offset).limit(10).all()
        data = [product.to_dict() for product in product_sku]
        return jsonify(code=1, data=data, msg="查询成功！")
    else:
        return jsonify(code=0, data="", msg="不支持此接口！！")
