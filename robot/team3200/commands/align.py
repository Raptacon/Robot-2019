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
        '''This button is an example and prints when you press the button'''
        print("Alignment Started")
        self.ta = self.table.getNumber('tv', None)
        if(self.ta in locals()):
            while(self.tx < -5 and self.tx > 5):
                self.tx = self.table.getNumber('tx', None)
                if(self.tx < 0):
                    print(self.tx)
                    self.dtSub.setTankDrive(-.5, .5)
                elif(self.tx > 0):
                    print(self.tx)
                    self.dtSub.setTankDrive(5, -.5)
                    