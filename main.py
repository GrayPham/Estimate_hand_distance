import cv2
from HandTrackingModule import HandDetector
import math
import numpy as np
import putText

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Find Function
# x is the raw distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

# Loop
while True:
    success, img = cap.read()
    hands = detector.findHands(img, draw=False)
    print(hands[0])

    if hands[0]:
        print("Hand", hands[0])
        with open("texxt.txt", "w") as file:
            for value in hands:
                # Ghi từng giá trị vào tệp, theo dòng
                file.write(str(value) + "\n")
        lmList = hands[0][0]['lmList']
        x, y, w, h = hands[0][0]['bbox']
        print("lmList[5]", lmList[5])
        x1, y1,_ = lmList[5]
        x2, y2,_ = lmList[17]

        distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
        A, B, C = coff
        distanceCM = A * distance ** 2 + B * distance + C

        # print(distanceCM, distance)

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        putText.putTextRect(img, f'{int(distanceCM)} cm', (x+5, y-10))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()