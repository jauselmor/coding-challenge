#!/usr/bin/python

######
# Usage:
#       ./fetch-file.py
#
######

import re
import sys
import urllib
from urllib import urlopen
import ijson

#url1=sys.argv[1]
url1='https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'

response1=urlopen(url1).read()

objects=ijson.items(response1,'')
people= (o for o in objects )
for person in people:
 print(person[10])