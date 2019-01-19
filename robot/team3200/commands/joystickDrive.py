# -*- coding: utf-8 -*-

from wpilib.command import Command

class JoystickDrive(Command):
    """
    This command will read the joystick values that are used
    to control the robot drive train and then set the drivetrain subsystem
    """
    
    def __init__(self, robot):
        super().__init__("Joystick Drive")
        self.robot = robot
        self.requires(self.robot.dtSub)
        self.sensitivity = -1
        
    def setSensitivity(self, newSensitivity):
        self.sensitivity = newSensitivity
        
    def getSensitivity(self):
        return self.sensitivity
    
    def execute(self):
        dc = self.robot.driveController
        leftSide = dc.getRawAxis(1) * self.sensitivity
        rightSide = dc.getRawAxis(5) * self.sensitivity
        
        self.robot.dtSub.setTankDrive(leftSide,rightSide)