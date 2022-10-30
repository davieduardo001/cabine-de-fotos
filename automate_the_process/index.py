##KEYBOARD EVENTS
#gui.keyDown('winleft')
#gui.press('d')
#gui.keyUp('winleft')
#sleep(10)
#gui.write('...')

##MOUSE EVENTS
#gui.moveTo(x=37, y=193, duration=0.1)
#gui.click()

#####################################################
##THE CODE
import pyautogui as gui
from time import sleep

#go to DISPLAY button
sleep(3)
gui.moveTo( x=30, y=152, duration=0.1)
gui.click()

#go to DOWNLOAD button
gui.moveTo(x=115, y=154, duration=0.1)
gui.click()

#go to transfere to CANVA
sleep(1.5)
gui.keyDown('ctrlleft')
gui.press('tab')
gui.keyUp('ctrlleft')
#take the image from the "galery"
gui.moveTo(x=246, y=280, duration=0.1)
gui.click()
sleep(1)
gui.press('enter')
sleep(2)

#return to the MAIN tab
gui.keyDown('ctrlleft')
gui.press('tab')
gui.keyUp('ctrlleft')
sleep(1)

#open terminal
gui.keyDown('altleft')
gui.keyDown('tab')
gui.press('altleft')
gui.write('python3 index.py')
