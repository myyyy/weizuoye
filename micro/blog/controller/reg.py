# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from model import Assignment as ag
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class RegHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        st = ag.User()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        kwargs['password']  =  hashlib.md5(kwargs.get('password','')).hexdigest()
        st.modelfactory(kwargs)
        status ,msg = st.unique_save()
        self.write(dict(status=status,msg=msg))

