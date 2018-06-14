
#!/usr/bin/env python

import sys
sys.path.append('../lib')

from facebook import FacebookClient

client = FacebookClient()
res = client.login("thangmeo2020@gmail.com", "@123456@")
      
print res