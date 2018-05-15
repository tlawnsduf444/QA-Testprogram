#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import os
import time
from datetime import datetime
from gopher_sentience_msgs.msg import Reality
from std_msgs.msg import Empty
battery_flag = True
flag = True
cnt = 0
new_time = 0
old_time = 0

def stop():
    sub.unregister()

def start(startb, stopb):
    global goal, stop, sub, filename, startbattery, stopbattery
    startbattery = startb
    stopbattery = stopb
    now = datetime.now()  
    filename = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '.txt'
    if not os.path.exists("/home/yujin/qa_file/delivery_file"):
        os.makedirs("/home/yujin/qa_file/delivery_file")

    goal = rospy.Publisher('/behaviours/custom_delivery_overseer/goal', Empty, queue_size=10)
    sub = rospy.Subscriber('/sentience/reality', Reality, callback)
    
def callback(msg):
    global battery_flag, cnt, flag, new_time, old_time
    charge = msg.charging
    battery = msg.battery_level
    status = msg.status
    if status == 0:
        if charge == True:
            if battery_flag == True:
                if battery >= startbattery:
                    goal.publish(Empty())
                    if flag == True:
                        cnt += 1
                        with open("/home/yujin/qa_file/delivery_file/" + filename, "a") as f:
                            new_time = time.ctime().split(' ')[-2]
                            f.write("%s\t%s\t%s\n"%(str(cnt),str(battery),str(new_time)))
                            old_time = new_time
                        flag = False
                else:
                    battery_flag = False
            else:
                if battery >= stopbattery:
                    battery_flag = True
    else:
        flag = True
        
