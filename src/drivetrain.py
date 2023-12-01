# -- Imports

from vex import *
from const import *
import math


# -- Class Setup

class Drive_Train:

    def __init__(self, motor_1, motor_2, motor_3, motor_4, screen):
        self.motor_1 = motor_1
        self.motor_2 = motor_2
        self.motor_3 = motor_3
        self.motor_4 = motor_4   
        self.screen = screen

        self.motor_1.spin(FORWARD)
        self.motor_2.spin(FORWARD)
        self.motor_3.spin(FORWARD)
        self.motor_4.spin(FORWARD)   

    # -- Mathematics for functionality
    def set_directional_speed(self, forward_speed=0.0, direction=0.0, clockwise_speed=0.0):

        x = forward_speed * math.sin(direction + math.pi/4)
        y = forward_speed * math.cos(direction + math.pi/4)

        self.motor_1.set_velocity(y + clockwise_speed, PERCENT)
        self.motor_2.set_velocity(y - clockwise_speed, PERCENT)
        self.motor_3.set_velocity(x + clockwise_speed, PERCENT)
        self.motor_4.set_velocity(x - clockwise_speed, PERCENT)

    def set_drive_speed(self, drive_speed=0.0, right_speed=0.0, clockwise_speed=0.0):
        
        speed = math.sqrt(right_speed * right_speed + drive_speed * drive_speed)
        theta = math.atan2(right_speed, drive_speed)
        self.set_directional_speed(speed, theta, clockwise_speed)

    # -- Directions
    def stop_drive(self):
        self.set_drive_speed(0, 0, 0)
        self.screen.print("Drivetrain Stopped")
    
    def slow_drive(self):
        self.set_drive_speed(5, 0, 0)
        self.screen.print("Drivetrain set at 50%")

    def drive_forward(self):
        self.set_drive_speed(50, 0, 0)
        self.screen.print("Drivetrain going forward")

    def drive_rotate(self):
        self.set_drive_speed(0, 0, 50)
        self.screen.print("Drivetrain rotating")

    def drive_back(self):
        self.set_drive_speed(-30, 0, 0)
        self.screen.print("Drivetrain going back")
