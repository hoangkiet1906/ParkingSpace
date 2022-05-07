import cv2
import pickle

# img = cv2.imread("carParkImg.png")
width, height = 106,192-147;

try:
    with open("carPos", "rb") as f:
        list = pickle.load(f)
except:
    list = []

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        list.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(list):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+width:
                list.pop(i)
    with open("carPos", "wb") as f:
        pickle.dump(list,f)

while True:
    img = cv2.imread("carParkImg.png")

    for pos in list:
        cv2.rectangle(img,(pos[0],pos[1]),(pos[0]+width,pos[1]+height),(255,0,0),2)
    cv2.imshow("img", img)
    cv2.setMouseCallback("img", mouseClick)
    cv2.waitKey(1)