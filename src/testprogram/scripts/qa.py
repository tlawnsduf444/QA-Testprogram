#!/usr/bin/env python
# -*- coding:utf-8 -*-
import rospy
from appJar import gui
from monitor import *
from playapp import *

class app:
    version = "v1.0"
    testlist = sorted(["Battery_Percentage", "Battery_Voltage", "Battery_Current", "Bumper", "Button", "Cliff", "Motor_Current", "Motor_Voltage", 
    "Motor_Temperature","Motor_Board_Temperatures", "Velocity", "Odometry", "Pose", "Sonar", "Status", "Wifi"]) # 테스트가 추가될 경우 이부분을 수정해주세요.

    def __init__(self):
        rospy.init_node('QA', anonymous=True)
        self.app = gui("QA Test Program " + self.version, "800x600")
        self.app.startTabbedFrame("TabbedFrame")
        self.app.startTab("Test")
        #테스트 리스트#
        with self.app.panedFrame("p1"):
            self.app.label("testtitle", "Choose Your Test!!")
            for i in range(len(self.testlist)):
                self.app.checkBox(self.testlist[i])
                self.app.setCheckBoxOverFunction(self.testlist[i], self.showexplain)
            self.app.button("Show", self.playapp)

            #설명하는 곳#
            with self.app.panedFrame("p2", sticky = "ew", stretch = "column"):
                with self.app.labelFrame("Explain"):
                    self.app.label("explain", "체크리스트에 마우스를 가져가면 그에 대한 설명이 보입니다.")
                with self.app.labelFrame("Information", sticky = "news", stretch = "both"):
                    for i in range(len(self.testlist)):
                        self.app.label(self.testlist[i], "")
        
        self.app.stopTab()
        self.app.stopTabbedFrame()
        
        self.app.setPollTime(10)
        self.app.go()

    def playapp(self):
        self.checklist = self.app.getAllCheckBoxes()
        playtopic.playtopic(self.checklist)
        self.app.registerEvent(self.showinfo)
        
    def showexplain(self, name):
        self.app.label("explain", explain.explain(name))

    def showinfo(self):
        for i in range(len(self.checklist)): 
            if self.checklist[self.testlist[i]] == True:
                name = self.testlist[i].lower()
                self.app.label(self.testlist[i], rospy.get_param(name))

if __name__ == "__main__":
    qatest = app()