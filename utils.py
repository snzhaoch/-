import time


def formatted_time(time_unix):
    """
    unix 时间格式化函数
    2017/12/10 08:59:15
    """
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(time_unix)
    return time.strftime(format, value)


def log(*args, **kwargs):
    """
    log 函数，并将执行时间与参数写到 log 日志中
    """
    dt = formatted_time(int(time.time()))
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, **kwargs)
        print(dt, *args, file=f, **kwargs)
