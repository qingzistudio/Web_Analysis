# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 04:10:52 2015

@author: gogo-qing
"""
import re
import time,sys
from selenium import webdriver

def parsePage(html,monthSet):
    cc=0
    dates=re.finditer('<span class="a-size-base a-color-secondary review-date">(.*?)</span>',html)    
    for date in dates:
        monthSet.append(date.group(1).strip())
        cc+=1 
    print cc
    
    
#open Amazon pages
fileReader=open('in.txt')
for url in fileReader:
    url=url.strip() 
fileReader.close()

count=0

driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

time.sleep(2) 

allusers=list()

parsePage(driver.page_source,allusers)
print 'page 1 done'

#cm_cr-pagination_bar > ul > li.a-last > a

page=2
while True:
    cssPath='#cm_cr-pagination_bar > ul > li.a-last > a'
    
    try:
        button=driver.find_element_by_css_selector(cssPath)
    except:
        error_type, error_obj, error_info = sys.exc_info()
        print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
        print error_type, 'Line:', error_info.tb_lineno
        break

    button.click()
    time.sleep(2)
    
    parsePage(driver.page_source,allusers)

    print 'page',page,'done'
    page+=1

    
#write the results
fw=open('out.txt','w')
for user in allusers:
    if "August" in user:
       count+= 1
fw.write('%d\n' % count)
fw.close()

