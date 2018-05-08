#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    rospy.set_param("odometry", str(msg.pose.pose.position.x) + '\t' + str(msg.pose.pose.position.y) + '\t' + str(msg.pose.pose.orientation.z)) 

def odom():
    odom_sub = rospy.Subscriber('/core/odom', Odometry, callback)