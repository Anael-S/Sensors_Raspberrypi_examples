import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
pwm = GPIO.PWM(18,50)
pwm.start(7.5)
def on_connect(self, client,data,rc):
    self.subscribe("sensor/servo")

def on_message(client,data, msg):
    topic = msg.topic
    payload = str(msg.payload.decode("utf-8" ))

    if(topic == 'sensor/servo'):
        if(payload == 'right'):
            print(" 2.5")
            pwm.ChangeDutyCycle(2.5) #turn -90i
            time.sleep(1)
        elif(payload =='neutral'):
            print("7.5")
            pwm.ChangeDutyCycle(7.5)
            time.sleep(1)
        
        elif(payload == 'left'):
            print("12.5")
            pwm.ChangeDutyCycle(12.5)
            time.sleep(1)
        else:
            print("invalid message")
        

try:
    client = mqtt.Client()  
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("localhost",1883,60)
    client.loop_forever()
# while True:
       # pwm.ChangeDutyCycle(7.5) # turn 90
       # time.sleep(1)
       # pwm.ChangeDutyCycle(2.5) # turn back 90
       # time.sleep(1)
       # pwm.ChangeDutyCycle(12.5) # turn 180
       # time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
