import cozmo
from cozmo.util import distance_mm, speed_mmps, degrees

def reset(robot):
    robot.stop_all_motors()
    robot.set_head_angle(degrees(0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

def my_program(robot: cozmo.robot.Robot):
    try:
        robot.say_text("I can speak").wait_for_completed()
        for _ in range(4):
            robot.drive_straight(distance_mm(100), speed_mmps(100)).wait_for_completed()
            robot.turn_in_place(degrees(90)).wait_for_completed()

        head = robot.set_head_angle(degrees(30), in_parallel=True)
        lift = robot.set_lift_height(1.0, in_parallel=True)
        head.wait_for_completed()
        lift.wait_for_completed()
        robot.say_text("I did a square").wait_for_completed()
    finally:
        reset(robot)

cozmo.run_program(my_program)