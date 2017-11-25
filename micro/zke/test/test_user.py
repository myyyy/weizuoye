# -*- coding:utf-8 -*-
import json
import urllib
import urllib2
import unittest
import cookielib
from testbase import*
HOST = 'http://localhost:9878'

class TestReg(unittest.TestCase):
    """
    使用Python自带的unittest模块，编写sort.py测试用例
    """
    # def test_post_reg(self):
    #     values={
    #     'name':'suyf',
    #     'password':'111111'
    #     }
    #     URL = HOST+'/login'
    #     values = urllib.urlencode(values)
    #     req = urllib2.Request(url = URL,data =values)
    #     response = urllib2.urlopen(req)
    #     data = json.loads(response.read())
    #     print data
    #     self.assertEquals(data.get('status',''),True)

    # def test_task(self):
    #     URL = HOST+'/coursetask'
    #     values={
    #     'courseid':'courseid',
    #     'classesid':'classesid',
    #     'title':'title',
    #     'context':'context',
    #     'videoid':'videoid'
    #     }
    #     values = urllib.urlencode(values)
    #     req = urllib2.Request(url = URL,data =values)
    #     response = urllib2.urlopen(req)
    #     data = json.loads(response.read())
    #     print data
    #     self.assertEquals(data.get('status',''),True)

    # def test_login(self):
    #     values={
    #     'name':'suyf',
    #     'password':'111111'
    #     }
    #     URL = HOST+'/login'
    #     values = urllib.urlencode(values)
    #     req = urllib2.Request(url = URL,data =values)
    #     response = urllib2.urlopen(req)
    #     data = json.loads(response.read())
    #     print data
    #     filename = 'cookie.txt'
    #     #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    #     cookie = cookielib.MozillaCookieJar(filename)
    #     #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    #     handler = urllib2.HTTPCookieProcessor(cookie)
    #     #通过handler来构建opener
    #     opener = urllib2.build_opener(handler)
    #     #创建一个请求，原理同urllib2的urlopen
    #     response = opener.open(URL,values)
    #     # response = urllib2.urlopen(req)
    #     #保存cookie到文件
    #     cookie.save(ignore_discard=True, ignore_expires=True)
    #     self.assertEquals(data.get('status',''),True)

    def test_get_users(self):
        print 'BeginTest:test_get_users.....'
        URL = HOST+'/users'
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL)
        response = opener.open(req)
        data = json.loads(response.read())
        print data['data']
        self.assertEquals(data.get('status',''),True)

    def test_post_users(self):
        print 'BeginTest:test_get_users.....'
        URL = HOST+'/users'
        values={
            'name':'suyf',
            'password':'111111'
        }
        values = urllib.urlencode(values)
        opener = get_cookie_opener('cookie.txt')
        req = urllib2.Request(url = URL,data=values)
        response = opener.open(req)
        data = json.loads(response.read())
        self.assertEquals(data.get('status',''),True)

if __name__ == '__main__':  
    unittest.main()