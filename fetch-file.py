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
from collections import Counter

#url1=sys.argv[1]
url1='https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'

response1=urlopen(url1).read()

objects=ijson.items(response1,'')
people=(o for o in objects )
for person in people:
 peopleNum=len(person)
 for i in range(peopleNum):
  #print(person[i])
  person_items = person[i].items()
  for k,v in person_items:
      if k == 'type':
        if v == 'email':
         print('send_email to:')
         print(person_items)
        elif v == 'post':
         print('send_post to:')
         print(person_items)
        elif v == 'sms':
         print('send_sms to:')
         print(person_items)
        else:
         print('no valid send type:')
         print(person_items)


#print(type(person))
