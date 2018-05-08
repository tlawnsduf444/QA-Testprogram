#!/usr/bin/env python
import rospy
__all__ = ['battery', 'bumper', 'button', 'cliff', 'motor', 'odom', 'pose', 'sonar', 'status', 'velocity', 'version']
paramlist = sorted(["battery_percentage", "battery_voltage", "battery_current", "bumper", "button", "cliff", "motor_voltage", "motor_current", "motor_temperature",
"motor_board_temperature", "odometry", "pose", "sonar", "status", "wifi", "velocity"])

for i in range(len(paramlist)):
    rospy.set_param(paramlist[i], "None")

"""if not os.path.exists("/home/yujin/qa_file/sonar_file"):
        os.makedirs("/home/yujin/qa_file/sonar_file")
    with open("/home/yujin/qa_file/sonar_file/" + filename, "a") as f:
        f.write('\t'.join([str(lst) for lst in range(1,15)]))"""

"""f.write('\t'.join([str(msg.ranges[i].range) for i in range(0,14)]))"""
    #global filename
    #filename = str(datetime.datetime.now())
    #if not os.path.exists("/home/yujin/qa_file/sonar_file"):
    ##    os.makedirs("/home/yujin/qa_file/sonar_file")
    #with open("/home/yujin/qa_file/sonar_file/" + filename, "a") as f:
    #    f.write('\t'.join([str(lst) for lst in range(1,15)]))


    #with open("/home/yujin/qa_file/sonar_file/" + filename, "a") as f:
    #    f.write('\t'.join([str(msg.ranges[i].range) for i in range(0,14)]))