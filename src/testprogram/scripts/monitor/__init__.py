#!/usr/bin/env python
import rospy
import os
__all__ = ['battery', 'bumper', 'button', 'cliff', 'motor', 'odom', 'pose', 'sonar', 'status', 'velocity', 'version']
paramlist = sorted(["battery_percentage", "battery_voltage", "battery_current", "bumper", "button", "cliff", "motor_voltage", "motor_current", "motor_temperature",
"motor_board_temperatures", "odometry", "pose", "sonar", "status", "wifi", "velocity"])

for i in range(len(paramlist)):
    rospy.set_param(paramlist[i], "None")