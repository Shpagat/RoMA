from bluedot import BlueDot
from signal import pause
from gpiozero import Robot

# тут объявляешь функции, или в конце после баттанов можно попробовать


def forward():
    a = 10


def backward():
    a = 10


def left():
    a = 10


def right():
    a = 10
# и скорее всего нужно будет дggitобавить функцию стоп, когда отпускаешь кнопку bd[1, 0].when_released = robot.stop, также использовалось с robot


def stop():
    a = 10


# это тогда, как я понимаю нужно убрать, ибо robot испольховалось в bd[1, 0].when_pressed = robot.forward, в ты в шиме пропишешь подключение
robot = Robot(left=(4, 14), right=(17, 18))
bd = BlueDot(cols=3, rows=3)

bd.color = "red"
bd.square = True

bd[0, 0].visible = False
bd[2, 0].visible = False
bd[0, 2].visible = False
bd[2, 2].visible = False
bd[1, 1].visible = False

bd[1, 0].when_pressed = forward  # тут функция вызывается
bd[1, 2].when_pressed = backward
bd[0, 1].when_pressed = left
bd[2, 1].when_pressed = right

bd[1, 0].when_released = stop
bd[1, 2].when_released = stop
bd[0, 1].when_released = stop
bd[2, 1].when_released = stop

pause()
