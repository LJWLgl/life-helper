#!/usr/bin/python
# encoding: utf-8
import json


# return 省市list
def load():
    with open("./address.json", 'r') as f:
        address = json.loads(f.read())
    return address['result']

def find(name):
    match_data = {
        'province': '',
        'city': '',
        'district': ''
    }
    provinces = load()
    for province in provinces:
        cities = province['city']
        for city in cities:
            districts = city['district']
            for district in districts:
                if district['district'] == name:
                    match_data['province'] = str(province['id'])
                    match_data['city'] = str(city['id'])
                    match_data['district'] = str(district['id'])
                    return match_data
    return None

def get_app_key(key):
    with open("./key_config.json", 'r') as f:
        key_val = json.loads(f.read())
    return key_val[key]
