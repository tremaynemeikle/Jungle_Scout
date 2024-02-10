import pyautogui
import time
from random import randint

pages = 40

# Download Save
pyautogui.moveTo(115, 810, .3)
pyautogui.click()

for i in range(0, pages):

    if (i%15 == 0) & (i > 0):
        time.sleep(randint(10,60))
    
    # Download csv
    pyautogui.moveTo(1310, 345, .3)
    time.sleep(.5)
    pyautogui.moveTo(1318, 345, .3)
    time.sleep(.3)
    pyautogui.click()
    time.sleep(1)

    time.sleep(1)

    # Download Save
    pyautogui.moveTo(1185, 810, .3)
    pyautogui.click()

    time.sleep(1)

    # Next Page Right
    pyautogui.moveTo(1570, 339, .3)
    pyautogui.click()

    time.sleep(30)





