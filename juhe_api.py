#!/usr/bin/python
# encoding: utf-8

import json
import time

import file_utils
import utils
import requests


# 微信精选
def weixin_selected():
    try:
        params = {
            'key': file_utils.get_app_key(u'wx_key'),
        }
        url = 'http://v.juhe.cn/weixin/query?{}'.format(utils.dict_to_get_params(params))
        res = requests.get(url)
        data = json.loads(res.text)
        list = data['result']['list']
        resultList = []
        for item in list:
            resitem = {
                'title': item['title'],
                'subtitle': item['source'],
                'url': item['url'],
                'arg': item['url'],
                'icon': 'img/wechat.png',
                'valid': True
            }
            resultList.append(resitem)
        return resultList
    except Exception, e:
        print e
        return []


# 新闻
def news(type=None):
    p_type = type if type is not None else 'top'
    params = {
        'key': file_utils.get_app_key(u'news_key'),
        'type': p_type
    }
    url = 'http://v.juhe.cn/toutiao/index?{}'.format(utils.dict_to_get_params(params))
    result_list = []
    try:
        res = requests.get(url)
        data = json.loads(res.text)
        list = data['result']['data']
        for item in list:
            res_item = {
                'title': item['title'],
                'subtitle': u'《{}》  {}'.format(item['author_name'], item['title']),
                'url': item['url'],
                'arg': item['url'],
                'icon': 'img/news.png',
                'valid': True
            }
            result_list.append(res_item)
        return result_list
    except Exception, e:
        print e
        return []


# IP地址查询
def ip_query(ip):
    if ip is None or not utils.is_ipv4_addr(ip):
        return error_tip(u'ip地址为空或者格式错误')
    params = {
        'key': file_utils.get_app_key(u'ip_key'),
        'ip': ip
    }
    url = 'http://apis.juhe.cn/ip/ip2addr?{}'.format(utils.dict_to_get_params(params))
    try:
        res = requests.get(url)
        data = json.loads(res.text)['result']
        res_item = {
            'title': data['area'],
            'subtitle': data['location'],
            'url': '',
            'arg': data['area'],
            'icon': 'img/ip.png',
            'valid': True
        }
        return [res_item]
    except Exception, e:
        print e
        return []


# 笑话大全
def joke_content():
    try:
        params = {
            'sort': 'desc',
            'page': '1',
            'pagesize': '20',
            'time': str(int(time.time())),
            'key': file_utils.get_app_key(u'joke_key')
        }
        url = 'http://v.juhe.cn/joke/content/list.php?{}'.format(utils.dict_to_get_params(params))
        res = requests.get(url)
        data = json.loads(res.text)
        result_list = []
        for item in data['result']['data']:
            res_item = {
                'title': item['content'],
                'subtitle': item['updatetime'] + '   ' + u'按cmd复制笑话',
                'url': '',
                'arg': item['content'],
                'icon': 'img/joke.png',
                'valid': True
            }
            result_list.append(res_item)
        return result_list
    except Exception, e:
        print e
        return []

# 邮编
def postcode(name):
    try:
        address_ids = file_utils.find(name)
        if address_ids is None:
            return error_tip(u'未查到到地址，请确保以县或区结尾')
        params = {
            'key': file_utils.get_app_key(u'yb_key'),
            'pid': address_ids['province'],
            'cid': address_ids['city'],
            'did': address_ids['district'],
            'page': 1,
            'pagesize': 1,
        }
        url = 'http://v.juhe.cn/postcode/search?{}'.format(utils.dict_to_get_params(params))
        res = requests.get(url)
        data = json.loads(res.text)
        result_list = []
        for item in data['result']['list']:
            res_item = {
                'title': u'邮编： ' + item['PostNumber'],
                'subtitle': u' ' + item['Province'] + ' ' + item['City'] + ' ' + item['District'],
                'url': '',
                'arg': item['PostNumber'],
                'icon': 'img/yb.png',
                'valid': True
            }
            result_list.append(res_item)
        return result_list
    except Exception, e:
        print e
        return []

# 手机号归属地
def phone_addr(phone_number):
    try:
        if len(phone_number) != 7 and len(phone_number) != 11:
            return error_tip(u'手机号位数错误，请确保是11位数字')
        params = {
            'key': file_utils.get_app_key(u'gsd_key'),
            'phone': phone_number,
        }
        url = 'http://apis.juhe.cn/mobile/get?{}'.format(utils.dict_to_get_params(params))
        res = requests.get(url)
        data = json.loads(res.text)['result']
        res_item = {
            'title': u'' + data['province'] + '  ' + data['company'],
            'subtitle': u'上海区号：' + data['areacode'] ,
            'url': '',
            'arg': u'' + data['province'] + '  ' + data['company'],
            'icon': 'img/gsd.png',
            'valid': True
        }
        return [res_item]
    except Exception, e:
        print e
        return []

def error_tip(info):
    item = {
        'title': info,
        'subtitle': u'查看说明：https://github.com/LJWLgl/life-helper',
        'url': u'https://github.com/LJWLgl/life-helper',
        'arg': '',
        'icon': '',
        'valid': True
    }
    return [item]