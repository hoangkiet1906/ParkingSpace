import cv2
import cvzone
import pickle
import numpy as np
cap = cv2.VideoCapture("carPark.mp4")
with open("carPos", "rb") as f:
    list = pickle.load(f)
width, height = 106,192-147;

def checkPos(imgProcess):
    for pos in list:
        x,y = pos
        imgCrop = imgProcess[y:y+height,x:x+width]
        count = cv2.countNonZero(imgCrop)
        cv2.putText(img,str(count),(x,y+height-10),cv2.FONT_ITALIC,0.5,(0,0,255),2)
        if count>800:
            cv2.rectangle(img, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), (255, 0, 0), 2)
        else:
            cv2.rectangle(img, (pos[0], pos[1]), (pos[0] + width, pos[1] + height), (0, 255, 0), 2)
            cv2.putText(img, "empty", (x+width-50, y + height - 10), cv2.FONT_ITALIC, 0.5, (255, 153, 255), 2)


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    ret, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
    #switch to calculate pixels
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3),np.int8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkPos(imgDilate)

    cv2.imshow("img", img)
    # cv2.imshow("imgC", imgMedian)

    cv2.waitKey(5)
