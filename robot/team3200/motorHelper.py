    # -*- coding: utf-8 -*-

import rev
import ctre 

import logging
log = logging.getLogger("console") #These logs were set up for testing, should not be persistent, please delete if you see these and I forgot
log.setLevel(logging.DEBUG)

def createMotor(motorDescp):
    #Might want more motor types for set up
    '''This is where all motors are set up'''
    if motorDescp['type'] == 'CANTalon':
        #if we want to use the built in encoder set it here
        if('pid' in motorDescp) and motorDescp['pid'] != None:
            motor = WPI_TalonFeedback(motorDescp)
            motor.setupPid()
        else:
            motor = ctre.wpi_talonsrx.WPI_TalonSRX(motorDescp['channel'])

    elif motorDescp['type'] == 'CANTalonFollower':
        motor =ctre.wpi_talonsrx.WPI_TalonSRX(motorDescp['channel'])
        motor.set(mode = ctre.wpi_talonsrx.ControlMode.Follower, demand0 = motorDescp['masterChannel'])
        
    elif motorDescp['type'] == 'SparkMax':
        '''This is where SparkMax motor controllers are set up'''
        if 'pid' in motorDescp and motorDescp['pid'] != None:
            motor = SparkMaxFeedback(motorDescp)
            motor.setupPid()
        else:
            motor = SparkMaxFeedback(motorDescp)
    
    else:
        print("Unknown Motor")
    
    if 'inverted' in motorDescp: 
        motor.setInverted(motorDescp['inverted'])
    
    if 'currentLimits' in motorDescp:
        currentLimits = motorDescp['currentLimits']
        absMax = currentLimits['absMax']
        absMaxTimeMs = currentLimits['absMaxTimeMs']
        nominalMaxCurrent = currentLimits['maxNominal']
        motor.configPeakCurrentLimit(absMax,10)
        motor.configPeakCurrentDuration(absMaxTimeMs,10)
        motor.configContinuousCurrentLimit(nominalMaxCurrent,10)
        motor.enableCurrentLimit(True)

    if 'rampRate' in motorDescp:
        motor.configOpenLoopRamp(motorDescp['rampRate'],10)    
    
    return motor
#motor=map.CAN.driveMotors[name]
#            motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
#            motors[name]=ctre.wpi_talonsrx.WPI_TalonSRX(motor['channel'])
#            
#            motors[name] = wpilib.PWMSpeedController(motor['channel'])
#            
        

class WPI_TalonFeedback(ctre.wpi_talonsrx.WPI_TalonSRX):
    def __init__(self,motorDescription):
        ctre.wpi_talonsrx.WPI_TalonSRX.__init__(self,motorDescription['channel'])
        self.motorDescription = motorDescription
        
    def setupPid(self,motorDescription = None):
        if not motorDescription:
            motorDescription = self.motorDescription
        if not 'pid' in self.motorDescription:
            print("Motor channel %d has no PID"%(self.motorDescription['channel']))
            return
        pid = self.motorDescription['pid']
        self.controlType = pid['controlType']
        self.configSelectedFeedbackSensor(pid['feedbackDevice'], 0, 10)
        self.setSensorPhase(pid['sensorPhase'])
        self.pidControlType = pid['controlType']
        
        self.kPreScale = pid['kPreScale']
        
        #/* set the peak, nominal outputs, and deadband */
        self.configNominalOutputForward(0, 10)
        self.configNominalOutputReverse(0, 10)
        self.configPeakOutputForward(1, 10)
        self.configPeakOutputReverse(-1, 10)
        
        
        self.configVelocityMeasurementPeriod(self.VelocityMeasPeriod.Period_1Ms,10) 
        #/* set closed loop gains in slot0 */
        self.config_kF(0, pid['kF'], 10)
        self.config_kP(0, pid['kP'], 10)
        self.config_kI(0, pid['kI'], 10)
        self.config_kD(0, pid['kD'], 10)
        
    def set(self, speed):
        return ctre.wpi_talonsrx.WPI_TalonSRX.set(self, self.controlType, speed * self.kPreScale)
            
class SparkMaxFeedback(rev.CANSparkMax):
    def __init__(self,motorDescription):
        self.motorDescription = motorDescription
        rev.CANSparkMax.__init__(self, self.motorDescription['channel'], self.motorDescription['motorType'])
        self.setInverted(self.motorDescription['inverted'])

    def setupPid(self):
        if not 'pid' in self.motorDescription:
            print("Motor channel %d has no PID"%(self.motorDescription['channel']))
            return
        self.pid = self.motorDescription['pid']
        pid = self.pid
        self.pidControlType = rev.ControlType(pid['controlType'])
        self.encoder = self.getEncoder()
        
        self.kPreScale = pid['kPreScale']
        self.PIDController = self.getPIDController() #creates pid controller

        self.PIDController.setP(pid['kP'], pid['feedbackDevice'])
        self.PIDController.setI(pid['kI'], pid['feedbackDevice'])
        self.PIDController.setD(pid['kD'], pid['feedbackDevice'])
        self.PIDController.setFF(pid['kF'], pid['feedbackDevice'])

        self.PIDController.setOutputRange(-1, 1, pid['feedbackDevice'])
        self.PIDController.setReference(0 , self.pidControlType, pid['feedbackDevice']) #Sets the control type to velocity on the pid slot we passed in
    
    def set(self, speed):
        log.debug("error = %f", (speed*self.pid['kPreScale'])-self.encoder.getVelocity())
        return self.PIDController.setReference(speed*self.pid['kPreScale'], self.pidControlType)
