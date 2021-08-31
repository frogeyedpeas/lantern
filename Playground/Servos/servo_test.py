from adafruit_servokit import ServoKit
import time 

kit = ServoKit(channels=16)

while True:
    print("entering 90 degrees")
    kit.servo[1].angle = 90 
    time.sleep(5)
    print("entering 0 degrees") 
    kit.servo[1].angle = 0 
    time.sleep(5)
