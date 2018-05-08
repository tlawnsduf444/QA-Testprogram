#!/usr/bin/env python
import rospy
from somanet_msgs.msg import Info
import versionR

def version():
    rospy.set_param("version", str(rospy.wait_for_message('/core/status/info', Info)) + versionR.rplidar())