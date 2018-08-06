# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:17:24 2018

@author: rusty
"""

#linking to database
from pymongo import MongoClient
user = 'root'
pwd = '123456'
client = MongoClient('mongodb://root:123456@localhost:27017')
print(client.database_names())
db = client.test
print(client.database_names())
collection = db['goods']
collection
collection.insert_one(
        { '_id': 'H0000000_0_00000000', # item['code']
         'price' : '100',  # item['sellingPrice']
         'nameZh': '測試' , # item['summaryZh']
         'nameEn':'Test' , #
         'review' : '0'    # item['numberOfReviews']
         }
        )
db.goods.find_one()