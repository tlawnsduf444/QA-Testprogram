#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import os
from gopher_sentience_msgs.msg import Reality
from std_msgs.msg import Empty
battery_flag = True
flag = True
cnt = 0

def stop():
    sub.unregister()

def start():
    global goal, stop, sub, filename
    filename = str(time.ctime().split(' ')[-4]) + '\t' + str(time.ctime().split(' ')[-3]) + str(time.ctime().split(' ')[-2])
    if not os.path.exists("/home/yujin/qa_file/delivery_file"):
        os.makedirs("/home/yujin/qa_file/delivery_file")

    goal = rospy.Publisher('/behaviours/custom_delivery_overseer/goal', Empty, queue_size=10)
    sub = rospy.Subscriber('/sentience/reality', Reality, callback)
    
def callback(msg):
    global battery_flag, cnt, flag
    charge = msg.charging
    battery = msg.battery_level
    status = msg.status
    if status == 0:
        if charge == True:
            if battery_flag == True:
                if battery >= 35:
                    if flag == True:
                        goal.publish(Empty())
                        cnt += 1
                        with open("/home/yujin/qa_file/delivery_file/" + filename, "a") as f:
                            f.write("%s\t%s\t%s\n"%(str(cnt),str(battery),str(time.ctime().split(' ')[-2])))
                        flag = False
                else:
                    battery_flag = False
            else:
                if battery >= 70:
                    battery_flag = True
    else:
        flag = True
        
