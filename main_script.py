# Python Project
import sys
import vex
from vex import *

#region config
brain   = vex.Brain()
motor_1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
motor_2 = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
motor_3 = vex.Motor(vex.Ports.PORT3, vex.GearSetting.RATIO36_1, False)
motor_4 = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO36_1, False)
con     = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

FWD = DirectionType.FWD

dt         = vex.Drivetrain(motor_1, motor_2, 319.1764, 272, vex.DistanceUnits.MM) #INTIALIZE DRIVE

def forward_for(distance, velo):
    global dt
    dt.drive_for(FWD, distance, vex.DistanceUnits.CM, velo)
    
def forward(velo):
    global dt
    dt.drive(FWD, velo)



#brain.screen.set_font(vex.Font.MONO_40)
#for count in range(4):
#  brain.screen.print_line(1, 'Forward')
#  
#  sys.sleep(1)
#  brain.screen.print_line(1, 'Turn Left')
#  dt.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
#  sys.sleep(1) 
#brain.screen.print_line(1, 'Finished')


#CONTROLLER REGION -------START
while con.buttonR1.pressing():
    con.set_deadband(5)
    
    buttonr1_pressed = False
    motor_5_running = 0
    
    #region actions
    while True:
    	motor_1_power = 0
    	motor_2_power = 0
    	motor_3_power = 0
    	motor_4_power = 0
    	motor_5_power = 0
    	
    	# axis1: Linear Control
    	power = con.axis1.position()
    	if power != 0:
    		motor_1_power = power
    	
    	# axis2: Linear Control
    	power = con.axis2.position()
    	if power != 0:
    		motor_2_power = power
    	
    	# buttonL1: Forward
    	if con.buttonL1.pressing():
    		motor_3_power = 100
    	
    	# buttonL2: Reverse
    	if con.buttonL2.pressing():
    		motor_4_power = -100
    	

    	
    	motor_1.spin(vex.DirectionType.FWD, motor_1_power)
    	motor_2.spin(vex.DirectionType.FWD, motor_2_power)
    	motor_3.spin(vex.DirectionType.FWD, motor_3_power)
    	motor_4.spin(vex.DirectionType.FWD, motor_4_power)
	
#endregion actions
