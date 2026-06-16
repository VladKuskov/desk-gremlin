import cozmo
from cozmo.util import degrees

def reset(robot):
    robot.stop_all_motors()
    robot.set_head_angle(degrees(0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

def my_program(robot: cozmo.robot.Robot):
    try:
        # wait_for_completed = python halts/waits here
        # sequential movements
        robot.set_head_angle(degrees(30)).wait_for_completed()
        robot.set_lift_height(1.0).wait_for_completed()
        robot.say_text("sequential").wait_for_completed()

        reset(robot)

        # parallel movements
        head = robot.set_head_angle(degrees(30), in_parallel=True)
        lift = robot.set_lift_height(1.0, in_parallel=True)
        speech = robot.say_text("parallelism!", in_parallel=True)
        head.wait_for_completed()
        lift.wait_for_completed()
        speech.wait_for_completed()
    finally:
        reset(robot)

cozmo.run_program(my_program)