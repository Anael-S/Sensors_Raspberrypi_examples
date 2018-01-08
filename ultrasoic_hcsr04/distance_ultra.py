import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from time import sleep
import time

#mqtt connection
client = mqtt.Client()
client.connect("localhost",1883,60)
# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
trig= 24
echo = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

#GPIO.output(trig,False)
#sleep(2)
GPIO.output(trig,True)
sleep(0.00001)
GPIO.output(trig,False)

start_time = time.time()
stop_time = time.time()
while GPIO.input(echo) ==0:
    start_time = time.time()

while GPIO.input(echo) ==1:

    stop_time=time.time()


duration = stop_time - start_time
distance = (duration * 34300)/2

#distance = pulse_duration * 17150
#distance = round(distance,2)

#sensor = DistanceSensor(echo=21,trigger=24)
#distance = sensor.distance*100
try:
    while True:

        print(distance)
        client.publish('sensor/ultrasonic',distance)

except KeyboardInterrupt:
    pass
