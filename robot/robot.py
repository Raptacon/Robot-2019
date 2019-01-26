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
from team3200.commands.lights import GoodGood
import team3200.subsystems.driveTrain



#import sys       
def exit(retval):
    pass
#    sys.exit(retval)

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        team3200.getRobot = lambda x=0:self
        self.map = team3200.robotMap.RobotMap()
        self.networkTableInit()
        self.dtSub = team3200.subsystems.driveTrain.DriveTrainSub()
        self.driveController = wpilib.XboxController(0)
        self.createButtons()
        
    def networkTableInit(self):
        NetworkTables.initialize(server = 'roborio-3200-frc.local')
        
        self.liveWindowTable = NetworkTables.getTable('LiveWindow')
        self.liveWindowTable.putNumber('Sensitivity', -1)
        

    def createButtons(self):
        self.lightButton = JoystickButton(self.driveController, 3)
        self.lightButton.whenPressed(Lights())
        self.goodGoodButton = JoystickButton(self.driveController, 6)
        self.goodGoodButton.whenPressed(GoodGood())


if __name__ == '__main__':
    try:
        #patch no exit error if not running on robot
        try:
            print(wpilib._impl.main.exit)
        except:
            wpilib._impl.main.exit = exit
            
        #fixes simulation rerun errors.
        wpilib.DriverStation._reset()

        #patch sim
        import sim.ui
        import sim.pygame_joysticks
        import pyfrc.sim
        import pyfrc.sim.pygame_joysticks
        pyfrc.sim.SimUI = sim.ui.SimUI
        pyfrc.sim.pygame_joysticks.UsbJoysticks = sim.pygame_joysticks.UsbJoysticks
    except Exception as err:
            print("Failed to patch runtime. Error", err)
    
    wpilib.run(MyRobot,physics_enabled=True)
