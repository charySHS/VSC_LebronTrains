# Region VEXcode
from vex import *

brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
left_front = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_front = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
left_rear = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_rear = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
catapult = Motor(Ports.PORT15, GearSetting.RATIO_36_1, True)
elevation_motor = Motor(Ports.PORT5, GearSetting.RATIO_36_1, True)
windshield_wiper = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)

wait(30, MSEC)

# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Chary Hyland                                           #
# 	Created:      11/30/2023, 4:54:19 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# -- Library imports
from vex import *
import math
import time

from const import *
from drivetrain import Drive_Train
from scoring_methods import Scoring_Methods


# -- Class Setup

class Main:

    def __init__(self, motor_1, motor_2, motor_3, motor_4, Motor_1, Motor_2, Motor_3, screen, controller):
        self.controller = controller
        self.drive_train = Drive_Train(motor_1, motor_2, motor_3, motor_4, screen)
        self.scoring_method = Scoring_Methods(Motor_1, Motor_2, Motor_3, screen)

    def driver_control(self):
        global Drive_Train, Scoring_Methods, vexcode_brain_precision, vexdoce_console_precision, vexcode_controller_1_precision


        self.controller.buttonL1.pressed(self.scoring_method.catapult_spin)
        self.controller.buttonL2.pressed(self.scoring_method.catapult_stop)
        self.controller.buttonB.pressed(self.scoring_method.pass_under)
        self.controller.buttonX.pressed(self.scoring_method.elevate)

        self.controller.buttonR1.pressed(self.drive_train.slow_drive)
        self.controller.buttonR2.pressed(self.drive_train.stop_drive)

        self.controller.buttonA.pressing(self.scoring_method.windshield_armed)
        self.controller.buttonA.released(self.scoring_method.windshield_dearmed)

        while True:
            self.drive_train.set_drive_speed(self.controller.axis3.position(), self.controller.axis4.position(), self.controller.axis1.position())
            wait(5, MSEC)
    
    def autonomous(self):
        self.drive_train.drive_forward()
        wait(2, SECONDS)
        self.drive_train.stop_drive()

    competition = Competition(driver_control, autonomous)

robot = Main(left_rear, right_front, left_front, right_rear, catapult, elevation_motor, windshield_wiper, brain, controller_1)





        
