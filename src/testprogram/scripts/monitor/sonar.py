#!/usr/bin/env python
import rospy
from gopher_std_msgs.msg import Ranges

def callback(msg):
    rospy.set_param("sonar", '\t'.join([str(msg.ranges[i].range) for i in range(0,14)]))

def sonar():
    sonar_sub = rospy.Subscriber('/core/sonars', Ranges, callback)

def stop():
    sonar_sub.unregister()