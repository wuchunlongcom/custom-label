# -*- coding: UTF-8 -*-
import os
import sys
import django
import random

print('python 版本: %s。\ndjango版本: %s。'%(sys.version, django.get_version()))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission
    from account.models import  Poem
    
    if not User.objects.filter(username = 'admin'):
        User.objects.create_superuser('admin', 'admin@test.com','admin')     

    
    #test 默认  user.is_staff = False  user.is_superuser = False  不能从后台登录
    User.objects.create_user('test', 'test@test.com','1234qazx') 
    
    #test1 不能从后台登录
    user = User.objects.create_user('test1', 'test1@test.com','1234qazx')
    user.user_permissions.add(Permission.objects.get(name='Can add poem'),\
                              Permission.objects.get(name='Can change poem'),\
                              Permission.objects.get(name='Can delete poem')) #添加权限  
    user.is_staff = True
    user.is_superuser = False  #不能从后台登录
    user.save()
    
    user = User.objects.create_user('wcl6005', 'wcl6005@test.com','1234qazx')   
    user.is_staff = True
    user.is_superuser = True  #能从后台登录,实测对数据库有增删改权限
    user.save()
      
    titles = ['静夜思','送友人','早发白帝城','峨眉山月歌']
    for title in titles:
        Poem.objects.create(author = '李白', title = title)

        

