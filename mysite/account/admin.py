# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Poem


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):    
    list_display = ('id','title','author')

