from . import bp
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import *
from flask import jsonify, request,send_file
import datetime


@bp.route('/product/list', methods=['get'])
@jwt_required
def product_list():
    """查询商品列表"""
    if request.method == 'GET':
        limit = request.args.get('limit', int)
        page = request.args.get('page', int)
        if not limit or not page:
            return jsonify(code=0, data='参数错误！', msg='参数错误！')
        offset = (int(page) - 1) * int(limit)
        products = ProductSku.query.limit(int(limit)).offset(offset).all()
        total = ProductSku.query.count()
        data = [product.to_dict() for product in products]
        return jsonify(code=1, data={'product_list': data, 'total': total}, msg='查询成功！')


@bp.route('/product/create', methods=['post'])
@jwt_required
def product_create():
    """新增商品

    @@@
    ### args

    | args | nullable | type | remark |
    |--------|--------|--------|--------|
    |brand_id |false  |int    |品牌 id    |
    |cid      |true   |int    |分类 id    |
    |shop_id  |true   |int    |店铺 id    |
    |title    |true   |string |商品title  |
    |name     |true   |string |商品name   |
    |status   |true   |int    |商品状态   |
    |sku_list |true   |list   |sku列表    |

    ### return

    - ##### json

    ```json
    {"msg": "success", "code": 1}
    ```
    @@@
    """

    if request.method == 'POST':
        product = request.json.get('product')
        if not product:
            return jsonify(code=0, msg='请求参数错误')
        brand_id = product.get('brand_id', )
        cid = product.get('cid')
        shop_id = product.get('shop_id')
        spu_title = product.get('title')
        name = product.get('name')
        status = product.get('status')
        # 添加spu信息
        spu = ProductSpu(brand_id=brand_id, cid=cid, shop_id=shop_id, title=spu_title, name=name, status=status)
        db.session.add(spu)
        db.session.commit()
        sku_list = request.json.get('sku_list')
        if not sku_list:
            return jsonify(code=0, data='', msg='lock of sku_list,request params error')
        # 添加sku
        for sku in sku_list:
            product_sku = ProductSku(cid == cid, spu_id=spu.id, shop_id=shop_id, name=sku.name,
                                     original_price=sku.original_price,
                                     price=sku.price, stock=sku.stock, sales=sku.sales, status=sku.status)
            db.session.add(product_sku)
            db.session.commit()
            # 添加sku 规格
            sku_spec = SkuSpecValue(sku_id=product_sku.id, spec_id=sku.spec_id, spec_value_id=sku.spec_value_id)
            db.session.add(sku_spec)
            db.session.commit()
            # 添加sku图片信息
            for img in sku.images:
                sku_img = Img(url=img.url, owner_id=sku.id, owner_type=3)
                db.session.add(sku_img)
            db.session.commit()
        return jsonify(code=1, data='商品添加成功', msg='操作成功！')


@bp.route('/product/update', methods=['post'])
@jwt_required
def product_update():
    """修改商品信息
    """
    if request.method == 'POST':
        params = request.json
        sku_id = request.json.get('id')
        spu_id = request.json.get('spu_id')
        if sku_id:
            sku_info = params.get('sku_info')
            ProductSku.update_sku(sku_id, sku_info)
            return jsonify(code=1, data='', msg='操作成功！')
        elif spu_id:
            product = params.get('spu_info')
            ProductSpu.product_update(spu_id, product)
            return jsonify(code=0, data='该商品不存在', msg='操作失败！')
        else:
            return jsonify(code=0, data='该商品不存在', msg='操作失败！')


@bp.route('/product/del', methods=['post'])
@jwt_required
def product_del():
    """删除商品
    """
    if request.method == 'POST':
        sku_id = request.json.get('id')
        if sku_id:
            ProductSku.del_sku(sku_id)
            return jsonify(code=1, data='删除成功！', msg='操作成功！')
        else:
            return jsonify(code=0, data='请求参数错误', msg='操作失败！')


@bp.route('/product/deliver')
def product_deliver():
    """发货
    """
    if request.method == 'post':
        order_id = request.json.get('id')
        ship_id = request.json.get('ship_id')
        update_content = request.json.get('update_content')
        if not order_id or not ship_id:
            return jsonify(code=0, msg='请求错误，缺少必要参数！')
        order = Order.query.filert_by(id=id).first()
        # 发货
        ship_info = OrderShip(order_id=order_id, ship_id=ship_id, update_content=update_content)
        db.session.add(ship_info)
        order.order_status = 2  # 订单状态修改成已发货
        db.session.commit()
        return jsonify(code=1, data='', msg='发货成功！')


@bp.route('/product/category/list')
def product_category_list():
    import os
    print(os.environ.get('REDIS_URL'))
    os.environ.get('REDIS_URL')
    # root_category = Category.query.filter_by(index=1, parent_id=0).all()
    #
    # data = [{"label": root.name, "value": root.id, "children": []} for root in root_category]
    # for ds in data:
    #     second_category = Category.query.filter_by(index=2, parent_id=ds["value"]).all()
    #     ds["children"]=[{"label": root.name, "value": root.id, "children": []} for root in second_category]
    #     for dt in ds["children"]:
    #         third_category = Category.query.filter_by(index=3, parent_id=dt["value"]).all()
    #         dt["children"] = [{"label": root.name, "value": root.id, } for root in third_category]
    data = Category.get_category_list()
    return jsonify(code=1, data=data.get('tree'))


@bp.route('/product/sku')
def product_sku_create():
    if request.method == "POST":
        spu_id = request.json.get("spuId")
        price = request.json.get("price")
        name = request.json.get("name")
        specs_list = request.json.get("specsList")  # [{ specsId:int ,specValueId:123}]
        stock = request.json.get("stock")
        default_img_id = request.json.get("defaultImgId")

    if request.method == "GET":
        skuId = request.args.get("id")
        sku = ProductSku.query.filter_by(id=skuId).first()
        return jsonify(data=sku.to_dict())
        sql = r'''select * from article where id= :id'''
        res = db.session.execute(sql, {"id": 1}).fetchall()
        print(res)
        return jsonify(data=[str(row) for row in res])


@bp.route('/product/sku/list')
def product_sku_list():
    pass


@bp.route('/product/spu')
def product_spu_create():
    pass


@bp.route('/product/spu/list')
def product_spu_list():
    pass
