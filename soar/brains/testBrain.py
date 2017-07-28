from soar.gui.plot_window import PlotWindow
from soar.controller import sim_completed
from soar.robot.pioneer import PioneerRobot

from math import pi, inf

robot = PioneerRobot()


#  This function is called when the brain is loaded
def on_load():
    print('Brain on_load() called.')


#  This function is called when the start button is pushed
def on_start():
    print('Brain on_start() called.')
    robot.readings = []
    #robot.FV_CAP = inf


#  This function is called every step_duration seconds. By default, it is called 10 times/second
def on_step(step_duration):
    print(robot.pos[2])
    robot.rv = -2*pi



# This function is called when the stop button is pushed
def on_stop():
    print('Brain on_stop() called.')


# This function is called when the robot's controller is shut down
def on_shutdown():
    print('Brain on_shutdown() called.')