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

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  
}

// VEX V5 C++ Project with Competition Template
#include "vex.h"

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// ---- END VEXCODE CONFIGURED DEVICES ----
using namespace vex;



//#region config_globals
//vex::brain Brain;
vex::motor motor_l1(vex::PORT20, vex::gearSetting::ratio18_1, false);
vex::motor motor_r1(vex::PORT11, vex::gearSetting::ratio18_1, true);
//vex::motor motor_l2(vex::PORT10, vex::gearSetting::ratio18_1, false);
//vex::motor motor_r2(vex::PORT1, vex::gearSetting::ratio18_1, true);
vex::motor motor_as1(vex::PORT9, vex::gearSetting::ratio36_1, false);
vex::motor motor_as2(vex::PORT2, vex::gearSetting::ratio36_1, true);
vex::motor motor_ah1(vex::PORT19, vex::gearSetting::ratio36_1, false);
vex::motor motor_ah2(vex::PORT12, vex::gearSetting::ratio36_1, true);

//vex::motor_group leftwheels = motor_group(motor_l1, motor_l2);
//vex::motor_group rightwheels = motor_group(motor_r1, motor_r2);

//vex::motor_group leftstrafe = motor_group(motor_r1, motor_l2);
//vex::motor_group rightstrafe = motor_group(motor_r2, motor_l1);


vex::drivetrain dt(motor_l1, motor_r1, 319.1764, 272, vex::distanceUnits::mm);

vex::controller con(vex::controllerType::primary);

//dt.driveFor(vex::directionType::fwd, 100, vex::distanceUnits::cm, 10);


//#endregion config_globals


// Creates a competition object that allows access to Competition methods.
vex::competition Competition;

void pre_auton() {
    // All activities that occur before competition start
    // Example: setting initial positions

}

void autonomous() {
    // Place autonomous code here

}

void drivercontrol() {
    // Place drive control code here, inside the loop
    double left_power = 0;
    double right_power = 0;


    while (true) {
        while(con.ButtonR1.pressing()) {

          left_power = con.Axis3.position();
          right_power = con.Axis2.position();

          motor_l1.spin(vex::directionType::fwd, left_power, velocityUnits::rpm);
          motor_r1.spin(vex::directionType::fwd, right_power, velocityUnits::rpm);


          //double power = 100;

          //while (con.ButtonLeft.pressing()) {

          //  leftstrafe.spin(vex::directionType::fwd, power, velocityUnits::rpm);
          //  rightstrafe.spin(vex::directionType::fwd, -power, velocityUnits::rpm);

          //}

          //while (con.ButtonRight.pressing()) {

          //  leftstrafe.spin(vex::directionType::fwd, -power, velocityUnits::rpm);
          //  rightstrafe.spin(vex::directionType::fwd, power, velocityUnits::rpm);

          //}

        }
        
        left_power = 0;
        right_power = 0;
        motor_l1.spin(vex::directionType::fwd, left_power, velocityUnits::rpm);
        motor_r1.spin(vex::directionType::fwd, right_power, velocityUnits::rpm);

        // This is the main loop for the driver control.
        // Each time through the loop you should update motor
        // movements based on input from the controller.

    }
}

//int main() {
    // Do not adjust the lines below

    // Set up (but don't start) callbacks for autonomous and driver control periods.
    //Competition.autonomous(autonomous);
    //Competition.drivercontrol(drivercontrol);

    // Run the pre-autonomous function.
    //pre_auton();

    // Robot Mesh Studio runtime continues to run until all threads and
    // competition callbacks are finished.
//}
