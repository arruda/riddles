# -*- coding: utf-8 -*-

from riddles.riddles.models import Riddle

def run():
    print "Adding initial Riddles data"
    NUM_RIDDLES = 50
    for i in xrange(NUM_RIDDLES):
        riddle = Riddle()
        riddle.content = "content %d" %i
        riddle.answer = "answer %d" %i
        riddle.save()
