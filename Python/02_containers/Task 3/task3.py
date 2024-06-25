import pyautogui
from time import sleep

def install ():
    try:
        location = None
        while location is None:
            location = pyautogui.locateOnScreen('install.png', confidence=0.9)
            sleep(1)
    except pyautogui.ImageNotFoundException:
        print('install not found !')
    
    pyautogui.click(location.left+20, location.top+5, duration=1)

pyautogui.press('win')
sleep(2)
pyautogui.write('code')
pyautogui.press('enter')
sleep(1)

try:
    location = None
    while location is None:
        location = pyautogui.locateOnScreen('extensions.png', confidence=0.9)
        sleep(1)
except pyautogui.ImageNotFoundException:
    print('extensions not found !')
    exit()

pyautogui.click(location.left, location.top+5, duration=1)
pyautogui.moveTo(205, 149)    # search bar
sleep(2)
pyautogui.click()

pyautogui.write('clangd')
sleep(2)
pyautogui.moveTo(246, 224)    # choice
sleep(2)
pyautogui.click()

install()

pyautogui.moveTo(205, 149)    # search bar
sleep(2)
pyautogui.tripleClick()
sleep(2)
pyautogui.write('c++ testmate')
sleep(2)
pyautogui.moveTo(246, 224)    # choice
sleep(2)
pyautogui.click()

install()

pyautogui.moveTo(205, 149)    # search bar
sleep(2)
pyautogui.tripleClick()
sleep(2)
pyautogui.write('c++ helper')
sleep(2)
pyautogui.moveTo(246, 224)    # choice
sleep(2)
pyautogui.click()

install()

pyautogui.moveTo(205, 149)    # search bar
sleep(2)
pyautogui.tripleClick()
sleep(2)
pyautogui.write('cmake')
sleep(2)
pyautogui.moveTo(246, 224)    # choice
sleep(2)
pyautogui.click()

install()

pyautogui.moveTo(205, 149)    # search bar
sleep(2)
pyautogui.tripleClick()
sleep(2)
pyautogui.write('cmake tools')
sleep(2)
pyautogui.moveTo(246, 224)    # choice
sleep(2)
pyautogui.click()

install()
