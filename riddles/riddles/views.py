# -*- coding: utf-8 -*-
"""
    riddles.views
    ~~~~~~~~~~~~~~

    riddles views file
    
    :copyright: (c) 2012 by arruda.
"""
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to


