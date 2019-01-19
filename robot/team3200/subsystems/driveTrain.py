# -*- coding: utf-8 -*-
import wpilib

from wpilib.command.subsystem import Subsystem
import wpilib.drive.differentialdrive as dd

from team3200.commands.joystickDrive import JoystickDrive 

import team3200
import team3200.motorHelper

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
        self.map = self.robot.map
        self.driveMotors = {}
        #self.followMotors = {}
        for key, motorDesc in self.map.motorsMap.driveMotors.items():
            self.driveMotors[key] = team3200.motorHelper.createMotor(motorDesc)
            print(key, motorDesc, self.driveMotors[key])
        
        #self.driveMotors['leftMotor']    = ctre.WPI_TalonSRX(0)
        #self.driveMotors['rightMotor']   = ctre.WPI_TalonSRX(1)
        #self.followMotors['leftFollower'] = ctre.WPI_TalonSRX(3)
        #self.followMotors['leftFollower'].set(ctre.wpi_talonsrx.ControlMode.Follower, 0)
        #self.followMotors['rightFollower'] = ctre.WPI_TalonSRX(2)
        #self.followMotors['rightFollower'].set(ctre.wpi_talonsrx.ControlMode.Follower, 1)
        


        self.driveTrain = dd.DifferentialDrive(self.driveMotors['leftMotor'], self.driveMotors['rightMotor'])
        
    def setTankDrive(self, leftSide, rightSide):
        self.driveTrain.tankDrive(leftSide, rightSide)
        
    def setArcadeDrive(self, speed, rot):
        self.driveTrain.arcadeDrive(speed, rot)

    def initDefaultCommand(self):
        self.setDefaultCommand(JoystickDrive(self.robot))