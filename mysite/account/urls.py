# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [       
    
    url(r'', views.custom_label, name='custom_label'),  # 必须放在最后
    
    
]
