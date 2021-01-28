import RPi.GPIO as GPIO
import time

def init_setup():
  print('initializing gpio setup')
  GPIO.setmode(GPIO.BOARD)

  # Laser - set port
  global laser
  laser = 13
  GPIO.setup(laser,GPIO.OUT)

  # Servo 1+2 - set ports+pwm
  global servo1
  global servo2
  GPIO.setup(11,GPIO.OUT)
  GPIO.setup(12,GPIO.OUT)
  servo1 = GPIO.PWM(11,50)
  servo2 = GPIO.PWM(12,50)
  servo1.start(0)
  servo2.start(0)

  # set duty-cycle
  global duty
  duty = 2
  print('initialization done.')

def moveTo(x, y, laser_on):
  print ('moving to x:%s, y:%s, laser_on:%s'%(x,y,laser_on))
  # turn off laser before moving
  #GPIO.output(laser, False)
  servo1.ChangeDutyCycle(duty+(x/18))
  servo2.ChangeDutyCycle(duty+(y/18))
  GPIO.output(laser, laser_on)
  time.sleep(0.5)
  servo1.ChangeDutyCycle(0)
  servo2.ChangeDutyCycle(0)

def cleanup():
  GPIO.output(laser, False)
  servo1.stop()
  servo2.stop()
  GPIO.cleanup()
  print ("Goodbye")