#-*- coding:utf-8 -*-
"""
    riddles.admin
    ~~~~~~~~~~~~~~

    riddles admin file

    :copyright: (c) 2012 by arruda.
"""
from django.contrib import admin
from riddles.riddles.models import Riddle



admin.site.register(Riddle, admin.ModelAdmin)
