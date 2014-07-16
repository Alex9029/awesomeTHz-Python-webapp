#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test db.
'''
__author__ = 'Chalex'


from models import User, Blog, Comment
from transwarp import db

db.create_engine(user='root', password='password', database='awesome')

u = User(name='TTest', email='test@example.com.cn', password='9876543210', image='about: blank')

u.insert()

print 'new user id: ', u.id

u1 = User.find_first('where email=?', 'test@example.com.cn')
print 'find user\'s name: ', u1.name

u1.delete()

u2 = User.find_first('where email=?', 'test@example.com.cn')
print 'find user: ', u2