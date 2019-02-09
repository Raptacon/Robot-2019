# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:00:27 2019

@author: Micro
"""

from wpilib.command.subsystem import Subsystem
import team3200

class LifterSub(Subsystem):
	def __init__(self):
		super().__init__("LifterSub")
		self.robot = team3200.getRobot()
		self.map = self.robot.map
		self.level
	
	def setLevel(self, levelSet):
		if self.levelSet == 1:
			print("Setting level to 1.")
			if self.level == 2:
				print("Level is 2.")
			else:
				print("Unknown Level Error")
		if self.levelSet == 2:
			print("Setting level to 2.")
			if self.level == 1:
				print("Level is 1.")
			else:
				print("Unknown Level Error")
		else:
			print("Unknown Designated Level Error")
