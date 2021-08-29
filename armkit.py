from adafruit_servokit import ServoKit

class ArmKit:
    def __init__(self):
        self.ServoKit = ServoKit(channels=16)
        self.Grabber = self.ServoKit.servo[0]
        self.WristRotater = self.ServoKit.servo[1]
        self.WristAngle = self.ServoKit.servo[2]
        self.MotionState = None
        self.Amount = 0
        #TODO add height adjustment for arm

        #self.Grabber.angle = 10 #can be used to set the angle to a fixed angle  

    def grabber_change(self, angle):
        if self.Grabber.angle + angle >= 180:
            self.Grabber.angle = 180

        elif self.Grabber.angle + angle <= 0:
            self.Grabber.angle = 0

        else:
            self.Grabber.angle += angle 

    def wrist_rotate(self, angle):
        if self.WristRotater.angle + angle >= 90:
            self.WristRotater.angle = 90

        elif self.WristRotater.angle + angle <= 0:
            self.WristRotater.angle = 0

        else:
            self.WristRotater.angle += angle


    def wrist_flexion(self, angle):
        if self.WristAngle.angle + angle <= 90:
            self.WristAngle.angle = 90

        elif self.WristAngle.angle + angle <= 0:
            self.WristAngle.angle=0

        else:
            self.WristAngle.angle += angle 


    def evaluate_state(self):
        if self.MotionState != None and self.MotionState != "BLOCKED":
            MotionState = self.MotionState
            self.MotionState = "BLOCKED"
            changeToExecute = getattr(self, MotionState)
            changeToExecute(self.Amount)
            self.MotionState = None


