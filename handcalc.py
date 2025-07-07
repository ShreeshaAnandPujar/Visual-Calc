import cv2, numpy as np
from cvzone.HandTrackingModule import HandDetector as D

class Btn:
    def __init__(s,p,w,h,v): s.p,s.w,s.h,s.v=p,w,h,v
    def d(s,i):
        x,y=s.p
        cv2.rectangle(i,s.p,(x+s.w,y+s.h),(225,225,225),cv2.FILLED)
        cv2.rectangle(i,s.p,(x+s.w,y+s.h),(50,50,50),3)
        cv2.putText(i,s.v,(x+25,y+70),cv2.FONT_HERSHEY_PLAIN,2,(50,50,50),2)
    def c(s,x,y,i):
        bx,by=s.p
        if bx<x<bx+s.w and by<y<by+s.h:
            cv2.rectangle(i,(bx+3,by+3),(bx+s.w-3,by+s.h-3),(255,255,255),cv2.FILLED)
            cv2.putText(i,s.v,(bx+25,by+80),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),5)
            return True
        return False

vals=[['7','8','9','/'],
      ['4','5','6','*'],
      ['1','2','3','-'],
      ['C','0','.','='],
      ['+']]  # ➕ This fixes your missing addition!

btns=[Btn((x*100+800,y*100+150),100,100,vals[y][x]) for y in range(len(vals)) for x in range(len(vals[y]))]
eq, pinch = '', False

cap=cv2.VideoCapture(0)
det=D(0.9,1)

while True:
    _,img=cap.read(); img=cv2.flip(img,1); h,img=det.findHands(img)
    cv2.rectangle(img,(800,70),(1200,170),(225,225,225),cv2.FILLED)
    cv2.rectangle(img,(800,70),(1200,170),(50,50,50),3)
    cv2.putText(img,str(eq),(810,130),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
    [b.d(img) for b in btns]

    if h:
        l=h[0]['lmList']; x,y=l[8][:2]; d,_,img=det.findDistance(l[8][:2],l[12][:2],img)
        if d<30 and not pinch:
            for b in btns:
                if b.c(x,y,img):
                    v=b.v
                    if v=='C': eq=''
                    elif v=='=':
                        try: eq=str(eval(eq))
                        except: eq="Err"
                    else: eq+=v
                    pinch=True
        elif d>50: pinch=False

    if cv2.waitKey(1)==ord('c'): eq=''
    cv2.imshow("Image",img)


