from monitor import *

def playtopic(checklist):
    if checklist["Battery_Percentage"] == True or checklist["Battery_Voltage"] == True or checklist["Battery_Current"] == True:
        battery.battery()

    if checklist["Bumper"] == True:
        bumper.bumper()

    if checklist["Button"] == True:
        button.button()

    if checklist["Cliff"] == True:
        cliff.cliff()

    if checklist["Motor_Current"] == True or checklist["Motor_Voltage"] == True or checklist["Motor_Temperature"] == True or checklist["Motor_Board_Temperatures"] == True:
        motor.motor()

    if checklist["Velocity"] == True:
        velocity.velocity()

    if checklist["Odometry"] == True:
        odom.odom()
    
    if checklist["Pose"] == True:
        pose.pose()

    if checklist["Sonar"] == True:
        sonar.sonar()

    if checklist["Status"] == True or checklist["Wifi"] == True:
        status.status()