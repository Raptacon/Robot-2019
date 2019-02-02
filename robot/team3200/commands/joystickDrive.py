# -*- coding: utf-8 -*-

from wpilib.command import Command
import hal
import team3200

class JoystickDrive(Command):
    """
    This command will read the joystick values that are used
    to control the robot drive train and then set the drivetrain subsystem
    """
    
    def __init__(self, ntSensitivity = None):
        super().__init__("Joystick Drive")
        self.robot = team3200.getRobot()
        self.requires(self.robot.dtSub)
        
        self.sensitivity = -1
        if type(ntSensitivity) != None:    
            self.sensitivity = ntSensitivity.getNumber(-1)\
        
        ntSensitivity.addListener(self.setSensitivity, 0b010100) #trying to properly deal with bitmasks or whatever. should use flags from https://robotpy.readthedocs.io/projects/pynetworktables/en/latest/api.html#networktables.NetworkTablesInstance.NotifyFlags

        
    def setSensitivity(self, entry, key, value, param):
        self.sensitivity = int(value)
        
    def getSensitivity(self):
        return self.sensitivity
    
    def execute(self):
        '''This sets up the axes on the controller to send into tankDrive'''
        dc = self.robot.driveController
        leftSide = dc.getRawAxis(1)
        if hal.isSimulation():
            rightSide = dc.getRawAxis(3) * self.sensitivity
        else:
            rightSide = dc.getRawAxis(5) * self.sensitivity
        
        self.robot.dtSub.setTankDrive(leftSide,rightSide)
