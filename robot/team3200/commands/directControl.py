# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:56:42 2019

@author: Micro
"""


from wpilib.command import Command

class Automove(Command):
	def __init__(self, dtSub, controller):
		self.dtSub = dtSub
		self.controller = controller
		
	def execute(self):
		padAngle = self.controller.getPOV(0)
		if padAngle == 0:
			self.dtSub.autoTurn(1, 1)
		if padAngle == 90:
			self.dtSub.autoTurn(-1, 1)
		if padAngle == 180:
			self.dtSub.autoTurn(-1, -1)
		if padAngle == 270:
			self.dtSub.autoTurn(1, -1)