import numpy as np
import argparse  #console'dan parametre girisi için
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Goruntu yolunu gir")
args = vars(ap.parse_args())


print("Toplam={}".format(np.uint8([250]) + np.uint8([50])))  #[44]
print("Fark={}".format(np.uint8([50]) - np.uint8([250])))  #[56]
print("Toplam_CV2={}".format(cv2.add(np.uint8([250]), np.uint8([50])))) #[[255]]
print("Fark_CV2={}".format(cv2.subtract(np.uint8([50]), np.uint8([200])))) #[[0]]

res = cv2.imread(args["image"])
cv2.imshow("Orjinal", res)

# Renge ekleme (beyazlaştı)
M = np.ones(res.shape, dtype="uint8") * 100
ekle = cv2.add(res, M)
cv2.imshow("Eklenmis Resim", ekle)

#Renk çıkarma (koyulaştı)
M = np.ones(res.shape, dtype="uint8") * 50
fark = cv2.subtract(res, M)
cv2.imshow("Farki alinmis Resim", fark)

#BITWISE ISLEMLER
dortgen = np.zeros((300,300), dtype="uint8")
cv2.rectangle(dortgen, (25,25),(275,275),255,-1)
cv2.imshow("dortgen", dortgen)

cember = np.zeros((300,300),dtype="uint8")
cv2.circle(cember, (150,150),150,255,-1)
cv2.imshow("Cember", cember)


bAND = cv2.bitwise_and(dortgen, cember)
cv2.imshow("AND", bAND)

bOR = cv2.bitwise_or(dortgen, cember)
cv2.imshow("OR", bOR)

bXOR = cv2.bitwise_xor(dortgen, cember)
cv2.imshow("XOR", bXOR)

bNOT = cv2.bitwise_not(dortgen, cember)
cv2.imshow("NOT", bNOT)


#MASKELEME
maske = np.zeros(res.shape[:2],dtype="uint8")
(mX , mY) = (res.shape[1]//2, res.shape[0]//2)
cv2.rectangle(maske, (mX-100, mY-100), (mX+100, mY+100), 255, -1)
cv2.imshow("Maske", maske)

maskelenmiş = cv2.bitwise_and(res, res, mask = maske)
cv2.imshow("Maskelenmis", maskelenmiş)


#Kanallara Bölme ve Kanalları Birleştirme
(B, G, R) = cv2.split(res)
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)

birlestir = cv2.merge([B, G, R])
cv2.imshow("BirlesitrRGB", birlestir)


#Renk Uzayları
gri = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gri", gri)

hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(res, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

cv2.waitKey(0)
