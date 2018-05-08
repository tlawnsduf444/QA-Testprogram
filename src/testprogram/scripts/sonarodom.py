#!/usr/bin/env python
import rospy
import os
import datetime
from gopher_std_msgs.msg import Ranges
from nav_msgs.msg import Odometry
from gopher_sentience_msgs.msg import Reality
charging = False
velocity = '0'
angular = '0'
t = 0

def callback1(msg):
    global velocity, angular
    velocity = str(msg.twist.twist.linear.x)
    angular = str(msg.twist.twist.angular.z)

def callback2(msg):
    global charging
    if msg.charging == True:
        charging = True
    else:
        charging = False

def callback3(msg):
    global docking, undocking, t
    if t >= 0.2:
        with open("/home/yujin/qa_file/aging_file/" + filename + '.txt', "a") as f:
            f.write('\n')
            f.write('\t'.join([str(msg.ranges[i].range) for i in range(0,14)]))
            f.write('\t%s\t%s'%(velocity, angular))
            if charging == True:
                f.write('\t%s\t%s'%('charging', str(datetime.datetime.now())))
        t = 0
    else:
        t += 0.02

if __name__ == "__main__":
    global filename
    rospy.init_node('QA', anonymous=True)
    filename = str(datetime.datetime.now())
    if not os.path.exists("/home/yujin/qa_file/aging_file"):
        os.makedirs("/home/yujin/qa_file/aging_file")
    with open("/home/yujin/qa_file/aging_file/" + filename  + '.txt', "a") as f:
        f.write('\t'.join([str(lst) for lst in range(1,15)]))
        f.write('\t%s\t%s'%('linear', 'angular'))
        f.write('\t%s\t%s'%('status', 'time'))

    rospy.Subscriber('/core/odom', Odometry, callback1)
    rospy.Subscriber('/sentience/reality', Reality, callback2)
    rospy.Subscriber('/core/sonars', Ranges, callback3)
    rospy.spin()