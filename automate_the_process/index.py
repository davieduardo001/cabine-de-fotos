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
gui.moveTo(x=37, y=193, duration=0.1)
gui.click()

#go to DOWNLOAD button
gui.moveTo(x=110, y=190, duration=0.1)
gui.click()

#go to DOWNLOADS
gui.keyDown('alt')
gui.press('tab')
gui.keyUp('alt')

#copy the photo
gui.moveTo(x=333, y=172, duration=0.5)
gui.click()
gui.keyDown('ctrl')
gui.press('x')
gui.keyUp('ctrl')

#paste the photo
gui.keyDown('alt')
gui.press('tab')
gui.press('tab')
gui.keyUp('alt')
gui.moveTo(x=1198, y=712, duration=2.5)
gui.keyDown('ctrl')
gui.press('v')
gui.keyUp('ctrl')



