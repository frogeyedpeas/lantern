# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

#first motor set up
en1 = 2
in1 = 3
in2 = 4

in3 = 14
in4 = 15
en2 = 18


temp1=1

GPIO.setmode(GPIO.BCM)

#left motor
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en1,1000)


#right motor
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p2 = GPIO.PWM(en2, 1000)


p.start(75)
p2.start(75)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    


def motor_go(firstWire, secondWire, direction=True):
    if direction == True:
        GPIO.output(firstWire, GPIO.HIGH)
        GPIO.output(secondWire, GPIO.LOW)

    elif direction == False:
        GPIO.output(firstWire, GPIO.LOW)
        GPIO.output(secondWire, GPIO.HIGH)

    else:
        print("HOLY SHIT NON BOOLEAN INCOMING")

def motor_stop(firstWire, secondWire):
    GPIO.output(firstWire, GPIO.LOW)
    GPIO.output(secondWire, GPIO.LOW)

if __name__ == '__main__':

    while(1):

        x=input()
        

        if x=='s1':
            print("stop first motor")
            motor_stop(in1, in2)
            x='z'

        elif x=='s2':
            print("stop second motor")
            motor_stop(in3, in4)
            x = 'z'

        elif x=='f1':
            print("motor1 forward")
            motor_go(in1, in2, True)
            x='z'

        elif x=='f2':
           print("moto2 forward")
           motor_go(in3, in4, True)
           x = 'z'
        elif x=='b':
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            temp1=0
            x='z'

        elif x=='l':
            print("low")
            p.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            p.ChangeDutyCycle(50)
            x='z'

        elif x=='h1':
            print("high")
            p.ChangeDutyCycle(75)
            x='z'

        elif x =='h2':
            print("motor 2 is now high")
            p2.ChangeDutyCycle(75)
            x='z'
         
        
        elif x=='e':
            GPIO.cleanup()
            print("GPIO Clean up")
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
