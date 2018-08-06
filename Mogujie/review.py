# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:03:52 2018

@author: rusty
"""

import json
import requests
import time
itemId = '1m1t58k'
headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
           'Referer':'http://shop.mogujie.com/detail/1m1t58k?acm=3.ms.1_4_1m1t58k.43.1185-71198-68998.6JN5HqYJ1H8ND.sd_117-swt_43-imt_6-t_6JN5HqYJ1H8ND-lc_4-qid_88084-dit_19-idx_0-dm1_5001&ptp=1.eW5XD.0.0.HTwJydSH',
           'content-type' : 'application/x-www-form-urlencoded',
           'accept': 'application/json',
           }

try:
    my_url = "http://rate.mogujie.com/jsonp/pc.rate.ratelist/v2?itemId="+itemId
    req = requests.get(my_url,headers = headers) 
    print(req.status_code)
    req.encoding = 'utf-8'
    content = req.text[5:].strip().rstrip(')')
    jsonfile = json.loads(content)
    print(jsonfile['data']['averageScore'])    # Score
    
    for comment in jsonfile['data']['list']:
        print (comment['rateId'],comment['time'],comment['content'])  # comment
        for image in comment['images']:
            print(image)
#    
#    for img in jsonfile['data']['detailInfos']['detailImage'][0]['list']:
#        print(img)  #item image
#         
       
except requests.RequestException as e:
       print(e)