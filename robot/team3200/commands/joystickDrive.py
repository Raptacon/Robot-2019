# -*- coding: utf-8 -*-

from wpilib.command import Command
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
        
        self.sensitivity = 1.6
        if ntSensitivity != None:    
            self.sensitivity = ntSensitivity.getNumber(-1)
            ntSensitivity.addListener(self.networkTableSensListener, 0b010100) #trying to properly deal with bitmasks or whatever. should use flags from https://robotpy.readthedocs.io/projects/pynetworktables/en/latest/api.html#networktables.NetworkTablesInstance.NotifyFlags

    def setSensitivity(newSens, self):
        self.sensitvity = newSens
        
    def networkTableSensListener(self, entry, key, value, param):
        self.setSensitivity(value)
        
    def getSensitivity(self):
        return self.sensitivity
    
    def execute(self):
        '''This sets up the axes on the controller to send into tankDrive'''
        dc = self.robot.driveController
        leftTread = dc.getRawAxis(self.robot.map.controllerMap.driverController['leftTread'])
        rightTread = dc.getRawAxis(self.robot.map.controllerMap.driverController['rightTread'])
		
        if (leftTread < 0):
            leftSide = -1*((-leftTread) ** self.sensitivity)
        else:
            leftSide = leftTread ** self.sensitivity
        
        if (rightTread < 0):
            rightSide = -1*((-rightTread) ** self.sensitivity)
        else:
            rightSide = rightTread ** self.sensitivity
        
        self.robot.dtSub.setTankDrive(leftSide,rightSide)
