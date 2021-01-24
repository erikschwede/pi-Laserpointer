import RPi.GPIO as GPIO
import time

def init_setup():
  print('initializing gpio setup')
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(11,GPIO.OUT)
  global servo1
  servo1 = GPIO.PWM(11,50)
  servo1.start(0)
  global duty
  duty = 2
  print('initialization done.')

def moveTo(x, y, laser_on):
  print ('moving to x:%s, y:%s, laser_on:%s'%(x,y,laser_on))
  servo1.ChangeDutyCycle(2+(x/18))
  time.sleep(0.5)
  servo1.ChangeDutyCycle(0)

def cleanup():
  servo1.stop()
  GPIO.cleanup()
  print ("Goodbye")