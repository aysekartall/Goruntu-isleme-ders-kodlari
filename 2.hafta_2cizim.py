import cv2
import numpy as np

res = cv2.imread("C:\\Users\\Administrator\\Desktop\\Dersler 2021\\Goruntu Isleme\\DersKodlari\\2.resim.jpg")

bosRes = np.zeros((515,720,3), dtype='uint8')  #3 boyutlu matris tanımladık
#bosRes[:] = 0,255,0  #matrisin tüm elemanları yeşile boyandı
bosRes[100:300, 400:450] = 0,255,0 #ayrılan kısım boyandı
bosRes[100:100, 200:200] = 0,0,255

# Resim Üzerine Dikdörtgen Çizme
cv2.rectangle(bosRes, (0,0), (bosRes.shape[1]//2, bosRes.shape[0]//2), (0,255,0), thickness=1)
cv2.imshow('dikdortgen', bosRes)

cv2.imshow('Bos resim', bosRes)
cv2.imshow('Manzara', res)

cv2.waitKey(0)