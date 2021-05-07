import pyautogui as pyautogui
from time import sleep

while True:
    posXy = pt.position()
    print(posXY, pt.Pixel(posXY[0], posXY[1]))
    sleep(1)
    if(posXY[0]==0):
        break