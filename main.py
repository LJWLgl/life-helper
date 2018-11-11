#!/usr/bin/python
# encoding: utf-8
import juhe_api
from workflow import Workflow

select_type = {
    'wx': 'weixin_selected',
    'joke': 'joke_content'
}


def tip():
    item = {
        'title': u'显示所有功能',
        'subtitle': u'输入enter键',
        'url': '',
        'arg': '',
        'icon': '',
        'valid': True
    }
    return [item]



def main(wf):
    command = wf.args[0]
    type = wf.args[1] if len(wf.args) > 1 else None
    choose = select_type.get(command)
    data = []
    if choose is None or len(choose) < 2:
        data = tip()
    if choose is 'weixin_selected':
        data = juhe_api.weixin_selected()
    if choose is 'joke_content':
        data = juhe_api.joke_content()

    for item in data:
        wf.add_item(title=item['title'],
                    subtitle=item['subtitle'],
                    arg=item['url'],
                    valid=item['valid'],
                    icon=item['icon'])
    wf.send_feedback()


if __name__ == '__main__':
    Workflow().run(main)
