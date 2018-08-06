# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:01:57 2018

@author: rusty
"""

from bs4 import BeautifulSoup
import json
import requests
import time
#time test
start_time = time.time()
product_code = 'H0888001_S_10013908'
my_url ='https://www.hktvmall.com/hktv/zh/main/Unilever-/s/p/'+ product_code

headers = {
#           'Cookie' : 'ott-uuid=caa1ec83-b69b-44d1-90a2-25bd14a62878; device-type=desktop-web; _ga=GA1.2.1680261936.1530093855; LBI=-538824377; JSESSIONID=E5312BF318F8AC2BEB0198BC360C4182; _gid=GA1.2.676302823.1532249219; _gac_UA-55283480-1=1.1532249337.CjwKCAjw1tDaBRAMEiwA0rYbSDVdSZWl_XqaW-hJuP9OlFgHMx0j6UiqLYGv0pMlqeNHHqtF1ZRnWRoCCOYQAvD_BwE; _gac_UA-68175808-1=1.1532249337.CjwKCAjw1tDaBRAMEiwA0rYbSDVdSZWl_XqaW-hJuP9OlFgHMx0j6UiqLYGv0pMlqeNHHqtF1ZRnWRoCCOYQAvD_BwE; hktv-cart=04c173e8ce4a1503f827cb7351265e1e8dd1a93a; _gat_UA-55283480-1=1; _gat_UA-68175808-1=1',
#           'content-type' : 'application/x-www-form-urlencoded',
#           'accept': 'application/json'
           }

try:
       req = requests.get(my_url)
       
       print(req.status_code)
       req.encoding = 'utf-8'
#       for key , value in ans.items():
#            print (key)
#            print (value)
#       print(ans)
       soup = BeautifulSoup(req.text, 'html.parser')
       #price
       name = soup.find('div', class_='breadcrumb-btm').find('h1',class_='last')
       promo_price = soup.find('div',"product-detail").find('div','promotional').text 
       price = soup.find('div',"product-detail").find('div','price').text
       
       #image
       image = soup.find('div',"prod-det-gallery").findAll('img')
       
       #others
#       detail = soup.findAll('tr','productPackingSpec')
       spec = soup.find('tr','productPackingSpec').find('td').next_sibling.text
       origin = soup.find('tr','productPackingSpec').next_sibling
#       delivery = soup.find('tr','product-return-delivery').findAll('li')
       print(name.text)
       for i in image:
           print(i['src'])
       print("promotional_price" ,promo_price )
       print("price",price)
#       for i in detail:
#           print(i.text)
#       print(spec)
#       print(origin)
#       for i in delivery:
#           print(i.text)
       
#      print(req.text)
except requests.RequestException as e:
       print(e)
elapsed_time = time.time() - start_time
print (elapsed_time)       