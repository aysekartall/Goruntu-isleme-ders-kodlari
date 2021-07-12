import numpy as np
import argparse  #console'dan parametre girisi için
import cv2
import imutils
from matplotlib import pyplot as plt

"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Resim yolunu ve dosya adını gir")
args = vars(ap.parse_args())
"""

img = cv2.imread("Keskinlestirme.jpg")

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

img_sharpened = cv2.filter2D(img, -1, kernel)

cv2.imwrite("sharpened.jpg",img_sharpened)

cv2.imshow('Bulanik', img)
cv2.imshow('Keskin', img_sharpened)

# resime yazı yazdırma
"""
img = np.zeros((480,640,3), np.uint8)

img = cv2.line(img,(320,0),(320,480),(255,0,0),2)
img = cv2.line(img,(0,240),(640,240),(255,0,0),2)

for i in range (0,640,10):
    img = cv2.line(img,(i,235),(i,245),(255,0,0),2)

for i in range (0,480,10):
    img = cv2.line(img,(315,i),(325,i),(255,0,0),2)

cv2.putText(img, "170303003 - Ayse Kartal", (500,30),cv2, 0.5,(0,0,255),2,cv2.LINE_AA)
cv2.imshow("001", img)
"""

position = ((int) (img_sharpened.shape[1]/2 - 268/2), (int) (img_sharpened.shape[0]/2 - 36/2))

cv2.putText(
     img_sharpened, 
     "170303003-Ayse Kartal", 
     position, 
     cv2.FONT_HERSHEY_SIMPLEX, 
     1, 
     (209, 80, 0, 255),
     3) 
cv2.imwrite('output.png', img_sharpened)
cv2.imshow("Yazili ve Keskinlesmis Resim", img_sharpened)
cv2.waitKey(0)


