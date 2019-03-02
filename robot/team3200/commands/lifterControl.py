# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:00:38 2019

@author: Matthew McFarland
"""
from wpilib.command import InstantCommand
from wpilib.command import Command

class RaiseButton(InstantCommand):
    '''A button to raise the lifter while it is held.'''
    def __init__(self, liftSub):
        super().__init__("Raise Height")
        self.liftSub = liftSub
        
    def execute(self):
        print("Raise Lifter command")
        self.liftSub.SetLevel(50)
        
    #def end(self):
     #   self.liftSub.StopLifter()

class LowerButton(InstantCommand):
    '''A button to lower the lifter while it is held.'''
    def __init__(self, liftSub):
        super().__init__("Lower Height")
        self.liftSub = liftSub
        
    def execute(self):
        print("Lower Lifter command")
        self.liftSub.SetLevel(0)
        
    #def end(self):
     #   self.liftSub.StopLifter()

class PistonButton(InstantCommand):
    '''A button to actuate the piston.'''
    def __init__(self, pistonSub):
        super().__init__("Actuate Piston")
        self.pistonSub = pistonSub
        
    def execute(self):
        print("Piston Button Pressed")
        self.pistonSub.Activate()

class StopButton(InstantCommand):
    '''Used when the lifter buttons are released. Stops lifter motors.'''
    def __init__(self,liftSub):
        super().__init__("Stop Lifter")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.StopLifter()

class RollerIO(InstantCommand):
    '''Turns the motors on/off when pressed'''
    def __init__(self, liftSub):
        super().__init__("Toggle Roller On Off")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.RunRoller(1.0)



class StopRoller(InstantCommand):
    '''Turns the roller off'''
    def __init__(self, liftSub):
        super().__init__("Intake Stop")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.RunRoller(0)

class ForwardRoller(InstantCommand):
    '''Set roller to forwards'''
    def __init__(self, liftSub):
        super().__init__("Intake Forward")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.RunRoller(-.666)
        
class ReverseRoller(InstantCommand):
    '''Set roller to backwards'''
    def __init__(self, liftSub):
        super().__init__("Intake Backwards")
        self.liftSub = liftSub
        
    def execute(self):
        self.liftSub.RunRoller(1)
