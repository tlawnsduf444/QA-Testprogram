#!/usr/bin/env python
import rospy
from gopher_sentience_msgs.msg import Reality

def callback(msg):
    rospy.set_param("status", str(msg.status)) 
    rospy.set_param("wifi", str(msg.wifi_strength))

def status():
    status_sub = rospy.Subscriber('/sentience/reality', Reality, callback)

def stop():
    status_sub.unregister()