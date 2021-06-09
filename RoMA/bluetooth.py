from bluedot import BlueDot
from signal import pause
from gpiozero import Robot

robot = Robot(left=(4, 14), right=(17, 18))
bd = BlueDot(cols=3, rows=3)

bd.color = "red"
bd.square = True

bd[0, 0].visible = False
bd[2, 0].visible = False
bd[0, 2].visible = False
bd[2, 2].visible = False
bd[1, 1].visible = False

bd[1, 0].when_pressed = robot.forward
bd[1, 2].when_pressed = robot.backward
bd[0, 1].when_pressed = robot.left
bd[2, 1].when_pressed = robot.right

bd[1, 0].when_released = robot.stop
bd[1, 2].when_released = robot.stop
bd[0, 1].when_released = robot.stop
bd[2, 1].when_released = robot.stop

pause()