#!/usr/bin/python
# encoding: utf-8
import juhe_api
import utils
from workflow import Workflow

select_type = {
    'wx': 'weixin_selected',
    'joke': 'joke_content',
    'news': 'news',
    'ip': 'ip_query',
    'yb': 'postcode',
    'gsd': 'phone_addr',
    'config': 'open_config',
}

def config_tip():
    item = {
        'title': u'输入enter打开配置',
        'subtitle': '',
        'url': '',
        'arg': u'config',
        'icon': '',
        'valid': True
    }
    return [item]

def tip():
    item = {
        'title': u'输入enter查看所有命令',
        'subtitle': u'https://github.com/LJWLgl/life-helper',
        'url': u'https://github.com/LJWLgl/life-helper',
        'arg': '',
        'icon': '',
        'valid': True
    }
    return [item]


def xml(wf, data):
    for item in data:
        wf.add_item(title=item['title'],
                    subtitle=item['subtitle'],
                    arg=item['arg'],
                    valid=item['valid'],
                    icon=item['icon'])
    wf.send_feedback()


def main(wf):
    arg1 = wf.args[0]
    arg2 = wf.args[1] if len(wf.args) > 1 else None
    if arg1 is None or not utils.check_params(arg1, arg2):
        return xml(wf, tip())

    choose = select_type.get(arg1)
    data = []
    if choose is 'weixin_selected':
        data = juhe_api.weixin_selected()
    if choose is 'joke_content':
        data = juhe_api.joke_content()
    if choose is 'news':
        data = juhe_api.news(arg2)
    if choose is 'ip_query':
        data = juhe_api.ip_query(arg2)
    if choose is 'postcode':
        data = juhe_api.postcode(arg2)
    if choose is 'phone_addr':
        data = juhe_api.phone_addr(arg2)
    if choose is 'open_config':
        data = config_tip()
    return xml(wf, data)


if __name__ == '__main__':
    Workflow().run(main)
