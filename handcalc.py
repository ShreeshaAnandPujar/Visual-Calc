import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70),
                    cv2.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y, img):
        if self.pos[0] < x < self.pos[0] + self.width and            self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80),
                        cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)
            return True
        return False

# Button layout with Clear button 'C'
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['C', '0', '.', '=']]

buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 800
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x]))

myEquation = ''
pinchClicked = False  # To prevent multiple inputs per pinch

# Webcam setup
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Draw result box
    cv2.rectangle(img, (800, 70), (800 + 400, 70 + 100), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (800, 70), (800 + 400, 70 + 100), (50, 50, 50), 3)
    cv2.putText(img, myEquation, (810, 130), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    # Draw buttons
    for button in buttonList:
        button.draw(img)

    if hands:
        lmList = hands[0]['lmList']
        if lmList:
            index_tip = lmList[8][:2]
            middle_tip = lmList[12][:2]
            length, _, img = detector.findDistance(index_tip, middle_tip, img)
            x, y = int(index_tip[0]), int(index_tip[1])

            if length < 30 and not pinchClicked:
                for button in buttonList:
                    if button.checkClick(x, y, img):
                        value = button.value
                        if value == '=':
                            try:
                                myEquation = str(eval(myEquation))
                            except:
                                myEquation = "Error"
                        elif value == 'C':
                            myEquation = ''
                        else:
                            myEquation += value
                        pinchClicked = True

            elif length > 50:
                pinchClicked = False

    key = cv2.waitKey(1)
    cv2.imshow("Image", img)
    if key == ord('c'):
        myEquation = ''
