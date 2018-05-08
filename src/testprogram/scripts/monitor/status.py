#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    rospy.set_param("status", str(msg.status)) 
    rospy.set_param("wifi", str(msg.wifi_strength))

def odom():
    status_sub = rospy.Subscriber('/sentience/reality', Reality, callback)
