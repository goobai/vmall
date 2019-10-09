# from multiprocessing import Process
# # import os
# # from concurrent.futures import ProcessPoolExecutor
# #
# #
# # def info(title):
# #     print(title)
# #     print('module name:', __name__)
# #     print('parent process:', os.getppid())
# #     print('process id:', os.getpid())
# #
# #
# # def f(name):
# #     info('function f')
# #     print('hello', name)
# #
# #
# # if __name__ == '__main__':
# #     info('main line')
# #     p = Process(target=f, args=('bob',))
# #     p.start()
# #     p.join()
# from multiprocessing import Process, Pool
# import os
# import time
#
#
# def work(name):
#     print('task %s run ' % name)
#     print('task %s finished' % name)
#     print(" pid :%s ,ppid:%s" % (os.getpid(), os.getppid()))
#
#
# if __name__ == '__main__':
#     procespool = Pool(os.cpu_count())
#     t1 = time.time()
#     for p in range(1000):
#         procespool.apply_async(work, args=(p,))
#     procespool.close()
#     procespool.join()
#     print(time.time() - t1)
from datetime import datetime

print(datetime.utcnow())
# if (1):
#     print('True')
#
# plus = lambda x, y: x + y
#
# print(plus(1, 3))
import sys, os
from sys import argv, modules, path
import pprint, time
import multiprocessing

print(os.getcwd())
pprint.pprint(sys.platform)
print(os.path.abspath(os.getcwd()))

import pymysql.cursors
from urllib.parse import urlparse

# URI = 'mysql+pymysql://mysql:Goobai!1@192.168.16.129/aipycms?charset=utf8'
URI = 'mysql+pymysql://mysql:Goobai!1@localhost/aipycms?charset=utf8'

URL_CONFIG = urlparse(URI)


def call_proc(db, sql, params):
    cur = db.cursor()
    t1 = time.time()
    for i in range(200):
        res = cur.execute(sql, args=params)
    db.commit()
    t2 = time.time()
    print('call proc time: ', t2 - t1)
    cur.close()
    db.close()


def inster_cart(db, sql, params=""):
    cur = db.cursor()
    t1 = time.time()
    for i in range(50000):
        res = cur.execute(sql,
                          args=(i, i, 1, i, 1, datetime.utcnow()))
    db.commit()
    t2 = time.time()
    print('call proc time: ', t2 - t1)


def sql_pool():
    db = pymysql.connect(
        host=URL_CONFIG.hostname,
        port=URL_CONFIG.port,
        user=URL_CONFIG.username,
        password=URL_CONFIG.password,
        db=URL_CONFIG.path[1:],
        cursorclass=pymysql.cursors.DictCursor
    )
    sql = "call initcart(%s)"
    params = (2,)
    call_proc(db, sql, params)
    # sql = '''INSERT
    # INTO
    # cart(cart.sku_id, cart.user_id, cart.shop_id, cart.count, cart.checked, cart.modify_time) VALUES(%s,%s,%s,%s,%s,%s)'''
    # params = ""
    # inster_cart(db, sql)
    # cur = db.cursor()
    # t1 = time.time()
    # for x in range(50000):
    #     res = cur.execute('INSERT into  article (author_id,title,content) VALUES(%s,%s,%s)',
    #                       args=('4', '测试mysql', 'mysql 是一个性能强悍的数据存储软件'))
    # db.commit()
    # t2 = time.time()
    # for x in range(10000):
    #     cur.execute('select id ,title ,content from article where id=%s', args=(4))
    #     data = cur.fetchone()
    # t3 = time.time()
    # print('insert time: ', t2 - t1, '; query time :', t3 - t2)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=5)  # 创建5个进程
    for i in range(5):
        pool.apply_async(sql_pool)
    pool.close()  # 关闭进程池，表示不能在往进程池中添加进程
    pool.join()  # 等待进程池中的所有进程执行完毕，必须在close()之后调用
