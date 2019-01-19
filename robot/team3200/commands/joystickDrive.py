# -*- coding: utf-8 -*-

from wpilib.command import Command
import hal
class JoystickDrive(Command):
    """
    This command will read the joystick values that are used
    to control the robot drive train and then set the drivetrain subsystem
    """
    
    def __init__(self, robot):
        super().__init__("Joystick Drive")
        self.robot = robot
        self.requires(self.robot.dtSub)
        
    def execute(self):
        dc = self.robot.driveController
        leftSide = dc.getRawAxis(1)
        if hal.isSimulation():
            rightSide = -dc.getRawAxis(3)
        else:
            rightSide = -dc.getRawAxis(5)
        
        self.robot.dtSub.setTankDrive(leftSide,rightSide)
        