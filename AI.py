# to use the screen as an array of pixels
import numpy as np
# to grab the screen
import pyscreenshot as ImageGrab
# to scan the screen color
#import cv2

import keyboard
from pyautogui import press, sleep, typewrite, hotkey

import time
#calculate the window location
screenSize = (1366, 768)
screenCenter = (screenSize[0]/2, screenSize[1]/2)
gameSize = (600, 480)

x1 = screenSize[0]/2 - gameSize[0]/2
print(x1)
x2 = screenSize[0]/2 + gameSize[0]/2
print(x2)
y1 = screenSize[1]/2 - gameSize[1]/2
print(y1)
y2 = screenSize[1]/2 + gameSize[1]/2
print(y2)

gameBoxCoords = (x1, y1, x2, y2)

systemImage = ImageGrab.grab(gameBoxCoords)
screen = np.asanyarray(systemImage)
#screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

# AI loop

"""
while (True):
    startTime = time.time()
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            if keyboard.is_pressed('q'):
                typewrite('q is a letter')
                print('screen width: ', screenWidth, 'screen height: ', screenHeight)
                exit()
            print("Took {} seconds.".format(time.time() - startTime))
"""