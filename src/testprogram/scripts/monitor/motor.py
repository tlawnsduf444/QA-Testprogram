#!/usr/bin/env python
import rospy
from somanet_msgs.msg import MotorStates
# I need debug mod
def callback(msg):
    rospy.set_param("motor_voltage", str(msg.motors_voltages[0]) + '\t' + str(msg.motors_voltages[1]))
    rospy.set_param("motor_current", str(msg.currents[0]) + '\t' + str(msg.currents[1]))
    rospy.set_param("motor_temperature", str(msg.temperatures[0]) + '\t' + str(msg.temperatures[1]))
    rospy.set_param("motor_board_temperatures", str(msg.boards_temperatures[0]) + '\t' + str(msg.boards_temperatures[1]))

def motor():
    motor_sub = rospy.Subscriber('/core/debug/responses/motor_states', MotorStates, callback)

def stop():
    motor_sub.unregister()