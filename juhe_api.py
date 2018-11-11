#!/usr/bin/python
# encoding: utf-8

import json
import time
import utils
import requests


# 微信精选
def weixin_selected():
    try:
        res = requests.get('http://v.juhe.cn/weixin/query?key=040e9450449b863120f2522e534711f6')
        data = json.loads(res.text)
        list = data['result']['list']
        resultList = []
        for item in list:
            resitem = {
                'title': item['title'],
                'subtitle': item['source'],
                'url': item['url'],
                'arg': item['url'],
                'icon': '',
                'valid': True
            }
            resultList.append(resitem)
        return resultList
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
            'key': '1728f759f17a3c12c243cb957444d6a4'
        }
        url = 'http://v.juhe.cn/joke/content/list.php?{}'.format(utils.dict_to_get_params(params))
        res = requests.get(url)
        data = json.loads(res.text)
        list = data['result']['data']
        resultList = []
        for item in list:
            resitem = {
                'title': item['content'],
                'subtitle': item['updatetime'],
                'url': '',
                'arg': '',
                'icon': '',
                'valid': True
            }
            resultList.append(resitem)
        return resultList
    except Exception, e:
        print e
        return []
