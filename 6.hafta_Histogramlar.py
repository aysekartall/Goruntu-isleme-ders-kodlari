from matplotlib import pyplot as plt
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Resim yolu ve adi")
args = vars(ap.parse_args())

res = cv2.imread(args["image"])
resGri = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

#GRAY HISTOGRAM
def histGRAY():
    hist = cv2.calcHist([resGri], [0], None, [256], [0,255])

    #çalışmadı
    #yatayGoster = np.hstack((resGri, hist))
    #plt.imshow(yatayGoster, cmap="gray")

    #yatayGoster = np.hstack(res, resGri)
    #plt.imshow(yatayGoster)

    cv2.imshow("gri",resGri)
    #cv2.imshow("Histogram", hist)

    plt.figure()
    plt.title("Gri Histogram")
    plt.xlabel("seviyeler-Bins")
    plt.ylabel("piksel Sayısı")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)

histGRAY()


#COLOR-HISTOGRAM
def histCOLOR():
    kanallar = cv2.split(res)
    renkler = ("b", "g", "r")
    plt.figure()
    plt.title("Düz renkli histogram")
    plt.xlabel("Bins")
    plt.ylabel("Piksel #")

    for (kanal, renk) in zip(kanallar, renkler):
        hist = cv2.calcHist([kanal], [0], None, [256], [0,256])
        plt.plot(hist, color=renk)
        plt.xlim([0,256])
        plt.show()
        cv2.waitKey(0)

histCOLOR()


#2D HISTOGRAM
def hist2D():
    kanallar = cv2.split(res)
    fig = plt.figure()
    ax = fig.add_subplot(131)
    hist = cv2.calcHist([kanallar[1], kanallar[0]], [0,1], None, [32,32], [0,256,0,256])
    p = ax.imshow(hist, interpolation="nearest")
    ax.set_title("2D Renkli Histogram (Yesil, Mavi")
    plt.colorbar(p)
    plt.show()


#Hist Equalization
def histEsit():
    esit = cv2.equalizeHist(resGri)
    cv2.imshow("Histogram Esitleme", np.hstack([resGri, esit]))
    cv2.waitKey(0)


def main():
    histGRAY()
    histCOLOR()
    hist2D()
    histEsit()

main()
