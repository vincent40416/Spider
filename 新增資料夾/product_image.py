# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:54:28 2018

@author: rusty
"""

import json
import requests
import time
itemId = '1m1t58k'


try:
    my_url = "http://shop.mogujie.com/ajax/mgj.pc.detailinfo/v1?itemId="+ itemId
    req = requests.get(my_url) 
    print(req.status_code)
    req.encoding = 'utf-8'
    jsonfile = json.loads(req.text)
    
    for img in jsonfile['data']['detailInfos']['detailImage'][0]['list']:
        print(img)  #item image
         
       
except requests.RequestException as e:
       print(e)