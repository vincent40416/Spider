# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 00:06:47 2018

@author: rusty
"""
#  https://www.hktvmall.com/
import json
import requests
import time

#time test
#start_time = time.time()


# search with certain query
query= u'洗髮乳'
my_url ='https://8rn1y79f02-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%203.29.0&x-algolia-application-id=8RN1Y79F02&x-algolia-api-key=4819ab3e709be2e853154599a364464a'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
page = 0
value= {"requests":[{
        "indexName":"hktvProduct",
        "params":"query="+ query +
        "&filters=&facets=%5B%22*%22%5D&attributesToRetrieve=%5B%22*%22%5D&"
        "page="+ str(page) +
        "&hitsPerPage=60&maxValuesPerFacet=1000"}]}

headers = {'User-Agent': user_agent,
#           'Referer': my_url,
           'content-type': 'application/x-www-form-urlencoded',
           'accept': 'application/json'

           }

try:
       req = requests.post(my_url, json=value , headers=headers, timeout = 0.2) 
       print(req.status_code)
       req.encoding = 'utf-8' 
       ans= json.loads(req.text)
#       for key , value in ans.items():
#            print (key)
#            print (value)
#       print(ans)
       for item in ans['results'][0]['hits']:
           print(item['code'],item['sellingPrice'],item['nameZh'],item['nameEn'],item['numberOfReviews'])
           
#      print(req.text)
except requests.RequestException as e:
       print(e)
       
#elapsed_time = time.time() - start_time
#print (elapsed_time)


