import re
import time,sys
from selenium import webdriver

url='http://www.argos.co.uk/static/Browse/ID72/33017148/c_1/1%7Ccategory_root%7CTechnology%7C33006169/c_2/2%7C33006169%7CTelevisions+and+accessories%7C33008651/c_3/3%7Ccat_33008651%7CTelevisions%7C33017148.htm?tx=true&SEARCH_METADATA=uk.co.argos.ecommerce.search.util.SearchMetadata%4035c635c6'

driver = webdriver.Chrome('chromedriver.exe') 
driver.get(url)

time.sleep(2) 

ReviewsNumber=list()
ReviewsAddress=list()


ReviewsAdd=re.findall('<dd class="customerrating ">\n\t\t\t<a href="(.*?)#pdpProductReviews"',driver.page_source)
ReviewsNo=re.findall('\xa0(.*?)\n\t\t\t</a>',driver.page_source) 

Addressname=list()
Review=list()
for i in range(len(ReviewsNo)):
    a = ReviewsNo[i].replace('(',' ')
    b = a.replace(')',' ')
    Review.append(int(b))

DictReviews = dict(zip(ReviewsAdd,Review))
for i in range(len(DictReviews)):
    if DictReviews.values()[i]>400:
        Addressname.append(str(DictReviews.keys()[i]))
        
        
Addressname = Addressname[:-1]

#Build functions
#selecting rating parts

def Rating(html,userlist):
    ratings=re.findall('itemtype="http://schema.org/Rating" class="BVRRRatingNormalOutOf"> <.*?>(.*?)</span>',html)    
    for rate in ratings:
        userlist.append(rate.strip())
        
#overall rating         
def Fullreviews(html,userlist):
    reviews=re.finditer('</span> <span class="BVRRReviewText">(.*?)\n(.*?)</span>',html)    
    for user in reviews:
        userlist.append(user.group().strip())
                   

def Subdate(html,userlist):
    date=re.finditer('<span class="BVRRValue BVRRReviewDate">(.*?)<meta',html)    
    for day in date:
        userlist.append(day.group(1).strip())


driver = webdriver.Chrome('chromedriver.exe') 


#change0

ratinglist=list()
reviewslist=list()
datelist=list()


def Pagelink(i):
    driver.get(Addressname[i])#change1
    time.sleep(2) 

for i in range(len(Addressname)):
    Pagelink(i)
    
    Rating(driver.page_source,ratinglist)
    Fullreviews(driver.page_source,reviewslist)
    Subdate(driver.page_source,datelist)
    print 'page 1 done'

    page=2
    while True:
        cssPath='#BVRRDisplayContentFooterID > div > span.BVRRPageLink.BVRRNextPage > a'
     
        try:
            button=driver.find_element_by_css_selector(cssPath)
        except:
            error_type, error_obj, error_info = sys.exc_info()
            print 'STOPPING - COULD NOT FIND THE LINK TO PAGE: ', page
            print error_type, 'Line:', error_info.tb_lineno
            break

        button.click()
        time.sleep(2)
    
        Rating(driver.page_source,ratinglist)
        Fullreviews(driver.page_source,reviewslist)
        Subdate(driver.page_source,datelist)

        print 'page',page,'done'
        page+=1
    
    ratinglist=ratinglist[:-1]
   


w=[w.replace('</span> <span class="BVRRReviewText">',' ') for w in reviewslist]
b=[b.replace('</span>\n<span class="BVRRReviewTextSuffix">"</span>',' ') for b in w]
l=[l.replace('</span>\n</div><div class="BVRRReviewTextParagraph BVRRReviewTextLastParagraph"> <span class="BVRRReviewText">','\n') for l in b]

final=list()
for i in range(len(l)):
    final.append(l[i].encode('ascii', 'replace'))
    
 

zippart = zip(final,ratinglist,datelist)#change1
    

fw=open('reviews.txt','a')
for (i,j,k) in zippart:
    fw.write('http://www.argos.co.uk/'+'\t'+i+'\t'+j+'\t'+k+'\n') 
fw.close()


"""

# Output
www.bestbuy.com	Like the picture clarity and sharpness. On line e-guide very helpful.	4.0	10/04/2015
www.bestbuy.com	TV has a very sharp picture. Smart TV features are easy to use and it's so convenient to have all of that at the touch of a button. Good value for the price.	5.0	10/04/2015
www.bestbuy.com	Unbelievable picture quality. Easy to set up and use. Who needs cable TV?!	5.0	10/04/2015
www.bestbuy.com	very good I would recommend purchasing this item to my freinds	5.0	10/03/2015
www.bestbuy.com	Returned a Visio 55 in and paid $100 more for the Samsung. I'm glad I did because the Samsung is MUCH better in terms of picture quality.	5.0	10/03/2015
www.bestbuy.com	I purchased the television not necessarily knowing how much difference there was between 1080 resolution and 4k.<br />Now I know.<br />A fabulous picture that appears almost 3-D, and makes watching television more of an "experience" than simply watching television. The clarity, depth, and realism are beyond remarkable. For the price, I would not hesitate to purchase one or more of these televisions for my home.	5.0	10/03/2015
www.bestbuy.com	We are extremely pleased with this TV. Everyone who has seen it amazed	5.0	10/03/2015
www.bestbuy.com	After the purchase of the Samsung LED TV, I decided to hire Geek Squad to come in my home to set up along with a home theater system. No problems. If you are a lady, this is great! Highly worth all the extra money.	4.0	10/03/2015
www.bestbuy.com	Came from a 4 year old panasonic 50 inch 1080p plasma which died. At first I wasn't happy but after living with it for a few months I have changed my mind. Good picture after messing with some settings, color brightness etc. Haven't used smart part yet. Looks a little confusing. Still prefer plasma...but I'm happy.	4.0	10/03/2015
www.bestbuy.com	Easy to use great picture, light, stand keeps it close to wall good sound	5.0	10/03/2015
"""

