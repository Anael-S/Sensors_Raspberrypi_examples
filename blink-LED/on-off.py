import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt


red = 17
green = 27
blue = 22

COLOR_PIN = green



def on_connect(self,client, userdata, rc):
    #print("Connected with result code "+str(rc))
    self.subscribe("sensor/lightstate")
    self.subscribe("sensor/lightcolor")


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

def on_message(client,userdata,message):
    topic = message.topic
    turnOffAll()
    print("callback message {}".format(topic))
    payload = str(message.payload.decode("utf-8"))
    if(topic == 'sensor/lightstate'):
        if(payload == 'on'):
           redOn()
           print("on")
        elif(payload == 'off'):
            turnOffAll()
    elif(topic == 'sensor/lightcolor'):
        turnOffAll()
        if(payload == 'red'):
            redOn()
        elif(payload == 'green'):
            greenOn()
        elif(payload =='magenta'):
            magentaOn()
        elif(payload == 'blue'):
            blueOn()
        else: redOn()    
    else:
        print("command does not exist")








if __name__=="__main__":
    try:

        #connect to the broker 
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("localhost",1883,60)
        client.loop_forever()

    except KeyboardInterrupt:
        turnOffAll()



