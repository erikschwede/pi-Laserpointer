import controls
import time

controls.init_setup()
controls.moveTo(0,120,True)
time.sleep(1)
controls.moveTo(180,100,True)
time.sleep(1)
controls.moveTo(90,120,False)
time.sleep(1)
controls.cleanup()