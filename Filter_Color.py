import cv2
import numpy as np
import os
import TrainAndTest as tnt
import datetime as dt
import threading


def findText(imgPath):

    imgs=load_images_from_folder(imgPath)
    f = open("ketqua\\ketqua.txt", "a")
    for img in imgs:
        singleImage=cv2.imread(img)
        # print img
        t=extractImageColor(singleImage)
        # print img
        f.write(img+" - "+tnt.extracTextFromImage(t) + '\n')
    f.close()
    for img in imgs:
        os.remove(img)

def load_images_from_folder(folder):
    # date="{:%HGio%MPhut%SGiay%B %d, %Y}".format(dt.datetime.now())
    print "Loading Image from folder"
    allImages=[]
    for filename in os.listdir(folder):
        # img1 = cv2.imread(os.path.join(folder,filename))
        allImages.append(os.path.join(folder,filename))

    return allImages
    #     # print os.path.join(folder,filename)
    #     t=extractImageColor(img1)
    #     # cv2.imwrite('D:\\Ouput\\'+filename+'.png', t, params=None) # Write extracted image to folder
    #     f.write(filename+" - "+tnt.extracTextFromImage(t)+'\n')
    # f.close()

def extractImageColor(img1):
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,180, 150])
    upper_red = np.array([4, 260,280])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)
    # upper mask (170-180)
    lower_red = np.array([170, 180, 150])
    upper_red = np.array([180,260,280])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # join my masks
    mask = mask0 + mask1

    res = cv2.bitwise_and(img1, img1, mask=mask)

    imgGray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)  # get grayscale image
                         # blur
    ret, thresh1 = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY_INV)
    #
    #
    # cv2.imshow('goc', img1)
    # cv2.imshow('den trang', thresh1)
    # cv2.waitKey(0)
    return thresh1

def run():
    folderPath='data'
    findText(folderPath)
