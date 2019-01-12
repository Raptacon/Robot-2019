import pygame
from hal_impl.data import hal_data

class UsbJoysticks(object):
    
    def __init__(self, ui):
        pygame.init()
        
        self.ui = ui
        
        self.joysticks = self.getUsbJoystickList()
        self.initJoystickList(self.joysticks)
        
    def getUsbJoystickList(self):
        joysticks = []
        
        for i in range(pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
        return joysticks
    
    def initJoystickList(self, joystickList):
        for i, joystick in enumerate(joystickList):
            joystick.init()
            if i < len(hal_data['joysticks']):
                hal_data['joysticks'][i]['name'] = joystick.get_name()
        
    def update(self):
        pygame.event.get()
        
        for i in range(len(self.joysticks)):
            joystick = self.joysticks[i]
            ui_joystick = self.ui.joysticks[i]
            
            ui_axes = ui_joystick[0]

            for axis in range(joystick.get_numaxes()):
                if axis == 6:
                    break
                
                ui_current_axis = ui_axes[axis]
                value = joystick.get_axis(axis)
                
                #xbox controller trigger fix
                #map axis 2+ to axis 3 Left Trigger 0-1
                #map axis 2- to axis 5 Right Trigger 0-1
                if axis == 2:
                    axisValue = value
                    value = 0 if axisValue <= 0 else axisValue
                    ui_current_axis.set_value(value)
                    #map axis 5 to
                    ui_current_axis = ui_axes[5]
                    value = 0 if axisValue >= 0 else abs(axisValue)
                    
                
                ui_current_axis.set_value(value)
                
            ui_buttons = ui_joystick[1]
            for button in range(joystick.get_numbuttons()):
                if button == 10:
                    break
                
                ui_current_button = ui_buttons[button]
                ui_current_button = ui_current_button[0]
                
                value = joystick.get_button(button)
                
                if value == False:
                    ui_current_button.deselect()
                else:
                    ui_current_button.select()
