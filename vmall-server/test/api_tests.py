import unittest
import app
import json
from datetime import datetime


class ApiTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.create_app()
        self.client = self.app.test_client()

    def test_cart_add(self):
        now = datetime.utcnow()
        now1 = now.strftime('%Y-%m-%d %H:%M:%S %f')
        now2 = now.strftime('%y-%m-%d %I:%M:%S %p')
        data = {"username": "goobai777",
                "phone": "15208177009",
                "password": "1",
                "email": "123@123.com"}
        response = self.client.post('/api/user/reg', data=json.dumps(data), content_type="application/json")
        assert response.status_code == 200, "注册接口测试失败"


if __name__ == '__main__':
    unittest.main()
