# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:47:05 2020

@author: hp
"""
from os import path
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
currdir = path.dirname(__file__)

comment_words= ' '
mask = np.array(Image.open(path.join(currdir, "cloud.png")))
stopwords=set(STOPWORDS)

f=open('file.txt','r+')
textdata=f.read().replace('\n','')
wc = WordCloud(background_color="white",
					max_words=200, 
					mask=mask,
	               	stopwords=stopwords).generate(textdata)
	
#wordcloud= WordCloud(width=800,height=800,background_color='white',stopwords=stopwords,min_font_size=10).generate(textdata)
wc.to_file('Image.png')
print('Image Saved Sucessfullly')