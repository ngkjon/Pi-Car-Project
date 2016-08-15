# A simple internet-chat application

import network
import sys
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

from time import sleep

GPIO.setmode(GPIO.BOARD)
run=True
#wr
a=16
b=18
c=22
#wl
d=19
e=21
f=23
#setup
GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)

GPIO.setup(d,GPIO.OUT)
GPIO.setup(e,GPIO.OUT)
GPIO.setup(f,GPIO.OUT)
#methods
def fw():
    rightfw()
    leftfw()
def rv():
    rightrv()
    leftrv()
#FW rightW
def rightfw():
    GPIO.output(a,GPIO.HIGH)
    GPIO.output(b,GPIO.LOW)
    GPIO.output(c,GPIO.HIGH)
#FW leftW
def leftfw():
    GPIO.output(d,GPIO.HIGH)
    GPIO.output(e,GPIO.LOW)
    GPIO.output(f,GPIO.HIGH)


#stop
def halt():
    GPIO.output(c,GPIO.LOW)
    GPIO.output(f,GPIO.LOW)

#RV rightW
def rightrv():
    GPIO.output(a,GPIO.LOW)
    GPIO.output(b,GPIO.HIGH)
    GPIO.output(c,GPIO.HIGH)
#RV leftW
def leftrv():
    GPIO.output(d,GPIO.LOW)
    GPIO.output(e,GPIO.HIGH)
    GPIO.output(f,GPIO.HIGH)

def heard(phrase):
  print("Receive: " + phrase)
  if (phrase=="halt"):
        halt()
        run=False
  elif (phrase=="w"):
        halt()
        fw()
  elif (phrase=="f"):
        halt()
  elif (phrase=="s"):
        halt()
        rv()
  elif (phrase=="a"):
        #halt()
        fw()
        rightfw()
        leftrv()
  elif (phrase=="d"):
        #halt()
        fw()
        leftfw()
        rightrv()
        
if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)

while network.isConnected() & run:
  #phrase = raw_input() #python2
  phrase = input() # python3
  print("Send: " + phrase)
  network.say(phrase)
halt()
GPIO.cleanup()