#!/usr/bin/python

######
# Usage:
#       ./send_notifications_multiprocessing.py
#
######

import re
import sys
import urllib
from urllib import urlopen
import ijson
from validators import email_validator, url_validator, phone_validator
import logging
from time import time, sleep
import multiprocessing

# def send_sms(phone: str, data: dict) -> None:
def send_sms(phone, data):
    sleep(0.3) #To simulate delay in function
    print("SMS sent to " + str(phone) , ". Data:", data)
#def send_email(email: str, data: dict) -> None:
def send_email(email, data):
    sleep(0.1) #To simulate delay in function
    print("EMAIL sent to " + str(email),". Data:", data)
#def send_post(url: str, data: dict) -> None:
def send_post(url, data):
    sleep(0.2) #To simulate delay in function
    print("POST sent to " + str(url),". Data:", data)

def precheck_send_sms(phone, name):
    # Check if:
    # - mandatory parameters are present (name, phone)
    # - phone is present and format is correct.
    if name == '':
        return False
    else:
        return phone_validator(phone)

def precheck_send_email(email, name):
    # Check if:
    # - mandatory parameters are present (name, email)
    # - email is present and format is correct.
    #print("EMAIL sent to " + str(email),". Data:", data)
    if name == '':
        return False
    else:
        return email_validator(email)

def precheck_send_post(url, name):
    # Check if:
    # - mandatory parameters are present (name, url)
    # - url is present and format is correct.
    if name == '':
        return False
    else:
        return url_validator(url)


def worker(threadId, peopleNum, totalProcesses, person):
   for i in range(threadId, peopleNum, totalProcesses):
        person_items = person[i].items()
        url=person_items[0][1]
        phone=person_items[1][1]
        name=person_items[3][1]
        email=person_items[4][1]
        for k,v in person_items:
            if k == 'type':
              if v == 'email':
               if precheck_send_email(email, name):
                  send_email(email, person_items)
               else:
                  logger.error(person_items)
              elif v == 'post':
               if precheck_send_post(url, name):
                  send_post(url, person_items)
               else:
                  logger.error(person_items)
              elif v == 'sms':
               if precheck_send_sms(phone, name):
                  send_sms(person_items[1][1], person_items)
               else:
                   logger.error(person_items)
              else:
               print('no valid send type:')

##########################

# For multiprocessing
totalProcesses=8

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
ts = time()

# Hardcoded source url to download the json
url1='https://raw.githubusercontent.com/UN-ICC/notifications-processor/master/notifications_log.json'

response1=urlopen(url1).read()

objects=ijson.items(response1,'')
people=(o for o in objects )
for person in people:
 peopleNum=len(person)

processes = []
for i in range(totalProcesses):
    processes = multiprocessing.Process(target=worker(i, peopleNum, totalProcesses, person))
    processes.start()
    processes.join()

logging.info('Took %s seconds', time() - ts)

