# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:19:35 2018

@author: rusty
"""
#  http://www.mogujie.com/
import json
import requests
import time
query= u'長褲'
page = 1
headers = {
           'content-type' : 'application/x-www-form-urlencoded',
           'accept': 'application/json'
           }

try:
    my_url = "http://list.mogujie.com/search?&cKey=43&page="+str(page)+"&q="+ query +"&minPrice=&maxPrice="
    req = requests.get(my_url) 
    print(req.status_code)
    req.encoding = 'utf-8'
    jsonfile = json.loads(req.text)
#    print(jsonfile['result']['wall']['docs'])
    for item in jsonfile['result']['wall']['docs']:
        print(item['tradeItemId'],item['title'],item['orgPrice'],item['price'],item['img'])
#    
#           
       
except requests.RequestException as e:
       print(e)