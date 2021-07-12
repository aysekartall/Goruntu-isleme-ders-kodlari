import numpy as np
import imutils
import cv2
import argparse   #resmi parametre olarak girdi vermek için

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="Image yolu")
args = vars(ap.parse_args())

res = cv2.imread(args["image"])
cv2.imshow("Orjinal Resim", res)

# def fonksiyonları refactoring 

#M = np.float32([[1,0,25],[0,1,50]])  # T matrisimiz 1,0,dx ve 0,1,dy sütun olarak

# OTELEME
def Otele(res, tx, ty):
    M = np.float32([[1,0,tx],[0,1,ty]])
    otele = cv2.warpAffine(res, M, (res.shape[1],res.shape[0]))
    cv2.imshow("Translate islemi", otele)

Otele(res,100,-50)


# DONME
def Donme(res, aci):
    (h,w) = res.shape[:2]
    merkez = (w//2, h//2)
    M = cv2.getRotationMatrix2D(merkez, aci, 1.0)
    donme = cv2.warpAffine(res, M, (w,h))
    cv2.imshow("Donme islemi", donme)

Donme(res, 45)

# YENİDEN BOYUTLANDIRMA
def yenidenBoyutlandir(res):
    r = 250.0 / res.shape[1]
    boy = (150, int(res.shape[0] * r))
    yeniBoy = cv2.resize(res, boy, interpolation=cv2.INTER_AREA)
    cv2.imshow("Yeniden boyutlandırma", yeniBoy)

yenidenBoyutlandir(res)



# AYNALA
aynala = cv2.flip(res, 1)
cv2.imshow("Yatay aynala", aynala)


cv2.waitKey(0)
