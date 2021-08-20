import RPi.GPIO as GPIO
import time 

class dc_motor:
    def __init__(self, en: int, pin1: int, pin2: int, pwm=1000, intensity=75): #this could really be just 1 pin but its two for some reason atm
        self.en = en
        self.pin1 = pin1
        self.pin2 = pin2
        self.pwm=pwm
        self.intensity = intensity

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(en, GPIO.OUT)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)

        GPIO.output(pin1, GPIO.LOW)
        GPIO.output(pin2, GPIO.LOW)
        self.p = GPIO.PWM(en, pwm)
        self.p.start(intensity)

        
    def motor_start(self, direction: bool):
        if direction:
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
        elif not direction:
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self.pin2, GPIO.HIGH)
        else:
            print("ahhhh non boolean")
            self.motor_stop()

    def motor_stop(self):
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.LOW)

    def set_duty_cycle(self, duty_cycle: int):
        self.p.ChangeDutyCycle(duty_cycle)
    

class mecanum:
    def __init__(self, motor_front_left, motor_front_right, motor_back_left, motor_back_right, wait_time: int):
        self.motor_front_left = motor_front_left
        self.motor_front_right = motor_front_right
        self.motor_back_left = motor_back_left
        self.motor_back_right = motor_back_right
        self.wait_time = wait_time
        self.motion_type = None #by default the mecanum is stopped 


    def evaluate_state(self):
        if self.motion_type != None and self.motion_type != "BLOCK":
            motion_type = self.motion_type
            self.motion_type = "BLOCK"
            getattr(self, motion_type)()
            self.motion_type = None #once we are done running the method we can then free up the robot for more instructions

    def __wait__(self):
        time.sleep(self.wait_time)
        self.stop()

    def __vertical__(self, direction: bool):
        self.motor_front_left.motor_start(direction)
        self.motor_front_right.motor_start(direction)
        self.motor_back_left.motor_start(direction)
        self.motor_back_right.motor_start(direction)
        self.__wait__()

    def __sideward__(self, direction: bool):
        self.motor_front_left.motor_start(direction)
        self.motor_front_right.motor_start(not direction)
        self.motor_back_left.motor_start(not direction)
        self.motor_back_right.motor_start(direction)
        self.__wait__()

    def __base_rotation__(self, direction: bool):
        self.motor_front_left.motor_start(direction)
        self.motor_front_right.motor_start(not direction)
        self.motor_back_right.motor_start(not direction)
        self.motor_back_left.motor_start(direction)
        self.__wait__()
    
    def __diagonal_left__ (self, direction: bool):
        self.motor_front_left.motor_stop()
        self.motor_front_right.motor_start(direction)
        self.motor_back_left.motor_start(direction)
        self.motor_back_right.motor_stop()
        self.__wait__() 

    def __diagonal_right__(self, direction: bool):
        self.motor_front_left.motor_start(direction)
        self.motor_front_right.motor_stop()
        self.motor_back_left.motor_stop()
        self.motor_back_right.motor_start(direction)
        self.__wait__() 

    def stop(self):
        self.motor_front_left.motor_stop()
        self.motor_front_right.motor_stop()
        self.motor_back_left.motor_stop()
        self.motor_back_right.motor_stop()

    def forward(self):
        print("driving forward")
        self.__vertical__(True)

    def backward(self):
        print("driving backward")
        self.__vertical__(False)

    def leftward(self):
        print("driving leftward")
        self.__sideward__(False)

    def rightward(self):
        print("driving rightward")
        self.__sideward__(True)

    def rotate_left(self):
        print("rotating left")
        self.__base_rotation__(False)

    def rotate_right(self):
        print("rotating right")
        self.__base_rotation__(True)

    def diagonal_left_forward(self):
        print("diagonal left forward")
        self.__diagonal_left__(True)

    def diagonal_right_backward(self):
        print("diagonal right backward")
        self.__diagonal_left__(False)

    def diagonal_right_forward(self):
        print("diagonal right forward")
        self.__diagonal_right__(True)

    def diagonal_left_backward(self):
        print("diagonal left backward")
        self.__diagonal_right__(False)


    


if __name__ == '__main__':

    print("is this being called!")
    FRONT_LEFT = dc_motor(2,3,4)
    BACK_LEFT = dc_motor(14,18,15)
    FRONT_RIGHT = dc_motor(17,27,22)
    BACK_RIGHT = dc_motor(10,11,9)

    print(FRONT_LEFT, BACK_LEFT, FRONT_RIGHT, BACK_RIGHT) 

    DRIVING_BASE = mecanum(FRONT_LEFT, FRONT_RIGHT, BACK_LEFT, BACK_RIGHT, 1)

    DRIVING_BASE.stop()


    DRIVING_BASE.forward()

    input("enter to continue, backward next: ")

    DRIVING_BASE.backward()

    input("enter to continue, leftware next: ")

    DRIVING_BASE.leftward()

    input("enter to continue, rightward next: ")

    DRIVING_BASE.rightward()

    input("enter to continue, diagonal left next: ")

    DRIVING_BASE.diagonal_left_forward()

    input("enter to continue, diagonal right next: ")

    DRIVING_BASE.diagonal_right_forward()

    input("enter to toncintue, digonal left backward nexT: ")

    DRIVING_BASE.diagonal_left_backward()

    input("enter to continue, diagonal right backward next: ")

    DRIVING_BASE.diagonal_right_backward()

    input("enter to continue, rotate left next: ")

    DRIVING_BASE.rotate_left()

    input("enter to continue, rotate right next: ")

    DRIVING_BASE.rotate_right()
