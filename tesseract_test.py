# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:05:38 2020

@author: wtjang
"""

from PIL import Image
from pytesseract import *

filename = r"C:\Users\wtjang\Downloads\test.jpg"
image = Image.open(filename)
text = image_to_string(image, lang="eng")

with open("sample.txt", "w") as f:
    f.write(text)
    
    
    
    
img = Image.open(r"C:\Users\wtjang\Downloads\test_2.jpg")

import pytesseract

# [WinError 5] 액세스가 거부되었습니다 해결
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

text = pytesseract.image_to_string(img,lang='eng')#영어면 'eng' 근데 str로 읽어서 이거 또 처리해야댐


text_1 = pytesseract.image_to_data(img,lang='eng')#영어면 'eng'



import pandas as pd
df = pd.DataFrame()

for i in range(2, len(text)):
    temp = text[i]
    temp = temp.split(',')
    
    df.loc[i-2] = temp