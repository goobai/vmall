import multiprocessing

# 监听本机的5000端口
bind = '127.0.0.1:8000'
# 开启4个进程
workers = multiprocessing.cpu_count() * 2 + 1
# 线程
# threads=8000
keepalive = 1
# 在keep-alive连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。
daemon = True
worker_connections = 10000
# worker_connections最大客户端并发数量，默认情况下这个值为1000。此设置将影响gevent和eventlet工作模式
graceful_timeout = 0
# graceful_timeout优雅的人工超时时间，默认情况下，这个值为30。收到重启信号后，工作人员有那么多时间来完成服务请求。在超时(从接收到重启信号开始)之后仍然活着的工作将被强行杀死
limit_request_line = 8048
# limit_request_line HTTP请求行的最大大小，此参数用于限制HTTP请求行的允许大小，默认情况下，这个值为4094。值是0~8190的数字。此参数可以防止任何DDOS攻击
backlog = 8048
# 工作模式为gevent
worker_class = "egg:meinheld"
debug = True
chdir = './'
proc_name = 'gunicorn.pid'
# 记录PID
pidfile = 'debug.log'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 设置gunicorn访问日志格式，错误日志无法设置
errorlog = "./errlog"
accesslog = "./logs"
