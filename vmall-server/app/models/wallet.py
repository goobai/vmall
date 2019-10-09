from app import db


class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)  # 用户id
    amounts = db.Column(db.DECIMAL)  # 金额
    status = db.Column(db.SMALLINT)  # 钱包状态


class WalletDetail(db.Model):
    pass
