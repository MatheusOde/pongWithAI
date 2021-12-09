# to use the screen as an array of pixels
import numpy as np
# to grab the screen
import pyscreenshot as ImageGrab
# to scan the screen color
import cv2

#to get inputs and post outputs on to the game
import keyboard
import mouse

import time

screen = np.array(ImageGrab.grab(bbox=gameCoords))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

# AI loop
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