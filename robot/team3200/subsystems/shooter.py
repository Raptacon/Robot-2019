# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:16:51 2019

@author: Micro
"""
import wpilib.drive.differentialdrive as dd
from wpilib.command.subsystem import Subsystem

from team3200.commands.shooterControl import ShooterControl 
import team3200

class ShooterSub(Subsystem):
	def __init__(self):
		super().__init__("ShooterSub")
		self.robot = team3200.getRobot()
		self.map = self.robot.map
		self.isIntake = False
		self.shooterMotors = {}
		for key, motorDesc in self.map.motorsMap.shooterMotors.items():
			self.shooterMotors[key] = team3200.motorHelper.createMotor(motorDesc)
			print(key, motorDesc, self.shooterMotors[key])
		self.shooterTrain = dd.DifferentialDrive(self.shooterMotors['LeftFlyWheel'], self.shooterMotors['RotMotor'])
		
	def initDefaultCommand(self):
		self.setDefaultCommand(ShooterControl(self.robot))
	
	def toggleIntake(self):
		self.isIntake = not self.isIntake
		
	def setShooterSpeed(self, flyWheelSpeed, rotSpeed):
		if self.isIntake:
			flyWheelSpeed = -flyWheelSpeed
		self.shooterTrain.tankDrive(flyWheelSpeed, rotSpeed)
		
		
