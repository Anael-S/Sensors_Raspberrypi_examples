from hcsr04sensor import sensor
import paho.mqtt.client as mqtt
from time import sleep




def main():
    client = mqtt.Client()
    client.connect("localhost",1883,60)
    trig_pin = 12
    echo_pin = 16
    value = sensor.Measurement(trig_pin, echo_pin)
    try:
        raw_measurement = value.raw_distance()
        metric_distance = value.distance_metric(raw_measurement)
    except Exception: raise     
    print("The Distance = {} centimeter".format(metric_distance))
    if metric_distance is not None:
            client.publish('sensor/ultrasonic',str(metric_distance))

if __name__ == "__main__":
    while True:
         main()
