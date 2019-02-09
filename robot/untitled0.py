# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:13:19 2019

@author: jackr
"""

data = bytes(b'\xbbYY\xcf\x002\x01\x07\x00\xbbYY\xcf\x001\x01\x07\x00\xbaYY\xcf\x002\x01\x07\x00\xbbYY\xcf\x00')
print(data)
header = bytes([0x59, 0x59])
print(data.strip(header))
    