#!/usr/bin/env python
import rospy
from gopher_core_msgs.msg import BatteryState

def callback(msg):
    rospy.set_param("battery_percentage", str(msg.sensor_state.percentage))
    rospy.set_param("battery_voltage", str(msg.sensor_state.voltage))
    rospy.set_param("battery_current", str(msg.sensor_state.current))

def battery():
    battery_sub = rospy.Subscriber('/core/status/battery/raw', BatteryState, callback)