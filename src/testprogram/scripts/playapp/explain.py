#!/usr/bin/env python
# -*- coding:utf-8 -*-

def explain(name):
    if name == "battery_percentage":
        return '배터리의 남은 용량을 보여줍니다.'
    
    elif name == "battery_voltage":
        return '배터리의 전압을 보여줍니다.'

    elif name == "battery_current":
        return '배터리의 전류값을 보여줍니다.'

    elif name == "bumper":
        return '범퍼가 눌렸는지를 보여줍니다.'

    elif name == "button":
        return '어떤 버튼이 눌렸는지를 보여줍니다.'

    elif name == "cliff":
        return '절벽 센서의 값을 보여줍니다.'

    elif name == "motor_current":
        return '모터의 전류값을 보여줍니다.'

    elif name == "motor_voltage":
        return '모터의 전압값을 보여줍니다.'

    elif name == "motor_temperature":
        return '모터의 온도값을 보여줍니다.'

    elif name == "motor_board_temperatures":
        return '모터 보드의 온도값을 보여줍니다.'

    elif name == "veloticy":
        return '로봇의 현재 속도값을 보여줍니다.'

    elif name == "odometry":
        return '로봇의 주행 거리계값을 보여줍니다.'
    
    elif name == "pose":
        return '로봇의 현재 위치값을 보여줍니다.'

    elif name == "sonar":
        return '로봇의 초음파 센서의 값을 보여줍니다.'

    elif name == "status":
        return '로봇이 현재 어떤 상태인지 보여줍니다.'

    elif name == "wifi":
        return '로봇이 연결한 와이파이의 신호값을 보여줍니다.'