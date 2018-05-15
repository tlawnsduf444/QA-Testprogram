#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
import os
from appJar import gui
from monitor import *
from playapp import *
import time
from datetime import datetime

class app:
    version = "v1.0"
    show_flag = True
    aging_flag = True
    write_flag = False
    debug_flag = False
    loop_flag = False
    testlist = sorted(["battery_percentage", "battery_voltage", "battery_current", "bumper", "button", "cliff", "motor_current", "motor_voltage", 
    "motor_temperature","motor_board_temperatures", "velocity", "odometry", "pose", "sonar", "status", "wifi"]) # 테스트가 추가될 경우 이부분을 수정해주세요.

    def __init__(self):
        rospy.init_node('QA', anonymous=True)
        self.app = gui("QA Test Program " + self.version, "1000x800")
        self.app.startTabbedFrame("TabbedFrame")
        self.app.startTab("Test")
        #테스트 리스트#
        with self.app.panedFrameVertical("TOP"):
            self.app.setInPadding([10,5])
            self.app.button("Show", self.playapp, 0, 0, sticky="ew")
            self.app.button("Delivery", self.playapp, 0, 1)
            self.app.button("No-Write", self.yesorno, 0, 2)
            self.app.button("No-Debug", self.yesorno, 0, 3)
            self.app.addEntry("hz",0, 4)
            self.app.addEntry("start",0, 5)
            self.app.addEntry("stop",0, 6)
            self.app.setEntryDefault("hz", "몇초에 한 번 저장할까요?")
            self.app.setEntryDefault("start", "몇%에서 출발할까요?")
            self.app.setEntryDefault("stop", "몇%에서 충전할까요?")
            with self.app.panedFrame("LEFT"):
                for i in range(len(self.testlist)):
                    self.app.checkBox(self.testlist[i])
                    self.app.setCheckBoxOverFunction(self.testlist[i], self.showexplain)
            #설명하는 곳#
                with self.app.panedFrame("RIGHT"):
                    with self.app.labelFrame("Explain"):
                        self.app.label("explain", "체크리스트에 마우스를 가져가면 그에 대한 설명이 보입니다.", sticky = "ew")
                    with self.app.labelFrame("Information", sticky = "ew"):
                        for i in range(len(self.testlist)):
                            self.app.label(self.testlist[i], "")
        
        self.app.stopTab()
        self.app.stopTabbedFrame()
        
        self.app.go()

    def playapp(self, button):
        if button == "Show":
            now = datetime.now()  
            self.filename = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '.txt'
            for i in range(len(self.testlist)):
                self.app.clearLabel(self.testlist[i])
            self.checklist = self.app.getAllCheckBoxes()
            playtopic.playtopic(self.checklist)
            if self.loop_flag == False:
                if self.app.getEntry("hz") != "":
                    self.app.setPollTime(int(float(self.app.getEntry("hz"))*1000))
                    self.app.registerEvent(self.showinfo)
                    self.app.disableEntry("hz") 
                    self.loop_flag = True
                else:
                    self.app.label("explain", "주기를 입력해주세요 ㅠㅠ")
        else:
            if self.aging_flag == True:
                if self.app.getEntry("start") != "" and self.app.getEntry("stop") != "":
                    aging.start(int(self.app.getEntry("start")), int(self.app.getEntry("stop")))
                    self.app.setButton("Delivery", "Stop-Delivery")
                    self.aging_flag = False
                else:
                    self.app.label("explain", "배터리를 입력해주세요 ㅠㅠ")
            else:
                aging.stop()
                self.app.setButton("Delivery", "Delivery")
                self.aging_flag = True

    def yesorno(self, button):
        if button == "No-Write":
            if self.write_flag == False:
                self.app.setButton("No-Write", "Write")
                self.write_flag = True
            else:
                self.app.setButton("No-Write", "No-Write")
                self.write_flag = False
        else:
            if self.debug_flag == False:
                self.app.setButton("No-Debug", "Debug")
                self.debug_flag = True
                os.system("rosrun dynamic_reconfigure dynparam set /core/somanet debug_mode true")
            else:
                self.app.setButton("No-Debug", "No-Debug")
                self.debug_flag = False
                os.system("rosrun dynamic_reconfigure dynparam set /core/somanet debug_mode false")

    def showexplain(self, name):
        self.app.label("explain", explain.explain(name))

    def showinfo(self):
        for i in range(len(self.checklist)):
            if self.checklist[self.testlist[i]] == True:
                self.app.label(self.testlist[i], rospy.get_param(self.testlist[i]))
                if self.write_flag == True:
                    if not os.path.exists("/home/yujin/qa_file/" + self.testlist[i] +"_file/"):
                        os.makedirs("/home/yujin/qa_file/" + self.testlist[i] +"_file/")
                    with open("/home/yujin/qa_file/" + self.testlist[i] +"_file/" + self.filename, "a") as f:
                        f.write(str(time.ctime().split(' ')[-2]) + '\t' + rospy.get_param(self.testlist[i]) + '\n')

if __name__ == "__main__":
    qatest = app()