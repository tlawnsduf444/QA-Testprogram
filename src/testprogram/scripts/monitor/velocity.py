#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    rospy.set_param("velocity", str(msg.twist.twist.linear.x)[:4] + '\t' + str(msg.twist.twist.angular.z)[:4])

def velocity():
    velocity_sub = rospy.Subscriber('/core/odom', Odometry, callback)

def stop():
    velocity_sub.unregister()