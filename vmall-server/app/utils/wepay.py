import requests


class WePayApi(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.host = app.config.get('WePayHost')

    def unified_order(self, data):
        """
        微信Native Api :统一下单
        :return: qr url
        """

        res = requests.post(self.url, data=data, header='')
        res.content

    def query_order(self):
        """
        微信Native Api :查询订单
        :return:
        """
        pass

    def close_order(self):
        """
        微信Native Api :关闭订单
        :return:
        """
        pass

    def refund(self):
        """
        微信Native Api :申请退款
        :return:
        """
        pass

    def query_refund(self):
        """
        微信Native Api :查询退款
        :return:
        """
        pass

    def download_bill(self):
        """
        微信Native Api :下载对账单
        :return:
        """
        pass

    def download_fund_flow(self):
        """
        微信Native Api :下载资金账单
        :return:
        """
        pass

    def report(self):
        """
        微信Native Api :交易保障
        :return:
        """
        pass

    def notify_pay_result(self):
        """
        微信Native Api :支付结果通知
        :return:
        """
        pass

    def short_url(self):
        """
        微信Native Api :转换短链接
        :return:
        """
        pass

    def notify_refund_result(self):
        """
        微信Native Api :退款结果通知
        :return:
        """
        pass

    def batch_query_comment(self):
        """
        微信Native Api :拉取订单评价数据
        :return:
        """
        pass
