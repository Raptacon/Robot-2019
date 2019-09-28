# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:00:38 2019

@author: Micro
"""
from wpilib.command import InstantCommand
locked = False
class RaiseButton(InstantCommand):
	def __init__(self, liftSub):
		super().__init__("Raise Height")
		self.liftSub = liftSub
		
	def execute(self):
		if locked!=True:
			self.liftSub.RaiseLevel()
		

class LowerButton(InstantCommand):
	def __init__(self, liftSub):
		super().__init__("Lower Height")
		self.liftSub = liftSub
		
	def execute(self):
		if locked != True:
			self.liftSub.LowerLevel()
		
class StopButton(InstantCommand):
	def __init__(self,liftSub):
		super().__init__("Stop Lifter")
		self.liftSub = liftSub
		
	def execute(self):
		if locked!=True:
			self.liftSub.StopLifter()
		
class LockToggle(InstantCommand):
	def __init__(self,liftSub):
		super().__init__("Lock Lifter")
		self.liftSub = liftSub
	def execute(self):
		global locked
		if(locked == True):
			locked = False
		else:
			locked = True
			self.liftSub.LockLifter()
#class PistonButton(InstantCommand):
#	def __init__(self, pistonSub):
#		super().__init__("Actuate Piston")
#		self.pistonSub = pistonSub
#		
#	def execute(self):
#		self.pistonSub.Activate()

class RollerIO(InstantCommand): #change name and refactor rollerio and rollertoggle
	def __init__(self, liftSub):
		super().__init__("Toggle Roller On Off")
		self.liftSub = liftSub
		
	def execute(self):
		self.liftSub.RunRoller(.8)

class RollerToggle(InstantCommand):
	def __init__(self, liftSub):
		super().__init__("Toggle Intake")
		self.liftSub = liftSub
		
	def execute(self):
		self.liftSub.InRoller(.8)
		
class RollerStop(InstantCommand):
	def __init__(self, liftSub):
		super().__init__("Turn off roller")
		self.liftSub = liftSub
		
	def execute(self):
		self.liftSub.StopRoller()