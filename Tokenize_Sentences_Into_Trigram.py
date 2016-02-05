# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:05:57 2015

@author: gogo-qing
"""

import nltk
import nltk.data
from nltk.util import ngrams
import re
from nltk.corpus import stopwords


#read the input
f=open('article.txt')
text=f.read().strip().lower() #strip each word and make it lower 
f.close()

fileWriter=open('out.txt','w')

sentences=re.split('\.',text)
print 'NUMBER OF SENTENCES: '+ str(len(sentences))

all3grams=set()

stop = stopwords.words('english')

# for each sentence
for sentence in sentences:
    
    nones=set()
    
    sentence=re.sub('[^a-z\d]',' ',sentence)
    sentence=re.sub(' +',' ',sentence).strip()
    
    terms=sentence.split()
    
    tagged_terms=nltk.pos_tag(terms)#do POS tagging on the tokenized sentence, which parts of the spee
            
    for pair in tagged_terms: 
        
        if pair[1].startswith('NN'): nones.add(pair[0])
        
    twograms = ngrams(terms,3) #compute 2-grams
    
    #for each 2gram
    for tg in twograms:  
        if tg[0] not in stop and tg[1] not in stop and tg[2] not in stop:
            if tg[0] in nones and tg[1] in nones: # if the 2gram is a an adverb followed by an adjective
                print tg
                fileWriter.write(tg[0]+' '+tg[1]+' '+tg[2]+'\n')
    
            elif tg[0] in nones and tg[2] in nones: # if the 2gram is a an adverb followed by an adjective
                print tg
                fileWriter.write(tg[0]+' '+tg[1]+' '+tg[2]+'\n')
            
            elif tg[1] in nones and tg[2] in nones: # if the 2gram is a an adverb followed by an adjective
                print tg
                fileWriter.write(tg[0]+' '+tg[1]+' '+tg[2]+'\n')
            
            elif tg[0] in nones and tg[1] in nones and tg[2] in nones: # if the 2gram is a an adverb followed by an adjective
                print tg
                fileWriter.write(tg[0]+' '+tg[1]+' '+tg[2]+'\n')
        
        
"""

#Output

gainesville	florida	ap
feet	125	meters
sea	crusted	anchor
cargo	lay	scattered
terra	cotta	jars
cotta	jars	called
jars	called	amphora
florida	based	group
global	underwater	explorers
underwater	explorers	gue
wreck	fetching	artifacts
wine	olive	oil


"""        
    
        
