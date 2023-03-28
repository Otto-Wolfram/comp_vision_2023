import cv2
import time
import Hand_Tracking_Module as htm

print("start video...")

frameWidth = 1280
frameHeight = 720
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
pTime = 0
cTime = 0

print("handDetector инициализация...")

detector = htm.handDetector()

print("start algorithm...")


# любые нужные вам функции
def some_f_1():
    print("some_f_1")


def some_f_2():
    print("some_f_2")


def some_f_3():
    print("some_f_3")


def some_f_4():
    print("some_f_4")


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)

    # в зависимости от полученного положения рук включаем разные функции (какие - можно реализовать как угодно)
    if len(lmlist) != 0:
        pos = lmlist[4]
        if pos[1] < 300 and pos[2] < 250:
            some_f_1()
        if pos[1] < 300 and pos[2] >= 250:
            some_f_2()
        if pos[1] >= 300 and pos[2] < 250:
            some_f_3()
        if pos[1] >= 300 and pos[2] >= 250:
            some_f_4()

    # отображение фпс для отладки
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS= " + str(int(fps)), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1,(0, 0, 0), 1)

    # Вывод и обработка закрытия
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 20:
        break
