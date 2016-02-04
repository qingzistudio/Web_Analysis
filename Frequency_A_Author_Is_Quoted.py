# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 15:31:38 2015

@author: gogo-qing
"""

import re
#read the file
import operator

f=open('in.html')
html=f.read()
f.close()

fw=open('out.txt','w')

segments=html.split('<div class="x-post-content">')

totalmatch=list()

for segment in segments[1:]:
 
    match=re.findall('<div class="htmlxquoteauthor">(.*?)wrote: </div>',segment,re.S) #find authors under the segments
    
    totalmatch.append(match)

    print match
    
total=sum(totalmatch,[])
total=map(str.strip, total) # prepocessing dataset

for i in range(len(total)):
    total[i]=total[i].lower()
    
# count the frequency 
counts = dict()
for i in total:
  counts[i] = counts.get(i, 0) + 1    # counted frequency of quotes

sorted_x = sorted(counts.items(), key=operator.itemgetter(0))

for key,value in sorted_x:
    fw.write(key+'\t'+'\t'+str(value)+'\n')
    
fw.close()

"""
#output
end the hate		1
hangupanddrive		2
justrightnow		2
lutin		2
nobama		2
purple haze		3
seriously		1
the unwashed		1
"""