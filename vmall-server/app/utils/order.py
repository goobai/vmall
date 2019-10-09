from app import redis_client
from flask import current_app
import random
import logging


def generate_order_id(uid, **kwargs):
    """
    sn(10位) +machineId+ uId
    自增id +redis设备号2位 用户id后2位。用户id，redis设备id不足2位时用0在左边补齐
    :param kwargs:  uid
    :return: order ID
    """
    try:
        machine_id = redis_client.get('machine:id')
        if not 0 < int(machine_id) < 100:
            logging.error("Redis machine id 设置错误：不在0-99之间.当前 machine id: %s", machine_id)
            return None
        if not uid or not isinstance(uid, int) or uid < 1:
            logging.error("uid非法： %s", uid)
            return None
        else:
            uid = str(uid).zfill(2)[-2:]
            machine_id = str(machine_id).zfill(2)[-2:]
            sn = redis_client.incrby('order:amount', 1)
            return sn * 10000 + int(machine_id) * 100 + int(uid)
    except Exception as e:
        logging.error("订单id生成错误，错误信息： %s", e)
        return None


def gen_id():
    pools = current_app.id_pool
    if isinstance(pools, list) and len(pools) > 0:
        rad = random.choice(pools)
        current_app.id_pool.remove(rad)
        return rad
    else:
        retry = 3
        while retry:
            id_list(10)
            pools = current_app.id_pool
            if isinstance(pools, list) and len(pools) > 0:
                rad = random.choice(pools)
                current_app.id_pool.remove(rad)
                return rad
            else:
                retry = retry - 1
        return None


def id_list(step):
    try:
        redis_client.setnx('order:maxId', 0)
        max_id = redis_client.incrby('order:maxId', step)
        current_app.id_pool = [x for x in range(max_id - step, max_id)]
    except Exception as e:
        logging.error(e)


def cache1redis(key, value):
    redis_client.set(key, value)


def get4cache(key):
    if isinstance(key, (str, int)):
        data = redis_client.get(key)
        return data
    else:
        return None
