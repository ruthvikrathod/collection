import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
GPIO.setup(16,GPIO.IN)
while True:
    input_state1=GPIO.input(12)
    input_state2=GPIO.input(16)
    print input_state1
    print input_state2
    if  (input_state1 == 0):
        print "led1 on"
        GPIO.output(18,1)
        GPIO.output(24,0)
        GPIO.output(23,0)

    elif (input_state2 == 0):
        print "led2 on"
        GPIO.output(18,0)
        GPIO.output(23,1)
        GPIO.output(24,0)
    else:
        GPIO.output(24,1)
        GPIO.output(23,0)
        GPIO.output(18,0)
        print "led 3 is on"
    time.sleep(1)
