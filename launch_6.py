from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import *
from pybricks.robotics import DriveBase
from pybricks.tools import *
from umath import *
from urandom import *

async def quit_program():
    watch = StopWatch()
    await wait(1000)
    watch.resume()
    while True:
        if Button.CENTER in hub.buttons.pressed():
            watch.reset()
            while Button.CENTER in hub.buttons.pressed():
                if watch.time() >= 500:
                    watch.pause()
                    watch.reset()
                    hub.display.icon([[100, 0, 0, 0, 100], [0, 100, 0, 100, 0], [0, 0, 100, 0, 0], [0, 100, 0, 100, 0], [100, 0, 0, 0, 100]])
                    await wait(100)
                    return
        while not Button.CENTER in hub.buttons.pressed():
            await wait(10)

async def launch():
    await multitask(mission(), quit_program(), race=True)

def program():
    # initialize hub, motors, and driving base
    global hub, move_motor_1, move_motor_2, arm_motor_1, arm_motor_2, drive_base
    arm_motor_1 = Motor(Port.C, reset_angle=True, profile=5)
    move_motor_2 = Motor(Port.B, reset_angle=True, profile=5, positive_direction=Direction.CLOCKWISE)
    move_motor_1 = Motor(Port.A, reset_angle=True, profile=5, positive_direction=Direction.COUNTERCLOCKWISE)
    arm_motor_2 = Motor(Port.D, reset_angle=True, profile=5)
    hub = PrimeHub()
    hub.light.off()
    hub.display.off()
    hub.system.set_stop_button(None)
    drive_base = DriveBase(move_motor_1, move_motor_2, 62.4, 110)
    drive_base.use_gyro(True)

    # run mission
    run_task(launch())

    # close motors so that they can be used again
    move_motor_1.close()
    move_motor_2.close()
    arm_motor_1.close()
    arm_motor_2.close()

async def mission():
    # mission code goes here
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=400)
    await drive_base.straight(-10)
    await drive_base.straight(490)
    drive_base.settings(straight_speed=200)
    await drive_base.arc(1250, angle=12)
    drive_base.settings(straight_speed=400)
    await drive_base.arc(1250, angle=-25)