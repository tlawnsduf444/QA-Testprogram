#!/usr/bin/env python
import rospy
from gopher_std_msgs.msg import Bumpers

def callback(msg):
    rospy.set_param("bumper", str(msg.bumpers[1].is_pressed) + '\t' + str(msg.bumpers[4].is_pressed))

def bumper():
    battery_sub = rospy.Subscriber('/core/bumper', Bumpers, callback)