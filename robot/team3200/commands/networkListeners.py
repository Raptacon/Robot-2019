# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 18:59:11 2019

@author: Raptor3200
"""

from networktables import NetworkTables

class NetworkListeners():
    '''
    Creates and calls all network listeners
    '''
    
    def __init__(self):
        self.table = NetworkTables.getTable("Custom")
        
    def ChangeTable(self, TableName):
        self.table = NetworkTables.getTable(TableName)
        
    def TestCalledFunction(key, value, isNew):
        print("\n--" + str(key))
        print("--" + str(value))

        
    NetworkTables.addEntryListener(TestCalledFunction, False, "/Custom/ControllerSensitivity")
    