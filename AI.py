import numpy as np
import pyscreenshot as ImageGrab
import cv2
import keyboard
import mouse
import time

screen = np.array(ImageGrab.grab(bbox=gameCoords))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

for i in range(1000):
    startTime = time.time()
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if keyboard.is_pressed('q'):
                exit
            if screen[y][x] < 10:
                mouse.move(x,y, absolute=False, duration=0)
                mouse.click('right'){x, y}
    print("Took {} seconds. Up to {} frames".format((time.time() - startTime), i))