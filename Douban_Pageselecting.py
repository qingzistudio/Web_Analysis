# -*- coding: utf-8 -*-
"""
Created on Sun Oct 04 23:31:47 2015

@author: gogo-qing
"""
import re
import time,sys
from selenium import webdriver

url='http://www.douban.com/doulist/41195002/?start=0&sort=seq&sub_type='

driver = webdriver.Chrome('chromedriver.exe') 
driver.get(url) #get information from douban.com

time.sleep(2) 

Rates=list()
ratetotal=list()
Addresses=list()
addtotal=list()

Rates=re.findall('<span class="rating_nums">(.*?)</span>',driver.page_source)
ratetotal.append(Rates)

Addresses=re.findall('<div class="post">\n      <a href="(.*?)" target=',driver.page_source) 
addtotal.append(Addresses)
#content > div > div.article > div.paginator > span.next > a

page=2
while True:
    cssPath='#content > div > div.article > div.paginator > span.next > a'
    
    try:
        button=driver.find_element_by_css_selector(cssPath)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break

    button.click()
    time.sleep(2)
    
    Rates=re.findall('<span class="rating_nums">(.*?)</span>',driver.page_source)
    ratetotal.append(Rates)
    Addresses=re.findall('<div class="post">\n      <a href="(.*?)" target=',driver.page_source)    
    addtotal.append(Addresses)

    print 'page',page,'done'
    page+=1
    
ratetotal=sum(ratetotal,[])
addtotal=sum(addtotal,[])

Dict = dict(zip(ratetotal,addtotal))

"""


for i in range(len(DictReviews)):
    if DictReviews.values()[i]>400:
        Addressname.append(DictReviews.keys()[i])

"""


 

