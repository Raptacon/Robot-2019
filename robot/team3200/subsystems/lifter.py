# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:00:27 2019

@author: Micro
"""
from enum import IntEnum
import time

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

class LifterSub(Subsystem):
	def __init__(self):
		super().__init__("LifterSub")
		self.robot = team3200.getRobot()
		self.map = self.robot.map
		self.level = 0
		self.isIntake = False
		self.lifterMotors = {}
		for key, motorDesc in self.map.motorsMap.lifterMotors.items():
			self.lifterMotors[key] = team3200.motorHelper.createMotor(motorDesc)
			print(key, motorDesc, self.lifterMotors[key])
			
	
	def RaiseLevel(self):
		self.lifterMotors['liftMotor'].set(.5)
		for i in range(0, 5):
			print(i)
		self.lifterMotors['liftMotor'].set(0)
		if self.level < 7:
			++self.level

	def LowerLevel(self):
		self.lifterMotors['liftMotor'].set(-.3)
		for i in range(0, 5):
			print(i)
		self.lifterMotors['liftMotor'].set(0)
		if self.level > 0:
			--self.level
			
	def ToggleRoller(self):
		self.isIntake = not self.isIntake
		
	def RunRoller(self, speed):
		if self.isIntake:
			speed = not speed
		if(self.lifterMotors['roller'].get() == 0):
			self.lifterMotors['roller'].set(speed)
		else:
			self.lifterMotors['roller'].set(0)