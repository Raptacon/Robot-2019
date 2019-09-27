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
import wpilib
import team3200
class LifterSub(Subsystem):
    def __init__(self):
        super().__init__("LifterSub")
        self.robot = team3200.getRobot()
        self.map = self.robot.map
        self.level = 0
        self.intakeSpd = 1
        self.lifterMotors = {}
        for key, motorDesc in self.map.motorsMap.lifterMotors.items():
            self.lifterMotors[key] = team3200.motorHelper.createMotor(motorDesc)
            print(key, motorDesc, self.lifterMotors[key])
		#self.angleMotor = team3200.motorHelper.createMotor(self.map.motorsMap.angleMotor)#creates test angle motor; for learning encoders

	
    def StopLifter(self):
        print(self.level)
        self.lifterMotors['liftMotor'].set(-0.001)
	
    def RaiseLevel(self):
        #if self.level < Level.kHighBall:
            self.lifterMotors['liftMotor'].set(.5)

    def LowerLevel(self):
		
        #print(self.angleMotor.getQuadraturePosition())
		#self.angleMotor.setQuadraturePosition(128)
        #Inserted code above to help with troubleshooting the encoders. This allows us to get the quadrature counts to then reset the counts to 128
        #if self.level > Level.kFloor:
            self.lifterMotors['liftMotor'].set(-.5)
			
			
    def ToggleRoller(self):
        self.intakeSpd = -self.intakeSpd
		
    def RunRoller(self, speed):
        self.lifterMotors['roller'].set(speed * self.intakeSpd)
            
    def InRoller(self, speed):
        self.lifterMotors['roller'].set(speed * self.intakeSpd * -1)
	
    def StopRoller(self):
    	self.lifterMotors['roller'].set(0)
			
from wpilib import DoubleSolenoid
class PlatePiston(Subsystem):
	def __init__(self):
		super().__init__("Plate Piston")
		self.robot = team3200.getRobot()
		self.map = self.robot.map.pneumaticsMap
		self.platePiston = DoubleSolenoid(self.map.pcmCan, self.map.forwardChannel, self.map.reverseChannel)
		
	def Activate(self):
		self.platePiston.set(DoubleSolenoid.Value.kForward)
		print("Piston Forwards")
		wpilib.Timer.delay(1)
		self.platePiston.set(DoubleSolenoid.Value.kReverse)
		print("Piston Backwards")
		wpilib.Timer.delay(1)