import cozmo
import time

def my_program(robot: cozmo.robot.Robot):
    triggers = [
        ("Happy",    cozmo.anim.Triggers.MajorWin),
        ("Bored",    cozmo.anim.Triggers.Bored),
        ("Curious",  cozmo.anim.Triggers.CuriousB),
        ("Startled", cozmo.anim.Triggers.Startled),
        ("Thinking", cozmo.anim.Triggers.CodeLabThinking),
    ]
    for name, trig in triggers:
        print(f"Playing: {name}")
        robot.say_text(name, use_cozmo_voice=True, duration_scalar=0.6).wait_for_completed()
        robot.play_anim_trigger(trig).wait_for_completed()
        time.sleep(0.5)

cozmo.run_program(my_program)