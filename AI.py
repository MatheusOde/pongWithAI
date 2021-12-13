# to use the screen as an array of pixels
import numpy as np
# to grab the screen
import pyscreenshot as ImageGrab
# to scan the screen color
#import cv2

import keyboard

import time
bbox = (0, 0, 800, 600)

gameCoords = [0, 0, 0, 0]
systemImage = ImageGrab.grab(bbox)
screen = np.asanyarray(systemImage)
#screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

# AI loop
while (True):
    startTime = time.time()
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if keyboard.is_pressed('q'):
                print('You Pressed A Key!')
                exit()
            print("Took {} seconds.".format(time.time() - startTime))
