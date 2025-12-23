from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import *
from pybricks.robotics import DriveBase
from pybricks.tools import *
from micropython import const
from umath import *
from urandom import *

async def mission():
    # mission code goes here
    await drive_base.straight(690)
    await drive_base.arc(155,90)
    drive_base.settings(straight_speed=50)
    await drive_base.straight(100)
    await multitask(arm_motor_2.run_angle(500, -50), drive_base.straight(-100))
    await drive_base.arc(155,-90)
    drive_base.settings(straight_speed=500)
    await arm_motor_2.run_angle(500, -70)
    await drive_base.straight(-700)

def program():
    # initialize hub, motors, and driving base
    global hub, move_motor_1, move_motor_2, arm_motor_1, arm_motor_2, drive_base
    hub = PrimeHub()
    move_motor_1 = Motor(Port.A, reset_angle=True, profile=5, positive_direction=Direction.COUNTERCLOCKWISE)
    move_motor_2 = Motor(Port.B, reset_angle=True, profile=5, positive_direction=Direction.CLOCKWISE)
    arm_motor_1 = Motor(Port.C, reset_angle=True, profile=5)
    arm_motor_2 = Motor(Port.D, reset_angle=True, profile=5)
    hub.light.off()
    hub.display.off()
    hub.system.set_stop_button(None)
    drive_base = DriveBase(move_motor_1, move_motor_2, 62.4, 110)
    drive_base.use_gyro(True)

    # run mission
    run_task(mission())

    # close motors so that they can be used again
    move_motor_1.close()
    move_motor_2.close()
    arm_motor_1.close()
    arm_motor_2.close()

program()