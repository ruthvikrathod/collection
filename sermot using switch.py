import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(14, GPIO.IN)
P = GPIO.PWM(7, 50)
P.start(7.5)
try:
    while True:
        input_state=GPIO.input(14)
        if (input_state == 0):
           GPIO.output(23, 1)
           print "ledon"
           time.sleep(2)
           GPIO.output(23, 0)
           print "ledoff"
           time.sleep(2)
           P.ChangeDutyCycle(7.5) #Neutral (90 degree's)
           print"Servo Rotates 90 degree's"
           time.sleep(2)
        else:
            GPIO.output(20, 1)
            print "ledon"
            time.sleep(2)
            GPIO.output(20, 0)
            print "ledoff"
            time.sleep(2)
            P.ChangeDutyCycle(12.5) #180 degree's
            print "Servo Rotates 180 degree's"
            time.sleep(2)
        
        


except KeyboardInterrupt:
    P.stop()
        
