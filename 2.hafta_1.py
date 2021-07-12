import cv2
"""
# READ IMAGE
res = cv2.imread("C:\\Users\\Administrator\\Desktop\\Dersler 2021\\Goruntu Isleme\\DersKodlari\\2.resim.jpg")
cv2.imshow("Manzara resmi", res)

cv2.waitKey(0)
"""


"""
# READ VIDEO
capture = cv2.VideoCapture("C:\\Users\\Administrator\\Desktop\\Dersler 2021\\Goruntu Isleme\\DersKodlari\\Birdvideo.mp4")

while True: #sonsuz döngü kurulamsının sebebi framelerin sayısını bilmek zorunda olmayışımız ve fps oranını ayarlamak zorunda olmayışımız
    isTrue, frame = capture.read()
    cv2.imshow("papagan", frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
"""



# IMAGE RESIZE(RESMİ YENİDEN BOYUTLANDIRMA)
res = cv2.imread("C:\\Users\\Administrator\\Desktop\\Dersler 2021\\Goruntu Isleme\\DersKodlari\\2.resim.jpg")
cv2.imshow("manzara", res)

def ResOlcek(res, olcek = 0.75):
    yukseklik = int(res.shape[0] * olcek)  #satır
    genislik = int(res.shape[1] * olcek)   #sütun
    boyutlar = (genislik, yukseklik)
    resBoy = cv2.resize(res, boyutlar, interpolation = cv2.INTER_AREA)
    return resBoy

cv2.imshow("boyutlandırılmış", ResOlcek(res, 2))

#cv2.waitKey(0)


# VİDEO BOYUTLANDIRMA
capture = cv2.VideoCapture("C:\\Users\\Administrator\\Desktop\\Dersler 2021\\Goruntu Isleme\\DersKodlari\\Birdvideo.mp4")

while True:
    isTrue, frame = capture.read()
    frameBoy = ResOlcek(frame, 2)
    cv2.imshow('Video', frameBoy)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break
    
cv2.waitKey(0)
