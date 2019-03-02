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

from team3200.commands.align import RightTurn
from team3200.commands.align import LeftTurn
from team3200.commands.align import AlignButton
from team3200.commands import lifterControl
import team3200.subsystems.driveTrain
import team3200.subsystems.lifter
import team3200.subsystems.healthMonitor

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self): 
        '''This is where the robot code starts.'''
        team3200.getRobot = lambda x=0:self
        self.map = team3200.robotMap.RobotMap()
        self.networkTableInit()
        self.dtSub = team3200.subsystems.driveTrain.DriveTrainSub()

        self.liftSub = team3200.subsystems.lifter.LifterSub()
        self.pistonSub = team3200.subsystems.lifter.PlatePiston()
        self.driveController = wpilib.XboxController(self.map.controllerMap.driverController['controllerId'])
        self.auxController = wpilib.XboxController(self.map.controllerMap.auxController['controllerId'])

        self.controllerInit()

        self.healthMonitor = team3200.subsystems.healthMonitor.HealthMonitor()
    
    def networkTableInit(self):
        '''This sets up the network tables and adds a variable called sensitivity'''
        NetworkTables.initialize(server = 'roborio-3200-frc.local')
        self.liveWindowTable = NetworkTables.getTable('Custom')
        
        for k, v in self.map.networkTableMap.networkTableValues.items():
            #K for key, V for value
            self.liveWindowTable.putNumber(k, v)
        
        

    def controllerInit(self):
        self.driveController = wpilib.XboxController(self.map.controllerMap.driverController['controllerId'])
        self.auxController = wpilib.XboxController(self.map.controllerMap.auxController['controllerId'])

        self.lightButton = JoystickButton(self.driveController, self.map.controllerMap.driverController['ledToggle'])
        self.lightButton.whenPressed(Lights())
        self.leftButton = JoystickButton(self.driveController, self.map.controllerMap.driverController['leftButton'])
        self.leftButton.whileActive(LeftTurn(self.dtSub))
        self.rightButton = JoystickButton(self.driveController, self.map.controllerMap.driverController['rightButton'])
        self.rightButton.whileHeld(RightTurn(self.dtSub))
        self.alignButton = JoystickButton(self.driveController, self.map.controllerMap.driverController['alignButton'])
        self.alignButton.whenPressed(AlignButton(self.dtSub))
        
        self.raiseButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['RaiseButton'])
        self.raiseButton.whenPressed(lifterControl.RaiseButton(self.liftSub))
        self.lowerButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['LowerButton'])
        self.lowerButton.whenPressed(lifterControl.LowerButton(self.liftSub))
        self.stopButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['StopButton'])
        self.stopButton.whenPressed(lifterControl.StopButton(self.liftSub))
        self.pistonButton = JoystickButton(self.auxController, self.map.controllerMap.auxController['PistonButton'])
        self.pistonButton.whenPressed(lifterControl.PistonButton(self.pistonSub))
        self.rollerIO = JoystickButton(self.auxController, self.map.controllerMap.auxController['RollerIO'])
        self.rollerIO.whenPressed(lifterControl.RollerIO(self.liftSub))
        self.rollerToggle = JoystickButton(self.auxController, self.map.controllerMap.auxController['RollerToggle'])
        self.rollerToggle.whenPressed(lifterControl.RollerToggle(self.liftSub))

    def driveInit(self):
        self.dtSub = team3200.subsystems.driveTrain.DriveTrainSub()
        sensName = "ControllerSensitivity"
        if sensName in self.map.networkTableMap.networkTableValues:
            
            sensEntry = self.liveWindowTable.getEntry(sensName)
            jDrive = team3200.commands.joystickDrive.JoystickDrive(sensEntry)
            self.dtSub.setDefaultCommand(jDrive)
        
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

