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

# def send_sms(phone: str, data: dict) -> None:
def send_sms(phone, data):
    print("SMS sent to " + str(phone) , ". Data:", data)
#def send_email(email: str, data: dict) -> None:
def send_email(email, data):
    print("EMAIL sent to " + str(email),". Data:", data)
#def send_post(url: str, data: dict) -> None:
def send_post(url, data):
    print("POST sent to " + str(url),". Data:", data)

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
         #print('send_email to:')
         #print(person_items[4][1])
         send_email(person_items[4][1], person_items)
        elif v == 'post':
         #print('send_post to:')
         #print(person_items[0])
         send_post(person_items[0][1], person_items)
        elif v == 'sms':
         #print('send_sms to:')
         #print(person_items[1])
         #print(person_items)
         send_sms(person_items[1][1], person_items)
        else:
         print('no valid send type:')
         #print(person_items)


#print(type(person))
