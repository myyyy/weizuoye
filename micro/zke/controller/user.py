# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import AccessHandler
from logic.access import *



@needcheck()
class UserHandler(AccessHandler):

    def get(self):
        #获得登陆用户自己的信息
        data = User.objects(id=ObjectId(self.uid))
        self.write(dict(data=data.to_json(),status=True,msg='xxx'))

    def post(self):
        #添加用户
        user = User()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        user.modelfactory(kwargs)
        status ,msg = user.unique_save()
        self.write(dict(status=status,msg=msg))

    def put(self):
        #修改用户信息
        email = self.get_json_argument('email','')
        nickname = self.get_json_argument('nickname','')
        kwargs={}
        if email:
            kwargs['email'] = email
        if email:
            kwargs['nickname'] = nickname
        User.objects().modify(taskerid="taskerid",id=self.uid,**kwargs)
        self.write(dict(status=True,msg='update success'))

    def delete(self):
        #删除用户
        uid = self.get_json_argument('uid')
        User.objects(id=ObjectId(uid)).delete()
        self.write(dict(status=True,msg='删除成功'))

class ResetUserHandler(AccessHandler):
    def put(self):
        #修改用户密码
        password =self.get_json_argument('password','')
        oldpassword =self.get_json_argument('oldpassword','')
        password =  hashlib.md5(kwargs.get('password','')).hexdigest()
        oldpassword =  hashlib.md5(kwargs.get('oldpassword','')).hexdigest()
        user = User.objects(id=self.uid,password=password).first()
        if user:
            User.objects(id=self.uid).modify(**{'password':oldpassword})
            status,msg=True,'修改用戶密碼成功'
        else:
            status,msg=True,'用戶信息验证失败'
        self.write(dict(status=status,msg=msg))
