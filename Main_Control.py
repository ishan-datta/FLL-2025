from pybricks.hubs import PrimeHub
from pybricks.parameters import *
from pybricks.tools import *
import launch_1, launch_2, launch_3, launch_4, launch_5, launch_6, launch_7, launch_8

hub = PrimeHub()
hub.system.set_stop_button(None)
program_selected = 1
program_name = ''
programs = ['launch_1', 'launch_2', 'launch_3', 'launch_4', 'launch_5', 'launch_6', 'launch_7', 'launch_8',] # change this based on what your program files' names are

while True: 
    if Button.LEFT in hub.buttons.pressed() and program_selected > 1:
        program_selected -= 1
        while Button.LEFT in hub.buttons.pressed():
            wait(10)
    if Button.RIGHT in hub.buttons.pressed() and program_selected < len(programs):
        program_selected += 1
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)
    if Button.CENTER in hub.buttons.pressed():
        program_name = programs[program_selected-1] + '.program()'
        eval(program_name)
        if program_selected < len(programs):
            program_selected += 1
        while Button.CENTER in hub.buttons.pressed():
            wait(10)
        wait(200)

    hub.display.number(program_selected)
    wait(20)