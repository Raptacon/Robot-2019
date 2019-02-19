# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:00:38 2019

@author: Micro
"""
from wpilib.command import InstantCommand
from wpilib.command import Command

class RaiseButton(InstantCommand):
    def __init__(self, liftSub):
        super().__init__("Raise Height")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.RaiseLevel()
        
    #def end(self):
     #   self.liftSub.StopLifter()

class LowerButton(InstantCommand):
    def __init__(self, liftSub):
        super().__init__("Lower Height")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.LowerLevel()
        
    #def end(self):
     #   self.liftSub.StopLifter()

class PistonButton(InstantCommand):
    def __init__(self, pistonSub):
        super().__init__("Actuate Piston")
        self.pistonSub = pistonSub
        
    def execute(self):
        self.pistonSub.Activate()

class StopButton(InstantCommand):
    def __init__(self,liftSub):
        super().__init__("Stop Lifter")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.StopLifter()

class RollerIO(InstantCommand):
    def __init__(self, liftSub):
        super().__init__("Toggle Roller On Off")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.RunRoller(.5)

class RollerToggle(InstantCommand):
    def __init__(self, liftSub):
        super().__init__("Toggle Intake")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.ToggleRoller()