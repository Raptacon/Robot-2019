
import wpilib.xboxcontroller
import wpilib
import ctre
import hal
import rev


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
        self.networkTableMap = NetworkTableMap()

        
        
        

class CANMap():
    def __init__(self):
        '''
        holds mappings to all the motors in the robot
        '''
        encoder = wpilib.Encoder(0, 1)

        rampRate = .2
        #rotRampRate = .20
        pid = {'controlType': wpilib.PIDBase.PIDSourceType(1), 'feedbackDevice':0, 'sensorPhase':False, 'kPreScale': 7000, 'kP': 0.000027, 'kI': 50, 'kD': 0, 'kF': 0.000001} #These are all values to be tuned
        #pidSparkVelocity = {'controlType':rev.ControlType.kVelocity, 'feedbackDevice':0, 'sensorPhase':False, 'kPreScale': 5000, 'kP': 0.0001,kI': 0.000001, 'kD': 0, 'kF': 0} #These are all values to be tuned (Prescale is a multiplier, position is measured in 1/6 rotations.)
        #pidSparkPosition = {'controlType':rev.ControlType.kPosition, 'feedbackDevice':1, 'sensorPhase':False, 'kPreScale': 6, 'kP': 0.1, 'kI': 0.000001, 'kD':0.3, 'kF': 0}
        lifterMotors = {}
        driveMotors = {}
        '''The code below is an example of code for the SparkMax motor controllers'''
        #shooterMotors['RotMotor'] = {'channel':4, 'inverted':False, 'type':'SparkMax', 'pid':rotPid, 'motorType':MotorType.kBrushless}
        '''The code below is for controlling TalonSRX motor controllers as well as their followers'''
        driveMotors['leftMotor'] = {'channel': 2, 'inverted': True, 'type':'CANTalon', 'pid': pid, 'encoderSource': encoder}
        
        driveMotors['rightMotor'] = {'channel':1, 'inverted':False, 'type':'CANTalon', 'pid':None, "rampRate":rampRate}
        driveMotors['rightFollower'] = {'channel':9, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':1, "rampRate":rampRate}
        driveMotors['rightFollowerFollower'] = {'channel':0, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':1, "rampRate":rampRate}
        
        lifterMotors['liftMotor'] = {'channel':7, 'inverted':True, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        lifterMotors['roller'] = {'channel':8, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        lifterMotors['roller2'] = {'channel':6, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel': 7, "rampRate":rampRate}
        angleMotor = {'channel':13, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        
        self.driveMotors = driveMotors
        self.lifterMotors = lifterMotors
        self.angleMotor = angleMotor

class PneumaticsMap():
    def __init__(self):
        self.pcmCan = 1
        self.forwardChannel = 0
        self.reverseChannel = 1
    
class ControllerMap():
    def __init__(self):
        '''creates two controllers and assigns
        axis and buttons to joysticks'''
        driverController = {}
        auxController = {}
        
        driverController['controllerId'] = 0
        auxController['controllerId'] = 1
        
        driverController['leftTread'] = 1
        if hal.isSimulation():
            driverController['rightTread'] = 3
        else:
            driverController['rightTread'] = 5

        driverController['ledToggle'] = wpilib.XboxController.Button.kX
        driverController['alignButton'] = wpilib.XboxController.Button.kA
        driverController['leftButton'] = wpilib.XboxController.Button.kBumperLeft
        driverController['rightButton'] = wpilib.XboxController.Button.kBumperRight
        
        auxController['LowerButton'] = wpilib.XboxController.Button.kBumperLeft
        auxController['RaiseButton'] = wpilib.XboxController.Button.kBumperRight
        auxController['StopButton'] = wpilib.XboxController.Button.kY
        auxController['PistonButton'] = wpilib.XboxController.Button.kX
        auxController['RollerIO'] = wpilib.XboxController.Button.kA
        auxController['RollerToggle'] = wpilib.XboxController.Button.kB

        
        driverController['voltRumble'] = 8.0
        
        self.driverController = driverController
        self.auxController = auxController
        
class NetworkTableMap():
    def __init__(self):
        '''
        Create and set default variables for the network tables, defaulted to if we don't create a different file with our saved variables
        '''
        self.networkTableValues = { }
        
        #To create a new network value, create it with the format of "networkTableValues["NameOfValue"] = Value
        self.networkTableValues["ControllerSensitivity"] = -1
        self.networkTableValues["VoltageRumbleBeginsAt"] = 0 #no idea about what value might need to be
    
