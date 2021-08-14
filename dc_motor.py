import RPI.GPIO as GPIO
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
        self.p = GPIO.pwm(en, pwm)
        self.p.start(intensity)

        
    def motor_start(self, direction: bool, wait_time: int):
        if direction:
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
            time.sleep(wait_time)
            self.motor_stop()
        elif not direction:
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self,pin2, GPIO.HIGH)
            time.sleep(wait_time)
            self.motor_stop()
        else:
            print("ahhhh non boolean")
            self.motor_stop()

    def motor_stop(self):
        GPIO.output(self, pin1, GPIO.LOW)
        GPIO.output(self, pin2, GPIO.LOW)

    def set_duty_cycle(self, duty_cycle: int):
        self.p.ChangeDutyCycle(duty_cycle)
    

class mecanum:
    def __init__(self, en, motor_front_left, motor_front_right, motor_back_left, motor_back_right, wait_time: int):
        self.motor_front_left = motor_front_left
        self.motor_front_right = motor_front_right
        self.motor_back_left = motor_back_left
        self.motor_back_right = motor_back_right
	self.wait_time = wait_time

    def __vertical__(self, direction: bool):
        self.motor_front_left.motor_start(direction, self.wait_time)
        self.motor_front_right.motor_start(direction, self.wait_time)
        self.motor_back_left.motor_start(direction, self.wait_time)
        self.motor_back_right.motor_start(direction, self.wait_time)

    def __sideward__(self, direction: bool):
        self.motor_front_left.motor_start(direction, self.wait_time)
        self.motor_front_right.motor_start(not direction, self.wait_time)
        self.motor_back_left.motor_start(not direction, self.wait_time)
        self.motor_back_right.motor_start(direction, self.wait_time)

    def __base_rotation__(self, direction: bool):

        self.motor_front_left.motor_start(direction, self.wait_time)
        self.motor_front_right.motor_start(not direction, self.wait_time)
        self.motor_back_right.motor_start(not direction, self.wait_time)
        self.motor_back_left.motor_start(direction, self.wait_time)
    
    def __diagonal_left__ (self, direction: bool):
        self.motor_front_left.motor_stop()
        self.motor_front_right.motor_start(direction, self.wait_time)
        self.motor_back_left.motor_start(direction, self.wait_time)
        self.motor_back_right.motor_stop()
       

    def __diagonal_right__(self, direction: bool):
        self.motor_front_left.motor_start(direction, self.wait_time)
        self.motor_front_right.motor_stop()
        self.motor_back_left.motor_stop()
        self.motor_back_right.motor_start(direction, self.wait_time)
        

    def stop():
        self.motor_front_left.motor_stop()
        self.motor_front_right.motor_stop()
        self.motor_back_left.motor_stop()
        self.motor_back_right.motor_stop()

    def forward(self):
        self.__vertical__(True)

    def backward(self):
        self.__vertical__(False)

    def leftward(self):
        self.__sideward__(False)

    def rightward(self):
        self.__sideward__(True)

    def rotate_left(self):
        self.__base_rotation__(False)

    def rotate_right(self):
        self.__base_rotation__(True)

    def diagonal_left_forward(self):
        self.__diagonal_left__(True)

    def diagonal_right_backward(self):
        self.__diagonal_left__(False)

    def diagonal_right_forward(self):
        self.__diagonal_right__(True)

    def diagonal_right_backward(self):
        self.__diagonal_right__(True)


    






