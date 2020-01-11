
import wpilib.xboxcontroller
import wpilib
import ctre
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
        self.networkTableMap = NetworkTableMap()

        
        
        

class CANMap():
    def __init__(self):
        '''
        holds mappings to all the motors in the robot
        '''
        rampRate = .2
        #rotRampRate = .2
        pid = {'controlType':ctre.WPI_TalonSRX.ControlMode.Velocity, 'feedbackDevice':0, 'sensorPhase':False, 'kMult': 7000, 'kP': .125, 'kI': 0, 'kD': .3, 'kF': 0} #These are all values to be tuned
        lifterMotors = {}
        driveMotors = {}
        '''The code below is an example of code for the SparkMax motor controllers'''
        #shooterMotors['RotMotor'] = {'channel':4, 'inverted':False, 'type':'SparkMax', 'pid':rotPid, 'motorType':MotorType.kBrushless}
        '''The code below is for controlling TalonSRX motor controllers as well as their followers'''
        driveMotors['leftMotor'] = {'channel':5, 'inverted':True,'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        driveMotors['leftFollower'] = {'channel':3, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':5, "rampRate":rampRate}
        driveMotors['leftFollowerFollower'] = {'channel':1, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':5, "rampRate":rampRate}
        
        driveMotors['rightMotor'] = {'channel':4, 'inverted':True, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        driveMotors['rightFollower'] = {'channel':2, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':4, "rampRate":rampRate}
        driveMotors['rightFollowerFollower'] = {'channel':0, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':4, "rampRate":rampRate}
        
        lifterMotors['liftMotor'] = {'channel':7, 'inverted':True, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        lifterMotors['roller'] = {'channel':8, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        lifterMotors['roller2'] = {'channel':6, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':5, "rampRate":rampRate}
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
    
