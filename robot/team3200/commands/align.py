# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:06:57 2019

@author: Matthew McFarland
"""

from wpilib.command import Command
from wpilib.command import InstantCommand
from networktables import NetworkTables

class LeftTurn(Command):
    def __init__(self, dtSub):
        super().__init__("Left Turn")
        self.dtSub = dtSub
        
    def execute(self):
        self.dtSub.autoTurn(-.5, .5)
        
class RightTurn(Command):
    def __init__(self, dtSub):
        super().__init__("Right Turn")
        self.dtSub = dtSub
        
    def execute(self):
        self.dtSub.autoTurn(.5, -.5)
        
class AlignButton(InstantCommand):
    def __init__(self, dtSub):
        super().__init__("Align Button")
        self.gripTable = NetworkTables.getTable("GRIP")
        self.dtSub = dtSub
        self.aligning = True
        
    def execute(self):
        '''This aligns the robot up to a target it sees when a button is pressed'''
        
        self.aligning = not self.aligning # designed to "toggle" this command, so that you can continuously align, until you click the button again
        areasArray = NetworkTables.getEntry("/vision/yellow_stuff/Areas").get() # areasArray = the value of the entry "Areas"
        for a in range (0, len(areasArray)-1): # looping through all values in the array
            pass # I was originally thinking of using an if loop "if it's too far to thr right, rotate clockwise. if it's too far left, rotate counterclockwise. otherwise, do nothing" More accurately, I would really want to calculate angle that the bot would have to move based on the location of the item in the frame. (note: it doesn't matter how far away something is because you rotate on the spot) my two concerns would be changes in camera position, and thus, angle, and then running it countinuously. 
                

class DriveStraight(Command):
    def __init__(self, dtSub):
        super().__init__("Right Turn")
        self.dtSub = dtSub
        
    def execute(self):
        self.dtSub.autoTurn(.5, .5)