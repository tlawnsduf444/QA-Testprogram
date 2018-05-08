#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(msg):
    rospy.set_param("pose", str(msg.pose.pose.position.x) + '\t' + str(msg.pose.pose.position.y) + '\t' + str(msg.pose.pose.orientation.z))
    with open("/home/yujin/qa_file/pose_file" + filename, "a") as f:
        f.write('\t'.join([str(lst) for lst in range(1,15)]))

def pose():
    global filename
    odom_sub = rospy.Subscriber('/navi/pose', PoseWithCovarianceStamped, callback)
    filename = str(time.ctime().split(' ')[-2])
    if not os.path.exists("/home/yujin/qa_file/pose_file"):
        os.makedirs("/home/yujin/qa_file/pose_file")