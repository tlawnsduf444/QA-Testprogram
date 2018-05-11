#!/usr/bin/env python
import rospy
from gopher_std_msgs.msg import Ranges

def callback(msg):
    rospy.set_param("cliff", '\t'.join([str(msg.ranges[i].range) for i in range(0,6)])) 

def cliff():
    cliff_sub = rospy.Subscriber('/core/psd_bottom', Ranges, callback)

def stop():
    cliff_sub.unregister()