# Python Project
import sys
import vex
from vex import *

#region config
brain   = vex.Brain()
motor_1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
motor_2 = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, False)
#endregion config

FWD = DirectionType.FWD

brain   = vex.Brain()
motorLeft  = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
motorRight = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
dt         = vex.Drivetrain(motorLeft, motorRight, 319.1764, 272, vex.DistanceUnits.MM)

def forward_for(distance, velo):
    global dt
    dt.drive_for(FWD, distance, vex.DistanceUnits.CM, velo)
    
def forward(velo):
    global dt
    dt.drive(FWD, velo)


forward(20)


pass

#brain.screen.set_font(vex.Font.MONO_40)
#for count in range(4):
#  brain.screen.print_line(1, 'Forward')
#  
#  sys.sleep(1)
#  brain.screen.print_line(1, 'Turn Left')
#  dt.turn_for(vex.TurnType.LEFT, 90, vex.RotationUnits.DEG)
#  sys.sleep(1) 
#brain.screen.print_line(1, 'Finished')

#
pass
