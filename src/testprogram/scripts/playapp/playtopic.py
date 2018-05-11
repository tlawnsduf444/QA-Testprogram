from monitor import *

def playtopic(checklist):
    init()
    if checklist["battery_percentage"] == True or checklist["battery_voltage"] == True or checklist["battery_current"] == True:
        battery.battery()
        
    if checklist["bumper"] == True:
        bumper.bumper()

    if checklist["button"] == True:
        button.button()

    if checklist["cliff"] == True:
        cliff.cliff()

    if checklist["motor_current"] == True or checklist["motor_voltage"] == True or checklist["motor_temperature"] == True or checklist["motor_board_temperatures"] == True:
        motor.motor()
            
    if checklist["velocity"] == True:
        velocity.velocity()

    if checklist["odometry"] == True:
        odom.odom()

    if checklist["pose"] == True:
        pose.pose()

    if checklist["sonar"] == True:
        sonar.sonar()

    if checklist["status"] == True or checklist["wifi"] == True:
        status.status()

def init():
    try:
        battery.stop()
    except:
        pass
    try:
        bumper.stop()
    except:
        pass
    try:
        button.stop()
    except:
        pass
    try:
        cliff.stop()
    except:
        pass
    try:
        motor.stop()
    except:
        pass
    try:
        velocity.stop()
    except:
        pass
    try:
        odom.stop()
    except:
        pass
    try:
        pose.stop()
    except:
        pass
    try:
        sonar.stop()
    except:
        pass
    try:
        status.stop()
    except:
        pass