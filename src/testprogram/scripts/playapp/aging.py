#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import os
from datetime import datetime
from gopher_sentience_msgs.msg import Reality
from std_msgs.msg import Empty
battery_flag = True
flag = True
write_flag = False
cnt = 0
starttime = None
stoptime = None

def stop():
    sub.unregister()

def start(startb, stopb):
    global goal, stop, sub, filename, startbattery, stopbattery
    startbattery = startb
    stopbattery = stopb
    now = datetime.now()  
    filename = now.strftime('%Y%m%d%H%M%S') + '.txt'
    if not os.path.exists("/home/yujin/qa_file/delivery_file"):
        os.makedirs("/home/yujin/qa_file/delivery_file")

    goal = rospy.Publisher('/behaviours/custom_delivery_overseer/goal', Empty, queue_size=10)
    sub = rospy.Subscriber('/sentience/reality', Reality, callback)
    
def callback(msg):
    global battery_flag, cnt, flag, write_flag, starttime, stoptime
    charge = msg.charging
    battery = msg.battery_level
    status = msg.status
    if status == 0:
        if charge == True:
            if write_flag == True:
                stoptime = datetime.now()
                with open("/home/yujin/qa_file/delivery_file/" + filename, "a") as f:
                    f.write('\t' + stoptime.strftime('%H시 %M분 %S초') + '\t' + str(stoptime - starttime) + '\n')
                write_flag = False
            if battery_flag == True:
                if battery >= startbattery:
                    goal.publish(Empty())
                    if flag == True:    
                        cnt += 1
                        starttime = datetime.now()
                        with open("/home/yujin/qa_file/delivery_file/" + filename, "a") as f:
                            f.write(str(cnt) + '\t' + str(battery) + '\t' + starttime.strftime('%H시 %M분 %S초'))
                        flag = False
                        rospy.set_param("RobotStatus", str(cnt) + '\t' + "Traveling")
                else:
                    battery_flag = False
            else:
                rospy.set_param("RobotStatus", str(cnt) + '\t' + "Charging")
                if battery >= stopbattery:
                    battery_flag = True
    else:
        write_flag = True
        flag = True