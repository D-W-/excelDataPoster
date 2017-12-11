#!/usr/bin/env python
#-*- coding: gb2312 -*-

__author__ = "Harry Wang"
__date__ = "2017/12/11"

import urllib
import cookielib
import requests
import pickle
import re

class WebContent():
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36',
                        'origin': 'http://tsglxt.cic.tsinghua.edu.cn',
                        'referer': 'http://tsglxt.cic.tsinghua.edu.cn/tsbx.tsdjb.do?m=add'}



def run(bookName, ISBN, price):
    req = WebContent('http://tsglxt.cic.tsinghua.edu.cn/tsbx.tsdjb.do?m=add')
    rawCookies = '_ga=GA1.3.951955535.1496913629; JSESSIONID=bac5zjAbug-U7ft1wqfbw; thuwebcookie=1208250122.20480.0000'
    cookies = {}
    for line in rawCookies.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    session = requests.session()
    session.headers = req.headers
    r = session.get(req.url, cookies=cookies)
    # print r.content

    data = {}
    # rawData = "m:delete;p_id:35675"
    rawData = "m:saveAdd;p_czkf:0;p_tsdjr:2016213574;p_tsdjrxm:%CD%F5%EA%CF;p_djrq:2017-12-11;p_djh:35679;p_yxmc:%C8%ED%BC%FE%D1%A7%D4%BA;p_tsbgr:2016990004;p_grj:101.1;p_sm:%D3%CE%CF%B7%D2%FD%C7%E6%BC%DC%B9%B9;p_sl:1;p_jfly:985%BE%AD%B7%D1;p_gzrq:2017-12-11;p_zllx:%D3%A1%CB%A2%C6%B7;p_isbn:9787121222887"
    for line in rawData.split(';'):
        key, value = line.split(':', 1)
        data[key] = value


    # print r.content

    pattern = 'name="token" value="([^"]+)'
    results = re.findall(pattern, r.content)[0]
    data['token'] = results

    pattern = 'name="p_djh" value="([^"]+)'
    results = re.findall(pattern, r.content)[0]
    data['p_djh'] = results

    data['p_jfly'] = '985经费'
    data['p_sm'] = bookName
    data['p_isbn'] = ISBN
    data['p_grj'] = price
    data['p_tsdjrxm'] = "王晗"
    data['p_yxmc'] = "软件学院"
    data['p_zllx'] = "印刷品"
    # print results


    req = WebContent('http://tsglxt.cic.tsinghua.edu.cn/tsbx.tsdjb.do')

    session = requests.session()
    session.headers = req.headers
    r = session.post(req.url, data=data, cookies=cookies)

    # print r.content


    # save_cookies(cookies)

# if __name__ == '__main__':
#     # main()