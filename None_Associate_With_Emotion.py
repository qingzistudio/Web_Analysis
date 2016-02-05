# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 21:59:10 2015

@author: gogo-qing
"""

import HTMLParser
from sklearn.feature_extraction import text
import pandas as pd
import re
import nltk
import nltk.data
from nltk.util import ngrams
import re, string, timeit
import numpy as np
import operator
from collections import OrderedDict

stopwords = text.ENGLISH_STOP_WORDS
punctuation = string.punctuation
html_parser = HTMLParser.HTMLParser()
#Frame = pd.read_csv('emotions.txt', index_col=None, delimiter="\t")

#English Word    abacus
#Anger                0
#Anticipation         0
#Disgust              0
#Fear                 0
#Joy                  0
#Sadness              0
#Surprise             0
#Trust                1
#Name: 1, dtype: object

# read emotion dictionary. 
def LoadSet(fname):
    emotion = dict()
    Frame = pd.read_csv(fname, index_col=None, delimiter="\t")
    for index in range(len(Frame)):
        emotion[Frame.ix[index].tolist()[0]] = Frame.ix[index].tolist()[1:]
    return emotion

#save it as dataset
dataset=LoadSet('emotions.txt')

#read text 
with open('data.txt','r+') as file:
    contain = file.read()
    #contain = re.replace('[\d+]','',contain)
    contain = contain.split('\n')
    contain = html_parser.unescape(contain)
    textcontain = []
    for i in contain:
        word = [' '.join(c for c in i.split() if c not in stopwords)]
        textcontain.append(word)
    file.close()
#    
FinalEmo = dict()     
     
for sentence in textcontain:
    
     origin = np.array([0,0,0,0,0,0,0,0])
     NN = set()
     Emotions = set()
     
     #preporcessing the data
     sentence[0] = re.sub(' +',' ',sentence[0]).strip()
     sentence[0] = re.sub('[\d+]','',sentence[0])
     sentence[0] = re.sub('ac','',sentence[0])
     sentence[0] = re.sub('s','',sentence[0])
     for p in punctuation: 
         sentence[0]=sentence[0].replace(p,'')
     
     terms = sentence[0].split()
          
     tagged_terms=nltk.pos_tag(terms)#do POS tagging on the tokenized sentence, which parts of the spee
             
     for pair in tagged_terms:       
        if pair[1].startswith('NN'): # keep nones in NN
            NN.add(pair[0]) 
        else:
            Emotions.add(pair[0]) #keep others in Emotions
 
        
     for Emo in Emotions:
        try:            
            idex = np.array(dataset[Emo])
            origin = origin + idex
        except:
            print 'Do not contain this word'
            continue
     
     
     for word in NN:
         if word in FinalEmo.keys():
             FinalEmo[word] = FinalEmo[word] + np.array(origin)
        
         else:
             F
    
   
sorted_x7 = sorted(FinalEmo.items(), key=lambda (k,v):v[7], reverse=True)
sorted_x6 = sorted(FinalEmo.items(), key=lambda (k,v):v[6], reverse=True)
sorted_x5 = sorted(FinalEmo.items(), key=lambda (k,v):v[5], reverse=True)
sorted_x4 = sorted(FinalEmo.items(), key=lambda (k,v):v[4], reverse=True)
sorted_x3 = sorted(FinalEmo.items(), key=lambda (k,v):v[3], reverse=True)
sorted_x2 = sorted(FinalEmo.items(), key=lambda (k,v):v[2], reverse=True)
sorted_x1 = sorted(FinalEmo.items(), key=lambda (k,v):v[1], reverse=True)
sorted_x0 = sorted(FinalEmo.items(), key=lambda (k,v):v[0], reverse=True)
  

output=open('output_emo.txt','ab')
    
for i in range(20):
    x0_20word = sorted_x0[i][0]
    x0_20freq = sorted_x0[i][1][0]
    output.write('Emotion:Anger'+'\t'+x0_20word+'\t'+'Frequency:'+str(x0_20freq)+'\n')

output.write("================================================"+'\n')

for i in range(20):
    x1_20word = sorted_x1[i][0]
    x1_20freq = sorted_x1[i][1][1]
    output.write('Emotion:Anticipation'+'\t'+x1_20word+'\t'+'Frequency:'+str(x1_20freq)+'\n')

output.write("================================================"+'\n')   
   
for i in range(20):
    x2_20word = sorted_x2[i][0]
    x2_20freq = sorted_x2[i][1][2]
    output.write('Emotion:Disgust'+'\t'+x2_20word+'\t'+'Frequency:'+str(x2_20freq)+'\n')

output.write("================================================"+'\n')
   
for i in range(20):
    x3_20word = sorted_x3[i][0]
    x3_20freq = sorted_x3[i][1][3]
    output.write('Emotion:Fear'+'\t'+x3_20word+'\t'+'Frequency:'+str(x3_20freq)+'\n')

output.write("================================================"+'\n')
   
for i in range(20):
    x4_20word = sorted_x0[i][0]
    x4_20freq = sorted_x0[i][1][4]
    output.write('Emotion:Joy'+'\t'+x4_20word+'\t'+'Frequency:'+str(x4_20freq)+'\n')

output.write("================================================"+'\n')

for i in range(20):
    x5_20word = sorted_x0[i][0]
    x5_20freq = sorted_x0[i][1][5]
    output.write('Emotion:Sadness'+'\t'+x5_20word+'\t'+'Frequency:'+str(x5_20freq)+'\n')

output.write("================================================"+'\n')
       
for i in range(20):
    x6_20word = sorted_x0[i][0]
    x6_20freq = sorted_x0[i][1][6]
    output.write('Emotion:Surprise'+'\t'+x6_20word+'\t'+'Frequency:'+str(x6_20freq)+'\n')

output.write("================================================"+'\n')
       
for i in range(20):
    x7_20word = sorted_x0[i][0]
    x7_20freq = sorted_x0[i][1][7]
    output.write('Emotion:Trust'+'\t'+x7_20word+'\t'+'Frequency:'+str(x7_20freq)+'\n')
    
output.close()


"""
# Output

Emotion:Anger	time	Frequency:50
Emotion:Anger	month	Frequency:50
Emotion:Anger	day	Frequency:50
Emotion:Anger	jut	Frequency:49
Emotion:Anger	im	Frequency:47
Emotion:Anger	year	Frequency:43
Emotion:Anger	ugar	Frequency:36


"""