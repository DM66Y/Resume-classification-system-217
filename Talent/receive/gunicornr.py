# encoding:utf-8
#并行工作线程数
workers = 1
#监听端口
bind = '0.0.0.0:8080'
#设置守护进程【关闭连接时，程序仍在运行】
daemon = True
#设置超时时间120s
timeout = 120
# 设置访问日志和错误信息日志路径
pidfile = './gunicornr_logs/gunicornr.pid'
accesslog = './gunicornr_logs/accessr.log'
errorlog = './gunicornr_logs/errorr.log'
