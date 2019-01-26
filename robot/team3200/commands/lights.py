# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:52:42 2019
@author: Raptor3200
"""

from wpilib.command import InstantCommand

from networktables import NetworkTables

from enum import IntEnum

class LedMode(IntEnum):
    kAUTO = 0
    kOFF = 1
    kBLINK = 2
    kON = 3

class GoodGood(InstantCommand):
    def __init__(self):
        super().__init__("GoodGood")
        
    def execute(self):
        print("Made by Matthew McFarland")

class Lights(InstantCommand):
    
    def __init__(self):
        super().__init__("Lights")
        
    def execute(self):
        print("Lights Toggled")
        table = NetworkTables.getTable("limelight")
        lightNum = table.getNumber('ledMode', None)
        if lightNum == LedMode.kOFF:
            table.putNumber('ledMode', LedMode.kON)
        else:
            table.putNumber('ledMode', LedMode.kOFF)
            