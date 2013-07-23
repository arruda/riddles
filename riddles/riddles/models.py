# -*- coding: utf-8 -*-
"""
    riddles.models
    ~~~~~~~~~~~~~~

    riddles models file

    :copyright: (c) 2012 by arruda.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Riddle(models.Model):
    """
    Riddle model
    """

    content = models.CharField(_("Content"), max_length=250)
    answer = models.CharField(_("Answer"), max_length=250)

    class Meta:
        app_label = 'riddles'

    def __unicode__(self):
        return self.content


class Guess(models.Model):
    """
    A Guess in a riddle.
    If the guess's answer is equal to the Riddle answer than it's correct.
    """
    answer = models.CharField(_("Guess"), max_length=250)
