import unittest
import requests
import app
from flask_redis import FlaskRedis
import time
import redis


class RedisTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.create_app()
        self.redis_client = FlaskRedis(self.app)
        self.url = "http://127.0.0.1:5000"
        self.redis_client.init_app(self.app)
        self.info = {
            'age': 29,
            'name': "goobai",
            'id': 2,
            'address': {
                "1": 1,
                "province": "四川",
                "city": "遂宁"
            }
        }

    def test_set_key(self):
        dic = {
            'age': 29,
            'name': "goobai",
            'id': 2,
            'address': {
                "1": 1,
                "province": "四川",
                "city": "遂宁"
            }
        }

        self.redis_client.hmset('user_info:', dic)
        #
        # re = self.redis_client.hmget('user_info', 'name', 'age')
        # all = self.redis_client.hgetall('user_info')
        # print(re, all)
        # res = requests.get(url=self.url + "/api/rdb", params=dic)
        # print(res.url)
        # print(res.content)
        # self.redis_client.hmset('user:', self.info)
        t1 = time.time()
        self.redis_client.set("order:id", 0)
        for x in range(10):
            if not self.redis_client.exists("order:id"):
                self.redis_client.setnx("order:id", 1)
            else:
                res = self.redis_client.incrby("order:id", 1)
                print(res)
        t2 = time.time() - t1
        print(str(t2))


if __name__ == '__main__':
    unittest.main()
