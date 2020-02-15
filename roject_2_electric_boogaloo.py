// To complete the VEXcode V5 Text project upgrade process, please follow the
// steps below.
// 
// 1. You can use the Robot Configuration window to recreate your V5 devices
//   - including any motors, sensors, 3-wire devices, and controllers.
// 
// 2. All previous code located in main.cpp has now been commented out. You
//   will need to migrate this code to the new "int main" structure created
//   below and keep in mind any new device names you may have set from the
//   Robot Configuration window. 
// 
// If you would like to go back to your original project, a complete backup
// of your original (pre-upgraded) project was created in a backup folder
// inside of this project's folder.

// ---- START VEXCODE CONFIGURED DEVICES ----
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;




//#region config_globals
//vex::brain Brain;
vex::motor motor_l1(vex::PORT20, vex::gearSetting::ratio18_1, false);
vex::motor motor_r1(vex::PORT11, vex::gearSetting::ratio18_1, true);
vex::motor motor_l2(vex::PORT10, vex::gearSetting::ratio18_1, false);
vex::motor motor_r2(vex::PORT1, vex::gearSetting::ratio18_1, true);
vex::motor motor_as1(vex::PORT9, vex::gearSetting::ratio36_1, false);
vex::motor motor_as2(vex::PORT2, vex::gearSetting::ratio36_1, true);
vex::motor motor_ah1(vex::PORT19, vex::gearSetting::ratio36_1, false);
vex::motor motor_ah2(vex::PORT12, vex::gearSetting::ratio36_1, true);

vex::motor motor_ap(vex::PORT1, vex::gearSetting::ratio36_1, false);  



vex::controller con(vex::controllerType::primary);



//#endregion config_globals


// Creates a competition object that allows access to Competition methods.
vex::competition Competition;

void pre_auton() {
    // All activities that occur before competition start
    // Example: setting initial positions

}

void autonomous() {
  motor_as1.setBrake(vex::brakeType::hold);
  motor_as2.setBrake(vex::brakeType::hold);
  motor_as1.spinTo(90, vex::rotationUnits::deg);
  motor_as2.spinTo(90, vex::rotationUnits::deg);
  //motor_ap.spinTo(double rotation, rotationUnits units)


}

void drivercontrol() {
    // Place drive control code here, inside the loop
    double left_power = 0; //Left-power
    double right_power = 0; //Right-power
    double arm_seeds = 0;
    double arm_seedh = 0;
    double as = 10; //shoulders
    double ah = 100; //intae/hands

      motor_as1.setBrake(vex::brakeType::hold);
  motor_as2.setBrake(vex::brakeType::hold);

    while (true) {

        left_power = con.Axis3.position();
        right_power = con.Axis2.position();

        motor_l1.spin(vex::directionType::fwd, left_power, velocityUnits::rpm);
        motor_r1.spin(vex::directionType::fwd, right_power, velocityUnits::rpm);
        


        // This is the main loop for the driver control.
        // Each time through the loop you should update motor
        // movements based on input from the controller.
        




        

        //joystick is being wasted on forward/backward movement
        if (con.ButtonL1.pressing()) {
          arm_seeds = as;
        }
        else if (con.ButtonL2.pressing()) {
          arm_seeds = -as;
        }
        if(!con.ButtonL1.pressing() and !con.ButtonL2.pressing()){
          arm_seeds = 0;
        }

        motor_as1.spin(vex::directionType::fwd, arm_seeds, velocityUnits::rpm);
        motor_as2.spin(vex::directionType::fwd, arm_seeds, velocityUnits::rpm);


        //Intae/hands
        if (con.ButtonR1.pressing()) {
          arm_seedh = ah;
        }
        else if (con.ButtonR2.pressing()) {
          arm_seedh = -ah;
        }
        if (!con.ButtonR1.pressing() and !con.ButtonR2.pressing()){
          arm_seedh = 0;
        }

        motor_ah1.spin(vex::directionType::fwd, arm_seedh, velocityUnits::rpm);
        motor_ah2.spin(vex::directionType::fwd, arm_seedh, velocityUnits::rpm);

    }
    
   
    
    
    
    
}

int main() {
    // Do not adjust the lines below

    // Set up (but don't start) callbacks for autonomous and driver control periods.
    Competition.autonomous(autonomous);
    Competition.drivercontrol(drivercontrol);

    // Run the pre-autonomous function.
    pre_auton();

    // Robot Mesh Studio runtime continues to run until all threads and
    // competition callbacks are finished.
}


