#!/usr/bin/python
# encoding: utf-8

def dict_to_get_params(_dict):
    x = ""
    for key, val in _dict.items():
        x += "%s=%s&" % (key, val)
    return x[:-1]
