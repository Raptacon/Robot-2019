'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import team3200
import wpilib
from networktables import NetworkTables
from wpilib.buttons.joystickbutton import JoystickButton
import commandbased
from team3200.commands.lights import Lights
from team3200.commands.lights import ExampleButton
from team3200.commands.align import AlignButton
import team3200.subsystems.driveTrain
import team3200.subsystems.healthMonitor

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self): 
        '''This is where the robot code starts.'''
        team3200.getRobot = lambda x=0:self
        self.map = team3200.robotMap.RobotMap()
        self.networkTableInit()
        self.driveInit();
        self.driveController = wpilib.XboxController(0)
        self.controllerInit()
        self.healthMonitor = team3200.subsystems.healthMonitor.HealthMonitor()
    
    def networkTableInit(self):
        '''This sets up the network tables and adds a variable called sensitivity'''
        NetworkTables.initialize(server = 'roborio-3200-frc.local')
        
        self.liveWindowTable = NetworkTables.getTable('LiveWindow')
        self.liveWindowTable.putNumber('Sensitivity', -1)
        

    def controllerInit(self):
        self.driveController = wpilib.XboxController(self.map.controllerMap.driverController['controllerId'])
        self.auxController = wpilib.XboxController(self.map.controllerMap.auxController['controllerId'])
        self.lightButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['ledToggle'])
        self.lightButton.whenPressed(Lights())
        self.exampleButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['exampleButton'])
        self.exampleButton.whenPressed(ExampleButton())
        self.alignButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['alignButton'])
        self.alignButton.whenPressed(AlignButton())

    def driveInit(self):
        self.dtSub = team3200.subsystems.driveTrain.DriveTrainSub()

    
    def testPeriodic(self):
        while(self.isTest()):
            self.dtSub.setTankDrive(.25, .25)
            


def exit(retval):
    pass           
if __name__ == '__main__':
    try:
        #patch no exit error if not running on robot
        try:
            print(wpilib._impl.main.exit)
        except:
            wpilib._impl.main.exit = exit
            
        #fixes simulation rerun errors.
        #todo verify this causes no issues on robot
        wpilib.DriverStation._reset()

        #patch simulation
        #we update the simluation files to ours. If we update WPIlib these may break
        import sim.ui
        import sim.pygame_joysticks
        import pyfrc.sim
        import pyfrc.sim.pygame_joysticks
        pyfrc.sim.SimUI = sim.ui.SimUI
        pyfrc.sim.pygame_joysticks.UsbJoysticks = sim.pygame_joysticks.UsbJoysticks
    except Exception as err:
            print("Failed to patch runtime. Error", err)
    
    wpilib.run(MyRobot,physics_enabled=True)
