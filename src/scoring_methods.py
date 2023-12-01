# -- Imports

from vex import *
from const import *


# -- Class Setup

class Scoring_Methods:

    def __init__(self, motor_1, motor_2, motor_3, screen):
        self.motor_1 = motor_1
        self.motor_2 = motor_2
        self.motor_3 = motor_3
        self.screen = screen
        
        self.motor_1.set_velocity(100, PERCENT)
        self.motor_2.set_velocity(100, PERCENT)
        self.motor_3.set_velocity(100, PERCENT)

    # Catapult Methods
    def catapult_spin(self):
        self.motor_1.spin(FORWARD)
        self.motor_2.spin(FORWARD)
        self.screen.print("Spin Code Ran")

    def catapult_stop(self):
        self.motor_1.stop()
        self.motor_2.stop()
        self.screen.print("Stop Code Ran")

    def pass_under(self):
        self.motor_1.spin_for(FORWARD, 700, DEGREES)
        self.motor_1.set_stopping(BRAKE)
        self.screen.print("Catapult set to traverse")

    def elevate(self):
        self.motor_1.spin_for(FORWARD, 700, DEGREES)
        self.motor_2.spin_for(FORWARD, 700, DEGREES)
        self.screen.print("Elevating")

    # Other Methods
    def windshield_armed(self):
        self.motor_3.spin_for(FORWARD, 90, DEGREES)
        self.screen.print("Windshield Armed")


    def windshield_dearmed(self):
        self.motor_3.spin_for(FORWARD, -90, DEGREES)
        self.screen.print("Windshield DeArmed")
