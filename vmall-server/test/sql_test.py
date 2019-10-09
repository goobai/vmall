from app import create_app
from app.models import *
from unittest import TestCase
import unittest


class DbTestCase(TestCase):
    def setUp(self) -> None:
        db.drop_all()

    def tearDown(self) -> None:
        pass
        # db.session.remove()
        # db.drop_all()

    def addSku(self):
        sku = ProductSku(cid=3, spu_id=100003464635, shop_id=1,
                         name='一加 OnePlus 7  骁龙855旗舰性能 4800万超清双摄 8GB+256GB 曜岩灰 全面屏拍照智能游戏手机', original_price=9999,
                         price=2999, stock=200,
                         create_time=datetime.datetime.now(), modify_time=datetime.datetime.now(), status=0)
        db.session.add(sku)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
