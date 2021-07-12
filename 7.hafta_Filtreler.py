import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Resim giriniz")
args = vars(ap.parse_args())

res = cv2.imread(args["image"])
cv2.imshow("Orjinal",res)


# Ortalama (averaging)
bulanik = np.hstack([
    cv2.blur(res, (3,3)),
    cv2.blur(res, (5,5)),
    cv2.blur(res, (7,7))
])
cv2.imshow("Ortalama", bulanik)


# Gauss  #daha yumuşak geçişli
bulanikGauss = np.hstack([
    cv2.GaussianBlur(res, (3,3), 0),
    cv2.GaussianBlur(res, (5,5), 0),
    cv2.GaussianBlur(res, (7,7), 0)
])
cv2.imshow("Ortalama", bulanikGauss)


# Median
bulanikMedian = np.hstack([
    cv2.medianBlur(res, 3),
    cv2.medianBlur(res, 5),
    cv2.medianBlur(res, 7)
])
cv2.imshow("Ortalama", bulanikMedian)


# Bilateral  #kenarları daha çok koruyo
bulanikBil = np.hstack([
    cv2.bilateralFilter(res, 3, 15, 15),
    cv2.bilateralFilter(res, 7, 51, 51)
])
cv2.imshow("Ortalama", bulanikBil)


cv2.waitKey(0)