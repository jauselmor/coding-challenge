#!/usr/bin/python

import re
from urlparse import urlparse

def email_validator(email):
    #email='pepito@example.mc'
    EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    myre = re.compile(EMAIL_REGEX)
    try:
        emailfound=myre.findall(email)
        if email == '':
          #print('invalid')
          #exit()
          return False
        elif emailfound == []:
          #print('invalid')
          #print(email)
          #exit()
          return False
        elif emailfound[0] == email:
          #print('valid')
          #print(email)
          return True
        else:
          #print('invalid')
          #print(email)
          return False
    except:
        return False
def phone_validator(phone):
## Too much simple but according the data provided, there are many formats of phone numbers in the list and I think is not required to lose too much time on it.
    if phone != None:
      return True
    else:
      return False

def url_validator(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False