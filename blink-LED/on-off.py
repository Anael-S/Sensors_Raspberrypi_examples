import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt


red = 17
green = 27
blue = 22




def on_connect(self,client, userdata, rc):
    #print("Connected with result code "+str(rc))
    self.subscribe("sensor/lightstate")
    self.subscribe("sensor/lightcolor")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red,GPIO.OUT)
    GPIO.setup(green,GPIO.OUT)
    GPIO.setup(blue,GPIO.OUT) 
   
def turnOn(pin): 
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
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
    print("callback message {}".format(topic))
    payload = str(message.payload.decode("utf-8"))
   
    if(topic == 'sensor/lightstate'):
        if(payload == 'on'):

            greenOn()
            client.publish('sensor/lightstate',"ondone")
            client.publish('sensor/lightcolor',"greendone")
            return
        elif(payload == 'off'):
            turnOffAll()
            client.publish('sensor/lightstate','offdone')
            return
    elif(topic == 'sensor/lightcolor'):
        if(payload == 'red'):
            turnOffAll()
            redOn()
            client.publish("sensor/lightcolor",'reddone')
            return
        elif(payload == 'blue'):
            turnOffAll()
            blueOn()
            client.publish("sensor/lightcolor",'bluedone')
            return
        elif(payload =='magenta'):
            turnOffAll()
            magentaOn()
            client.publish("sensor/lightcolor",'magentadone')
            return 
        elif(payload == 'green'):
            turnOffAll()
            greenOn()
            client.publish("sensor/lightcolor",'greendone')
            return
        else: print("INVALID:doesnot understand the payload message!i")    
    else:
        print("command doesnt exist")








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



