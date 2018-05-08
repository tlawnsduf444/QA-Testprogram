#!/usr/bin/env python
import rospy
from gopher_core_msgs.msg import Info

def rplidar():
    rplidar1 = '\n\nFront Lidar\n' + str(rospy.wait_for_message('/core/rplidar/info', Info)) 
    try:
        rplidar2 = '\nLeft Lidar\n' + str(rospy.wait_for_message('/core/rplidar/left/info', Info))
        rplidar3 = '\nRight Lidar\n' + str(rospy.wait_for_message('/core/rplidar/right/info', Info))
    except:
        rplidar2 = "\nNone"
        rplidar3 = "\nNone"
    return rplidar1 + rplidar2 + rplidar3