#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import os
import datetime
from gopher_sentience_msgs.msg import Reality
from std_msgs.msg import Empty
battery_flag = 1
cnt = 0

def stop():
    try:
        sub.unregister()
    except:
        print("먼저 로봇을 출발시켜주세요.")

def start():
    global goal, stop, sub, filename
    filename = str(datetime.datetime.now())
    if not os.path.exists("/home/yujin/qa_file/delivery_file"):
        os.makedirs("/home/yujin/qa_file/delivery_file")
    with open("/home/yujin/qa_file/delivery_file/" + filename, "w") as f:
        f.write("%s\t%s\t%s\n"%("Count","Percentage","Time"))

    goal = rospy.Publisher('/behaviours/custom_delivery_overseer/goal', Empty, queue_size=10)
    sub = rospy.Subscriber('/sentience/reality', Reality, callback)
    
def callback(msg):
    global battery_flag, cnt
    charge = msg.charging
    battery = msg.battery_level
    if charge == True: 
        if battery_flag == 1:
            if battery >= 35:
                goal.publish(Empty())
                cnt += 1
                with open("/home/yujin/qa_file/delivery_file/" + filename, "a") as f:
                    f.write("%s\t%s\t%s\n"%(str(cnt),str(battery),str(datetime.datetime.now())))
            else:
                battery_flag = 0
        else:
            if battery >= 50:
                battery_flag = 1
        
