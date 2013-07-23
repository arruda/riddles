# -*- coding: utf-8 -*-

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--rednose','--testmatch=^test','--exclude-dir-file=nose_exclude.txt','-s',]
