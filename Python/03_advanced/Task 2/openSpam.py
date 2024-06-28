#this code for open spam emails 

import pyautogui
from time import sleep
import webbrowser

url = 'https://mail.google.com/mail/u/0/#inbox'

webbrowser.open(url, new=2)
sleep(4)

try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('More.png', confidence=0.9)
        sleep(1)
except pyautogui.ImageNotFoundException:
    print('Image not found !')
    exit()

pyautogui.click(location.left, location.top+5, duration=1)

try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('spam.png', confidence=0.9)
        sleep(1)
except pyautogui.ImageNotFoundException:
    print('Image not found !')
    exit()

pyautogui.click(location.left, location.top+5, duration=1)
