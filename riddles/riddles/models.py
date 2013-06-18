# -*- coding: utf-8 -*-
"""
    riddles.models
    ~~~~~~~~~~~~~~

    riddles models file

    :copyright: (c) 2012 by arruda.
"""

from django.db import models

class Riddle(models.Model):
    """
    Riddle model
	"""

    class Meta:
        app_label = 'riddles'
