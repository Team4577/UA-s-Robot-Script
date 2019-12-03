# Python Project
import sys
import vex
from vex import *

#region config
brain   = vex.Brain()
motor_1 = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
motor_2 = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)
motor_3 = vex.Motor(vex.Ports.PORT19, vex.GearSetting.RATIO36_1, False)
motor_4 = vex.Motor(vex.Ports.PORT12, vex.GearSetting.RATIO36_1, False)
dt      = vex.Drivetrain(motor_1, motor_2, 319.1764, 272, vex.DistanceUnits.MM) #INTIALIZE DRIVE
con     = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

FWD = DirectionType.FWD

#T-Pose to asset dominance
brain.screen.draw_rectangle(215,141,16,100) #RLeg
brain.screen.draw_rectangle(231,141,16,100) #LLeg
brain.screen.draw_rectangle(50, 50, 170, 17) #RArm
brain.screen.draw_rectangle(242, 50, 170, 17) #LArm
brain.screen.draw_circle(230,25,25) #head
brain.screen.draw_rectangle(216,50,30,100) #body


def forward_for(distance, velo):
    global dt
    dt.drive_for(FWD, distance, vex.DistanceUnits.CM, velo)
    
def forward(velo):
    global dt
    dt.drive(FWD, velo)

forward_for(10, 10)

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

while True:
    
    con.set_deadband(5)
    
    buttonr1_pressed = False
    motor_5_running = 0
    
    while con.buttonR1.pressing():
    
    
    #region actions
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
    
    
    while not con.buttonR1.pressing():
        motor_1_power = 0
    	motor_2_power = 0
    	motor_3_power = 0
    	motor_4_power = 0
    	motor_5_power = 0
