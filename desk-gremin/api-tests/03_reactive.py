import cozmo
import time
from cozmo.util import degrees

def reset(robot):
    robot.stop_all_motors()
    robot.set_head_angle(degrees(0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()
    robot.set_all_backpack_lights(cozmo.lights.off_light)

def my_program(robot: cozmo.robot.Robot):
    try:
        robot.say_text("Try picking me up").wait_for_completed()

        # This handler fires automatically whenever state updates
        def watch(evt, **kw):
            if robot.is_picked_up:
                robot.set_all_backpack_lights(cozmo.lights.red_light)
            elif robot.is_cliff_detected:
                robot.set_all_backpack_lights(cozmo.lights.blue_light)
            else:
                robot.set_all_backpack_lights(cozmo.lights.green_light)

        robot.add_event_handler(cozmo.robot.EvtRobotStateUpdated, watch)

        # Just sit and let events fire for 30 seconds
        print("Pick him up (red), find an edge (blue), set down (green)")
        time.sleep(30)
        
    finally:
        reset(robot)

cozmo.run_program(my_program)