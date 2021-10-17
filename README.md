# Coding challenge for UN-ICC

Basically a JSON REDO log for notifications (rest of specifications in PDF provided CI-Codingchallenge-051021-1338.pdf)

First idea will be:
* Fetch JSON file (https://github.com/UN-ICC/notifications-processor/blob/master/notifications_log.json) 
* Read contacts and identify type of the notification 
* Identify if mandatory parameters are present and usable. We consider:
  - Valid emails match with a regex and not missing or null.
  - Phone numbers and url only invalids if missing or null.    
* Call the right function depends on the type of notification. 

----
 
