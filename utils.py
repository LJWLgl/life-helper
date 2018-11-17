#!/usr/bin/python
# encoding: utf-8

def dict_to_get_params(_dict):
    x = ""
    for key, val in _dict.items():
        x += "%s=%s&" % (key, val)
    return x[:-1]


commands = {
    'wx': [],
    'joke': [],
    'news': [
        'top',
        'shehui',
        'guonei',
        'guoji',
        'yule',
        'tiyu',
        'junshi',
        'keji',
        'caijing',
        'shishang',
    ],
    'ip': [],
    'yb': [],
    'gsd': [],
    'config': []
}


def check_params(arg1, arg2=None):
    list = commands.get(arg1)
    if commands.get(arg1) is None:
        return False
    if len(list) == 0:
        return True
    if arg2 is None:
        return False
    if index(list, arg2) is -1:
        return False
    return True


def index(list, value):
    try:
        return list.index(value)
    except Exception, e:
        print e
        return -1

# 判断Ip是否合法
def is_ipv4_addr(ipStr):
    # 切割IP地址为一个列表
    ip_split_list = ipStr.strip().split('.')
    # 切割后列表必须有4个元素
    if 4 != len(ip_split_list):
        return False
    for i in range(4):
        try:
            # 每个元素必须为数字
            ip_split_list[i] = int(ip_split_list[i])
        except:
            print("IP invalid:" + ipStr)
            return False
    for i in range(4):
        # 每个元素值必须在0-255之间
        if ip_split_list[i] <= 255 and ip_split_list[i] >= 0:
            pass
        else:
            print("IP invalid:" + ipStr)
            return False
    return True


if __name__ == '__main__':
    print is_ipv4_addr('32.54')


