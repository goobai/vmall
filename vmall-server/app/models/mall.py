from app import db
from datetime import datetime
from app.models import Img


class Category(db.Model):
    """商品分类"""
    id = db.Column(db.SmallInteger, primary_key=True)

    name = db.Column(db.String(64))  # 分类名称
    cid = db.Column(db.SmallInteger)  # 分类 id
    parent_id = db.Column(db.SmallInteger)  # 父分类id
    index = db.Column(db.SmallInteger)  # 分类的index：一级、二级、三级...
    status = db.Column(db.SmallInteger, default=0)  # 状态

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'parent_id': self.parent_id,
            'index': self.index,
            'status': self.status,
        }


class ProductSpu(db.Model):
    """商品spu：standard product unit"""
    id = db.Column(db.BIGINT, primary_key=True)
    brand_id = db.Column(db.Integer)  # 商品品牌id
    cid = db.Column(db.SmallInteger)  # 商品分类编号
    shop_id = db.Column(db.SmallInteger)  # 店铺 id
    title = db.Column(db.String(256))  # 商品标题
    name = db.Column(db.String(256))  # 商品名称
    create_time = db.Column(db.DateTime(), default=datetime.now())
    modify_time = db.Column(db.DateTime(), default=datetime.now())
    status = db.Column(db.SmallInteger, default=0)  # 状态

    @property
    def image(self):
        img = Img.query.filter_by(owner_id=self.id, owner_type=5).first()
        if img:
            return img.url
        else:
            default_img = Img.query.filter_by(owner_id=1, owner_type=5).first()
            return default_img.url

    @property
    def shop(self):
        shop = Shop.query.filter_by(id=self.shop_id).first()
        if shop:
            return shop.name
        else:
            return ''

    @property
    def sku_list(self):
        products = ProductSku.query.filter_by(spu_id=self.id).all()
        if not products:
            return []
        return [sku.to_dict() for sku in products]

    def product_create(self):
        product = ProductSpu(brand_id=self.brand_id, cid=self.cid, shop_id=self.shop_id, title=self.title,
                             name=self.name, create_time=self.create_time, modify_time=datetime.now(),
                             status=self.status)
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def product_update(spu_id, product):

        spu = ProductSpu.query.filter_by(id=spu_id).first()
        if not spu:
            return False
        spu.brand_id = product.get('brand_id', spu.brand_id)
        spu.cid = product.get('cid', spu.cid)
        spu.title = product.get('title', spu.title)
        spu.name = product.get('name', spu.name)
        spu.modify_time = datetime.now()
        spu.status = product.get('status', spu.status)
        spu.sku_list = product.get('sku_list')
        if not spu.sku_list:
            db.session.commit()
            return True
        for sku in spu.sku_list:
            ProductSku.update_sku(spu.id, sku)

        return True

    def to_dict(self):
        return {
            "id": self.id,
            "image": self.image,
            "name": self.name,
            "price": self.price,
            "comments": self.comments,
            "shop": self.shop,
            "shop_id": self.shop_id,
            "sku_list": self.sku_list,
            "status": self.status,
        }


class ProductSku(db.Model):
    """商品sku:stock keeping unit"""
    id = db.Column(db.BIGINT, primary_key=True)
    cid = db.Column(db.SmallInteger)  # 商品分类编号
    spu_id = db.Column(db.BIGINT)  # 商品id
    shop_id = db.Column(db.SmallInteger)  # 店铺 id
    name = db.Column(db.String(256))  # 商品名称
    original_price = db.Column(db.Integer)  # 原价
    price = db.Column(db.Integer)  # 当前价格
    stock = db.Column(db.Integer)  # 库存
    sales = db.Column(db.Integer)  # 销量
    comments = db.Column(db.String(64))  # 评论数量
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态

    @property
    def images(self):
        imgs = Img.query.filter_by(owner_id=self.id, owner_type=3).all()
        if imgs:
            return [img.url for img in imgs]
        else:
            # 默认预览图片
            default_imgs = Img.query.filter_by(owner_id=1, owner_type=3).all()
            return [img.url for img in default_imgs]

    @property
    def detail(self):
        imgs = Img.query.filter_by(owner_id=self.id, owner_type=4).all()
        if imgs:
            return [img.url for img in imgs]
        else:
            default_imgs = Img.query.filter_by(owner_id=1, owner_type=4).all()
            return [img.url for img in default_imgs]

    @property
    def shop(self):
        shop = Shop.query.filter_by(id=self.shop_id).first()
        if shop:
            return shop.name
        else:
            return ''

    def to_dict(self):
        return {
            "id": self.id, "title": self.name, "name": self.name, "price": self.price, "stock": self.stock,
            "images": self.images, 'spec': '',
            "detail": self.detail, "comments": self.comments, "shop": self.shop, "shop_id": self.shop_id
        }

    @staticmethod
    def del_sku(sku_id):
        sku = ProductSku.query.filter_by(id=sku_id).first()
        if sku:
            db.session.delete(sku)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def update_sku(sku_id, sku_info):
        """
        更新sku信息
        :param sku_id: int
        :param sku_info: json
        :return:
        """
        sku = ProductSku.query.filter_by(id=sku_id).first()
        if sku:
            sku.name = sku_info.get('name')
            sku.price = sku_info.get('price')
            sku.stock = sku_info.get('stock')
            sku.modify_time = datetime.now()
            sku.status = sku_info.get('status')
            return True
        else:
            return False


class Spec(db.Model):
    """
    规格表 sale prop
    """
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(16))  # 商品规格名。
    text = db.Column(db.String(16))  # 商品规格名显示值。如：颜色，版本，型号等
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态


class SpecValue(db.Model):
    """
    规格表
    """
    id = db.Column(db.Integer(), primary_key=True)
    spec_id = db.Column(db.BIGINT)  # 规格id
    value = db.Column(db.String(32))  # 商品规格值
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态


class SkuSpecValue(db.Model):
    """
    sku对应规格值
    """
    id = db.Column(db.Integer(), primary_key=True)
    sku_id = db.Column(db.BIGINT)  # sku id
    spec_id = db.Column(db.Integer)  # 规格id
    spec_value_id = db.Column(db.BIGINT)  # 规格值id
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态


class Cart(db.Model):
    """购物车"""
    id = db.Column(db.Integer, primary_key=True)
    sku_id = db.Column(db.BIGINT)  # 商品skuId
    user_id = db.Column(db.Integer, index=True)  # 用户id
    shop_id = db.Column(db.BIGINT)  # 商品店铺Id
    count = db.Column(db.Integer)  # 商品在购物车中选择的数量
    checked = db.Column(db.SmallInteger, default=1, )  # 购物车中该商品是否选择 0:未选择 1：选择
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())

    def to_dict(self):
        sku = ProductSku.query.filter_by(id=self.sku_id).first()
        shop = Shop.query.filter_by(id=sku.shop_id).first()
        return {
            'id': self.sku_id,
            'shop_id': self.shop_id,
            'name': sku.name,
            'shop_name': shop.name,
            'price': sku.price,
            'count': self.count,
            'checked': self.checked,
            'images': sku.images,
        }

    def cart_shop(self):
        shops = db.session.query(Cart).outerjoin(ProductSku, Cart.sku_id == ProductSku.id).filter(
            Cart.user_id == self.user_id).outerjoin(Shop, ProductSku.shop_id == Shop.id).with_entities(
            ProductSku.shop_id, Shop.name).group_by(ProductSku.shop_id).all()
        return {
            'id': shops.id,
            'name': shops.name,
            'products': [],
            'checked': self.checked
        }

    def shop_product(self, shop_id):
        result = Cart.query.filter_by(user_id=self.user_id, shop_id=shop_id).outerjoin(ProductSku,
                                                                                       Cart.sku_id == ProductSku.id).all()
        print(result)
        return {

        }


class Order(db.Model):
    """订单"""
    id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.BIGINT)  # 用户id
    user_address_id = db.Column(db.BIGINT)  # 用户收货地址对应id
    shop_id = db.Column(db.BIGINT)  # 店铺id
    order_id = db.Column(db.BIGINT, index=True)  # 订单号
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    total_price = db.Column(db.Integer, default=0)  # 订单商品总价格 单位为分
    order_status = db.Column(db.SmallInteger,
                             default=0)  # 订单状态状态 0:待付款 ；1：待发货；2：已发货，物流中，待确认收货 ；3：确认收货，待评价 4：评价完商品，订单完成 5:已取消
    status = db.Column(db.SmallInteger, default=0)  # 状态

    def to_dict(self):
        products = OrderProduct.query.filter_by(order_id=self.order_id).all()
        address_info = UserAddress.query.filter_by(id=self.user_address_id).first()
        return {
            "id": self.id,
            "order_id": self.order_id,
            "total_price": self.total_price,
            "order_status": self.order_status,
            "products": [product.to_dict() for product in products],
            "create_time": self.create_time,
            "address_info": address_info.to_dict()
        }


class OrderProduct(db.Model):
    """ 订单商品详情表"""
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT, index=True)  # 订单编号
    sku_id = db.Column(db.BIGINT, index=True)  # 商品sku id
    shop_id = db.Column(db.BIGINT, index=True)  # 商品shop id
    price = db.Column(db.String(64))  # 商品sku price
    count = db.Column(db.Integer)  # 商品下单数量
    total_price = db.Column(db.Integer)  # 商品总价
    coupon_amount = db.Column(db.Integer)  # 商品优惠券金额
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态

    def to_dict(self):
        image = Img.query.filter_by(owner_id=self.sku_id, owner_type=3).first()
        sku = ProductSku.query.filter_by(id=self.sku_id).first()
        return {
            "id": self.id,
            "order_id": self.order_id,
            "sku_id": self.sku_id,
            "shop_id": sku.shop_id,
            "shop_name": sku.shop,
            "sku_name": sku.name,
            "price": self.price,
            "count": self.count,
            "total_price": self.total_price,
            "coupon_amount": self.coupon_amount,
            "create_time": self.create_time,
            "img": image.url if image else ""
        }


class OrderPayment(db.Model):
    """订单支付详情表"""
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT, index=True)  # 订单编号
    pay_type = db.Column(db.SmallInteger, default=0)  # 支付方式
    outer_pay_no = db.Column(db.BIGINT, index=True)  # 第三方支付接口返回流水号
    amount = db.Column(db.Integer)  # 支付金额 单位为分
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    pay_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态 0：待支付 1：支付成功 3：支付失败


class OrderShip(db.Model):
    """订单物流详情表"""
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT, index=True)  # 订单编号
    ship_id = db.Column(db.BIGINT)  # 物流编号
    update_content = db.Column(db.String(128))  # 物流更新内容
    update_time = db.Column(db.DateTime, default=datetime.utcnow())  # 物流更新时间


class UserAddress(db.Model):
    """用户收货地址

    isDefault	是否为默认地址	boolean
    例如：addressDetail: "泉水人家3期B区"
    areaCode: "510106"
    city: "成都市"
    country: ""
    county: "金牛区"
    isDefault: false
    name: "goobai"
    postalCode: ""
    province: "四川省"
    tel: "15208177009"
    """
    id = db.Column(db.BIGINT, primary_key=True)
    user_id = db.Column(db.BIGINT, index=True)  # 用户 id
    name = db.Column(db.String(64))  # 收货人姓名
    phone = db.Column(db.String(32))  # 收货人手机号
    area_code = db.Column(db.String(32))  # 地区编码，通过省市区选择获取（必填）	string
    province = db.Column(db.String(32))  # 省份
    city = db.Column(db.String(32))  # 城市
    county = db.Column(db.String(32))  # 区县
    address_detail = db.Column(db.String(256))  # 详细地址
    postal_code = db.Column(db.String(32))  # 邮政编码
    isDefault = db.Column(db.String(32))  # 是否为默认
    status = db.Column(db.SmallInteger, default=0)  # 状态 0：待支付 1：支付成功 3：支付失败

    def full_address(self):
        if self.province == self.city:
            if self.city == self.county:
                return " ".join((self.province, self.county))
            else:
                return " ".join((self.province, self.county))
        else:
            if self.city == self.county:
                return " ".join((self.province, self.city))
            else:
                return " ".join((self.province, self.city, self.county))

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "name": self.name,
            "tel": self.phone,
            "areaCode": self.area_code,
            "province": self.province,
            "city": self.city,
            "county": self.county,
            "addressDetail": self.address_detail,
            "postalCode": self.postal_code,
            "isDefault": True if int(self.isDefault) else False,
            "address": " ".join((self.full_address(), self.address_detail)),
            "status": self.status,

        }


class Brand(db.Model):
    """商品品牌"""
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    status = db.Column(db.SmallInteger, default=0)  # 状态


class Shop(db.Model):
    """店铺"""
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    logo = db.Column(db.String(256))  # logo
    image = db.Column(db.String(256))  # image
    desc = db.Column(db.String(256))  #
    create_time = db.Column(db.DateTime(), default=datetime.now())
    modify_time = db.Column(db.DateTime(), default=datetime.now())
    status = db.Column(db.SmallInteger, default=0)  # 状态

    def card(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo': self.logo,
            'image': self.image
        }

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo': self.logo,
            'image': self.image,
            'status': self.status,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S') if self.create_time else '',
            'modify_time': self.modify_time.strftime('%Y-%m-%d %H:%M:%S') if self.modify_time else '',
        }


class OrderProductComment(db.Model):
    """订单商品评价表"""
    id = db.Column(db.BIGINT, primary_key=True)
    order_id = db.Column(db.BIGINT, index=True)  # 订单编号
    sku_id = db.Column(db.BIGINT, index=True)  # 商品sku id
    user_id = db.Column(db.BIGINT, index=True)  # 购买用户 id
    rate = db.Column(db.SmallInteger)  # 商品评分： 1 ，2 ，3，4 ，5
    content = db.Column(db.String(256))  # 评价内容
    like = db.Column(db.Integer)  # 赞
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态


class RecommendProduct(db.Model):
    """推荐商品表"""
    id = db.Column(db.BIGINT, primary_key=True)
    sku_id = db.Column(db.BIGINT, index=True)  # 商品sku id
    recommend_type = db.Column(db.SmallInteger, default=0)  # 为你精选：1 促销推荐 ：2，热卖商品：3
    expires_time = db.Column(db.DateTime, default=datetime.utcnow())  # 推荐过期时间
    create_time = db.Column(db.DateTime(), default=datetime.utcnow())
    modify_time = db.Column(db.DateTime(), default=datetime.utcnow())
    status = db.Column(db.SmallInteger, default=0)  # 状态

    def to_dict(self):
        image = Img.query.filter_by(owner_id=self.sku_id, owner_type=3).all()
        sku = ProductSku.query.filter_by(id=self.sku_id).first()
        return {
            "id": self.id,
            "sku_id": self.sku_id,
            "shop_id": sku.shop_id,
            "sku_name": sku.name,
            "price": sku.price,
            "create_time": self.create_time,
            "img": [img.url for img in image] if [img.url for img in image] else [
                "//img11.360buyimg.com/n1/s450x450_jfs/t1/29020/33/6838/263557/5c661ff4Ea61427ec/36f8fb23dc003d39.jpg"]
        }
