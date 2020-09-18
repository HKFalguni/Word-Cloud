from os import path
from PIL import Image
import numpy as np
import os

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

currdir = path.dirname(__file__)

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'file.txt')).read()

# read the mask / color image taken from the path
alice_coloring = np.array(Image.open(path.join(d, "10r.jpg")))
stopwords = set(STOPWORDS)

wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, random_state=42 ,contour_color="green", contour_width=3)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

wc.to_file(path.join(currdir, "wc3.png"))

