#-*- coding:utf-8 -*-
"""
    riddles.admin
    ~~~~~~~~~~~~~~

    riddles admin file

    :copyright: (c) 2012 by arruda.
"""
import warnings
from django.contrib import admin
from riddles.riddles.models import Riddle


#should make a better admin
warnings.warn("Make a better admin for Riddles.",SyntaxWarning)
admin.site.register(Riddle, admin.ModelAdmin)
