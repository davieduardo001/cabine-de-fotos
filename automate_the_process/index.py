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
gui.moveTo(x=41, y=137, duration=0.1)
gui.click()

#go to DOWNLOAD button
gui.moveTo(x=125, y=137, duration=0.1)
gui.click()

#go to transfere to CANVA
sleep(1)
gui.keyDown('ctrlleft')
gui.press('tab')
gui.keyUp('ctrlleft')
#take the image from the "galery"
gui.moveTo(x=224, y=264, duration=0.1)
gui.click()
sleep(1)
gui.press('enter')
sleep(1)

#return to the MAIN tab
gui.keyDown('ctrlleft')
gui.press('tab')
gui.keyUp('ctrlleft')
sleep(1)

#open terminal
gui.keyDown('ctrlleft')
gui.keyDown('altleft')
gui.press('t')
gui.keyUp('ctrlleft')
gui.keyUp('altleft')
gui.write('python3 index.py')
