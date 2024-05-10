import pyautogui
import math
import time

# run this script while game is in full screen

time.sleep(2)
pyautogui.PAUSE = 0.01
# Radius 
R = 620
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius 
pyautogui.moveTo(X+R,Y)

for i in range(360):
    # setting pace with a modulus 
    if i%6==0:
       pyautogui.mouseDown()
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
pyautogui.moveTo(X+R,Y)
