# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse
from django.contrib.auth.decorators import login_required #使用注意在settings.py中设置 LOGIN_URL = '/login/'
from django.utils.safestring import mark_safe

# http://localhost:8000/
#@login_required
def index(request):           
    meg = 'hello world! '
    return render(request, 'account/index.html', context=locals()) 

# Create your views here.
def custom_label(request):
    return render(request, 'account/custom_label.html', context=locals())
