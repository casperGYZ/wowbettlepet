import mss as mss
import pyautogui
import cv2
import numpy as np
import random
import time

mon = {'top':1,'left':1,'width':1920, 'height':1080}

sct = mss.mss()

goudan_img = cv2.imread('needle.png', cv2.IMREAD_UNCHANGED)
w = goudan_img.shape[1]
h = goudan_img.shape[0]

threshold = 0.8

while 1:
    sct_img = np.array(sct.grab(mon))
    result = cv2.matchTemplate(sct_img, goudan_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    yloc, xloc = np.where(result >= threshold)
    rectangles =[]
    time.sleep(round(random.uniform(0.5, 1.2)))
    pyautogui.press('[')
    time.sleep(round(random.uniform(0.5,1.2)))
    pyautogui.press(']')

    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles,1,0.2)

    for (x, y, w, h) in rectangles:
        cv2.rectangle(sct_img, (x,y), (x + w, y + h), (0, 255, 0), 2)
        pyautogui.click((x + 1 + w/2),(y - 5 + h/2))
        time.sleep(10)
        pyautogui.click((x + 1 + w / 2), (y + 1 + h * 7 / 8))
        time.sleep(10)
        pyautogui.click((x + 1 + w / 2), (y + 1 + h * 7 / 8))
        time.sleep(20)
        pyautogui.click(945,983)
        time.sleep(20)
        pyautogui.click(945, 983)
        time.sleep(1)
        pyautogui.click(945, 983)
        time.sleep(1)
        pyautogui.click(945, 983)


    cv2.imshow('test', sct_img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
         cv2.destroyAllWindows()
         break
         
