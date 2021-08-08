import RPI.GPIO as GPIO

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

        
    def motor_start(self, direction: bool) -> bool:
        if direction:
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)
            return True
        elif not direction:
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self,pin2, GPIO.HIGH)
            return True
        else:
            print("ahhhh non boolean")
            self.motor_stop()
            return False

    def motor_stop(self):
        GPIO.output(self, pin1, GPIO.LOW)
        GPIO.output(self, pin2, GPIO.LOW)

    def set_duty_cycle(self, duty_cycle: int):
        self.p.ChangeDutyCycle(duty_cycle)
    

class mecanum:
    def __init__(self, en, motor_front_left, motor_front_right, motor_back_left, motor_back_right):
        self.motor_front_left = motor_front_left
        self.motor_front_right = motor_front_right
        self.motor_back_left = motor_back_left
        self.motor_back_right = motor_back_right

    def forward(self):
        self.motor_front_left.motor_start(True)
        self.motor_front_right.motor_start(True)
        self.motor_back_left.motor_start(True)
        self.motor_back_right.motor_start(True)

    def backward(self):
        self.motor_front_left.motor_start(False)
        self.motor_front_right.motor_start(False)
        self.motor_back_left.motor_start(False)
        self.motor_back_right.motor_start(False)

    def leftward(self):
        self.motor_front_left.motor_start(False)
        self.motor_back_left.motor_start(True)
        self.motor_front_right.motor_start(True)
        self.motor_back_right.motor_start(False)

    def rightward(self):
        
        self.motor_front_left.motor_start(True)
        self.motor_back_left.motor_start(False)
        self.motor_front_right.motor_start(False)
        self.motor_back_right.motor_start(True)


    def base_rotation(self, direction: bool):

        self.motor_front_left.motor_start(direction)
        self.motor_front_right.motor_start(not direction)
        self.motor_back_right.motor_start(not direction)
        self.motor_back_left.motor_start(direction)


    def rotate_left(self):
        self.base_rotation(False)

    def rotate_right(self):
        self.base_rotation(True)

    #TODO DIAGONALS 

    






