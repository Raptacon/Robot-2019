# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 09:58:59 2019

@author: Micro
"""
from wpilib.command.instantcommand import InstantCommand
from wpilib.command import Command
class ShooterControl(Command):
	def __init__(self, robot):
		super().__init__("Shooter Controls")
		self.robot = robot
		self.requires(self.robot.shooterSub)
		
		
	def execute(self):
		ac = self.robot.auxController
		flyWheelSpeed = ac.getRawAxis(self.robot.map.controllerMap.auxController['flyWheelTrigger'])
		rotSpeed = ac.getRawAxis(self.robot.map.controllerMap.auxController['rotAxis'])
		self.robot.shooterSub.setShooterSpeed(flyWheelSpeed, rotSpeed)
		
class IntakeButton(InstantCommand):
	def __init__(self, shooterSub):
		super().__init__("Intake Button")
		self.shooterSub = shooterSub
	
	def execute(self):
		self.shooterSub.toggleIntake()