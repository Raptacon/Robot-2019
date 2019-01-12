

import hal

class RobotMap():
    """
    Robot map gathers all the hard coded values needed to interface with 
    hardware into a single location
    """
    def __init__(self):
        """intilize the robot map"""
        self.motorsMap = CANMap()
        self.pneumaticsMap = PneumaticsMap()
        self.controllerMap = ControllerMap()

        
        
        

class CANMap():
    def __init__(self):
        '''
        holds mappings to all the motors in the robot
        '''
        self.shooterMotors = {}
        self.intakeMotors = {}
        driveMotors = {}
        driveMotors['leftMotor'] = 0
        driveMotors['rightMotor'] = 1
        self.driveMotors = driveMotors
        

class PneumaticsMap():
    def __init__(self):
        self.pcmCan = 1
        self.loaderOpen = 1
        self.loaderClose = 0
        
class ControllerMap():
    def __init__(self):
        '''creates two controllers for driver and shooter and assigns
        axis and buttons to joysticks'''
        driverController = {}
        auxController = {}
        
        driverController['controllerId'] = 0
        driverController['leftTread'] = 1
        
        
        if hal.isSimulation():
            driverController['rightTread'] = 3
        else:
            driverController['rightTread'] = 5
        
        driverController['voltRumble'] = 8.0
        
        self.driverController = driverController
        self.auxController = auxController
        