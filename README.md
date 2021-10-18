# Coding challenge for UN-ICC

Basically a JSON REDO log for notifications (rest of specifications in PDF provided CI-Codingchallenge-051021-1338.pdf)

### How to setup and run the App:
Main dependencies:
- Linux
- Python 2.7.9
- ijson 3.1.4

````
curl https://raw.githubusercontent.com/jauselmor/coding-challenge/main/send_notifications.py --output send_notifications.py
curl https://raw.githubusercontent.com/jauselmor/coding-challenge/main/validators.py --output validators.py
sudo pip install ijson
python send_notifications.py
````


###Design highlevel overview::
* Fetch JSON file (https://github.com/UN-ICC/notifications-processor/blob/master/notifications_log.json) 
* Read contacts and identify type of the notification 
* Identify if mandatory parameters are present and usable. We consider:
  - Valid emails match with a regex and not missing or null.
  - Phone numbers and url only invalids if missing or null.    
* Call the right function depends on the type of notification.

### Implementation and challenge goals
- Mandatory parameters are present and are not null: see functions, precheck_send_sms, precheck_send_phone, precheck_send_url. And file [validators](./validators.py).
- You should write mock functions that send email, sms and post requests: Done, with a sleep to simulate the real behaviour. 
- You need to assume that the JSON file can have thousand or million of entries: We tried to improve the performance using multiprocessing and that is why exists the file [send_notifications_multiprocesing.py](./send_notifications_multiprocesing.py) but hadn't a significant improvement (saved 5% of the time aprox.). I have no time to redesign the project, but as TO DO we could implement a solution using Celery (https://docs.celeryproject.org/en/stable/).  
- Relevant third party libraries: Used ijson to manage big json data files.
- Commits documented to see how the code evolve: until now 17 commits. 
- No coding patters used, no enough experience in that field, but tried to create appropriate functions to help to read the code. Main script [send_notifications.py](./send_notifications.py) has less than 100 hundred lines. 
- Logging. Line with message of ERROR if message can't be send because data is wrong or missing, and line with message indicating the action:
Example:
````
('EMAIL sent to christopher93@example.net', '. Data:', [(u'url', u'http://fernandez.info/'), (u'phone', u'+1-152-084-6860x0958'), (u'type', u'email'), (u'name', u'Jasmine Anderson'), (u'email', u'christopher93@example.net')])
2021-10-18 00:29:54,564 - __main__ - ERROR - [(u'url', None), (u'phone', None), (u'type', u'post'), (u'name', u'Matthew Schwartz'), (u'email', u'geoffrey45@example.net')]


 
