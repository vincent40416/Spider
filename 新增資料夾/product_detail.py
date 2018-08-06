# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:37:50 2018

@author: rusty
"""

#  http://www.mogujie.com/
from bs4 import BeautifulSoup
import json
import requests
import time

#time test
#start_time = time.time()
itemId = '1m1t58k'
headers = {
           'content-type' : 'application/x-www-form-urlencoded',
           'accept': 'application/json'
           }

try:
    my_url = "http://shop.mogujie.com/detail/"+itemId
    req = requests.get(my_url) 
    print(req.status_code)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')
    name = soup.find('span', itemprop='name').text  # product name
    
    promo_price = soup.find('dd',"property-cont property-cont-origin").find('span','price').text 
    price = soup.find('dd',"property-cont property-cont-now fl").find('span',"price").text
    
        
    print(name)
    
    print(promo_price,price)

#    
#           
       
except requests.RequestException as e:
       print(e)


#elapsed_time = time.time() - start_time
#print (elapsed_time)