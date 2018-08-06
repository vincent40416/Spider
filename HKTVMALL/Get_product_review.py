# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:52:42 2018

@author: rusty
"""

import json
import requests
import time

#time test
#start_time = time.time()



product_code = 'H0888001_S_10013908'
page = 0

headers = {
           #'Cookie' : 'ott-uuid=caa1ec83-b69b-44d1-90a2-25bd14a62878; device-type=desktop-web; _ga=GA1.2.1680261936.1530093855; LBI=-538824377; JSESSIONID=E5312BF318F8AC2BEB0198BC360C4182; _gid=GA1.2.676302823.1532249219; _gac_UA-55283480-1=1.1532249337.CjwKCAjw1tDaBRAMEiwA0rYbSDVdSZWl_XqaW-hJuP9OlFgHMx0j6UiqLYGv0pMlqeNHHqtF1ZRnWRoCCOYQAvD_BwE; _gac_UA-68175808-1=1.1532249337.CjwKCAjw1tDaBRAMEiwA0rYbSDVdSZWl_XqaW-hJuP9OlFgHMx0j6UiqLYGv0pMlqeNHHqtF1ZRnWRoCCOYQAvD_BwE; hktv-cart=04c173e8ce4a1503f827cb7351265e1e8dd1a93a; _gat_UA-55283480-1=1; _gat_UA-68175808-1=1',
#           'content-type' : 'application/x-www-form-urlencoded',
#           'accept': 'application/json'
           }

#time test
#start_time = time.time()
try:
        my_url = "https://www.hktvmall.com/hktv/zh/ajax/get_pdp_product_reviews?productCode="+product_code+"&currentPage="+str(page)+"&reviewType=all&pageSize=10&_=1532253592124"
        req = requests.get(my_url) 
        print(req.status_code)
        req.encoding = 'utf-8'
        ans= json.loads(req.text)
#        if page == 1:
#            Allreview=ans['reviewCounts']['all']
        for item in ans['reviews']:
            print(item['principal']['name'] , item['rating'], item['comment'])
           
       
except requests.RequestException as e:
       print(e)

#elapsed_time = time.time() - start_time
#print (elapsed_time)