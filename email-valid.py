#!/usr/bin/python

import re
email='pepito@example.mc'
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
myre = re.compile(EMAIL_REGEX)
emailfound=myre.findall(email)
if email == '':
  print('invalid')
  exit()
  #return
elif emailfound == []:
  print('invalid')
  print(email)
  exit()
elif emailfound[0] == email:
  print('valid')
  print(email)
else:
  print('invalid')
  print(email)
