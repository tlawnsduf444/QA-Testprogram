#!/usr/bin/env python
import rospy
from gopher_std_msgs.msg import Buttons

def callback(msg):
    rospy.set_param("button", str(msg.buttons[0].is_pressed) + '\t' + str(msg.buttons[1].is_pressed) + '\t' + str(msg.buttons[2].is_pressed) + '\t' + str(msg.buttons[3].is_pressed))

def button():
    button_sub = rospy.Subscriber('/core/status/buttons', Buttons, callback)