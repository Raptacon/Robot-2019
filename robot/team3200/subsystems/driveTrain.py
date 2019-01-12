# -*- coding: utf-8 -*-
import wpilib

from wpilib.command.subsystem import Subsystem
import wpilib.drive.differentialdrive as dd

from commands.joystickDrive import JoystickDrive 

import team3200

import ctre

class DriveTrainSub(Subsystem):
    '''
    This is the subsystem to controller the robots wheels.
    '''
    
    def __init__(self):
        '''Initilizes the subsystem, gets the motors, 
        creates the drivetrain mixer
        '''
        super().__init__("DriveTrainSub")
        self.robot = team3200.getRobot();
        self.driveMotors = {}
        self.driveMotors['leftMotor'] = ctre.WPI_TalonSRX(0)
        self.driveMotors['rightMotor'] = ctre.WPI_TalonSRX(1)


        self.driveTrain = dd.DifferentialDrive(**self.driveMotors)
        
    def setTankDrive(self, leftSide, rightSide):
        self.driveTrain.tankDrive(leftSide, rightSide)
        
    def setArcadeDrive(self, speed, rot):
        self.driveTrain.arcadeDrive(speed, rot)

    def initDefaultCommand(self):
        self.setDefaultCommand(JoystickDrive(self.robot))