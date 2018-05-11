#!/usr/bin/env python
import rospy
import time
import os
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(msg):
    rospy.set_param("pose", str(msg.pose.pose.position.x) + '\t' + str(msg.pose.pose.position.y) + '\t' + str(msg.pose.pose.orientation.z))

def pose():
    global pose_sub
    pose_sub = rospy.Subscriber('/navi/pose', PoseWithCovarianceStamped, callback)

def stop():
    pose_sub.unregister()