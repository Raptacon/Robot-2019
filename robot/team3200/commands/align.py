# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:06:57 2019

@author: Micro
"""
from wpilib.command import InstantCommand
from networktables import NetworkTables
class AlignButton(InstantCommand):
    def __init__(self, dtSub):
        super().__init__("Align Button")
        self.table = NetworkTables.getTable("limelight")
        self.dtSub = dtSub
        
    def execute(self):
        '''This aligns the robot up to a target it sees when a button is pressed'''
        print("Alignment Started")
        if(table.getEntry('tv') == 1):
            while(self.tx < -2 and self.tx > 2):
                self.tx = self.table.getNumber('tx', None)
                if(self.tx < 0):
                    print(self.tx)
                    self.dtSub.autoTurn(-.5, .5)
                elif(self.tx > 0):
                    print(self.tx)
                    self.dtSub.autoTurn(.5, -.5)
                    