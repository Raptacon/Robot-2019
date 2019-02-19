# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:00:27 2019

@author: Micro
"""
from enum import IntEnum

class Level(IntEnum):
    kFloor = 0
    kLowPanel = 1
    kLowBall = 2
    kBallCargo = 3
    kMidPanel = 4
    kMidBall = 5
    kHighPanel = 6
    kHighBall = 7

from wpilib.command.subsystem import Subsystem
import team3200
import wpilib

class LifterSub(Subsystem):
    def __init__(self):
        super().__init__("LifterSub")
        self.robot = team3200.getRobot()
        self.map = self.robot.map
        self.level = 2
        self.acc = .6
        self.intakeSpd = 1
        self.lifterMotors = {}
        for key, motorDesc in self.map.motorsMap.lifterMotors.items():
            self.lifterMotors[key] = team3200.motorHelper.createMotor(motorDesc)
            print(key, motorDesc, self.lifterMotors[key])
            
    
    def StopLifter(self):
        '''Stops the lifter'''
        self.lifterMotors['liftMotor'].set(0)
    
    def RaiseLevel(self):
        '''Raises the lifter'''
        if self.level < Level.kHighBall:
            #self.voltage = 60
            self.lifterMotors['liftMotor'].set(self.acc)
            #wpilib.Timer.delay(.75)
            #self.lifterMotors['liftMotor'].set(0)

    def LowerLevel(self):
        '''Lowers the lifter'''
        if self.level > Level.kFloor:
            #self.voltage = -60
            self.lifterMotors['liftMotor'].set(-self.acc)
            #wpilib.Timer.delay(.4)
            #self.lifterMotors['liftMotor'].set(0)
            
            
    def ToggleRoller(self):
        '''Toggles the roller's direction'''
        self.intakeSpd = -self.intakeSpd
        
    def RunRoller(self, speed):
        '''Toggles the roller on/off.'''
        if(self.lifterMotors['roller'].get() == 0):
            self.lifterMotors['roller'].set(speed * self.intakeSpd)
        else:
            self.lifterMotors['roller'].set(0)
            
from wpilib import DoubleSolenoid
class PlatePiston(Subsystem):
    def __init__(self):
        super().__init__("Plate Piston")
        self.robot = team3200.getRobot()
        self.map = self.robot.map.pneumaticsMap
        self.platePiston = DoubleSolenoid(self.map.pcmCan, self.map.forwardChannel, self.map.reverseChannel)
        
    def Activate(self):
        if self.platePiston.get() == DoubleSolenoid.Value.kReverse:
            self.platePiston.set(DoubleSolenoid.Value.kForward)
            print("Piston Forwards")
        #wpilib.Timer.delay(1)
        elif self.platePiston.get() == DoubleSolenoid.Value.kForward:
            self.platePiston.set(DoubleSolenoid.Value.kReverse)
            print("Piston Backwards")
        #wpilib.Timer.delay(1)