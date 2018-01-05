import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin_signal = 18

GPIO.setup(pin_signal,GPIO.OUT)

pwm = GPIO.PWM(pin_signal,50)
pwm.start(5)
pwm.ChangeDutyCycle(7.5)
pwm.ChangeDutyCycle(10)
pwm.stop(5)

GPIO.cleanup()
