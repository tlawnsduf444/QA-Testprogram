#!/usr/bin/env python
# -*- coding:utf-8 -*-

def explain(name):
    if name == "Battery Percentage":
        return '배터리의 남은 용량을 보여줍니다.'
    
    elif name == "Battery Voltage":
        return '배터리의 전압을 보여줍니다.'

    elif name == "Battery Current":
        return '배터리의 전류값을 보여줍니다.'

    elif name == "Bumper":
        return '범퍼가 눌렸는지를 보여줍니다.'

    elif name == "Button":
        return '어떤 버튼이 눌렸는지를 보여줍니다.'

    elif name == "Cliff":
        return '절벽 센서의 값을 보여줍니다.'

    elif name == "Motor Current":
        return '모터의 전류값을 보여줍니다.'

    elif name == "Motor Voltage":
        return '모터의 전압값을 보여줍니다.'

    elif name == "Motor Temperature":
        return '모터의 온도값을 보여줍니다.'

    elif name == "Motor Board Temperatures":
        return '모터 보드의 온도값을 보여줍니다.'

    elif name == "Veloticy":
        return '로봇의 현재 속도값을 보여줍니다.'

    elif name == "Odometry":
        return '로봇의 주행 거리계값을 보여줍니다.'
    
    elif name == "Pose":
        return '로봇의 현재 위치값을 보여줍니다.'

    elif name == "Sonar":
        return '로봇의 초음파 센서의 값을 보여줍니다.'

    elif name == "Status":
        return '로봇이 현재 어떤 상태인지 보여줍니다.'

    elif name == "Wifi":
        return '로봇이 연결한 와이파이의 신호값을 보여줍니다.'