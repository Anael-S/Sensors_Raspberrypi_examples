import RPi.GPIO as GPIO
import time

red = 17
green = 27
blue = 22

#set up pins as OUTPUT
def setupPin(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
   
   
def turnOn(pin): 
    setupPin(pin)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    setupPin(pin)
    GPIO.output(pin,GPIO.LOW)


def redOn():
    turnOn(red)

def greenOn():
    turnOn(green)

def blueOn():
    turnOn(blue)

def magentaOn():
    turnOn(red);
    turnOn(blue);


def turnOffAll():
    turnOff(green)
    turnOff(red)
    turnOff(blue)



for i in range(0,10):

    redOn()
    time.sleep(2)
    turnOffAll()
    time.sleep(2)
    blueOn()
    time.sleep(2)
    turnOffAll()
    time.sleep(2)
    greenOn()
    time.sleep(2)
    turnOffAll()
    time.sleep(2)
    magentaOn()
    time.sleep(2)
    turnOffAll()
    time.sleep(2)
turnOffAll()

    

