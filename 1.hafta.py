import cv2
# import matplotlib.pyplot as plt

print(cv2.__version__)

#Reading Image
res = cv2.imread("C:\\Users\\Administrator\\Desktop\\Dersler 2021\\Goruntu Isleme\\DersKodlari\\1.resim.jpg")
cv2.imshow("manzara",res)
# plt.show()
cv2.waitKey(0)