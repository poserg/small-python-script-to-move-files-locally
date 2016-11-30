#!/usr/bin/env python

from sys import argv
from dirsync import sync

t=sync(argv[1], argv[2], 'diff', create=True, only=('^.*\.html$',))

