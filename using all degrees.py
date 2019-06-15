import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
P = GPIO.PWM(7, 50)
P.start(7.5)
try:
    while True:
        input_state1=GPIO.input(24)
        if(input_state1 == 0):
            P.ChangeDutyCycle(2.5) #Neutral (0 degree's)
            time.sleep(2)
            print"Servo Rotates 0 degree's"

        else:
              P.ChangeDutyCycle(12.5) #180 degree's
              print "Servo Rotates 180 degree's"
              time.sleep(1)
        


except KeyboardInterrupt:
    P.stop()
        
