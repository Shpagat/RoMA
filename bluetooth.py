import RPi.GPIO as GPIO
import time
import main
from bluedot import BlueDot
from signal import pause
#from gpiozero import Robot

pwm_0 = 17  #
pwm_1 = 10  #
backward_pin0 = 27 
backward_pin1 = 9
frequency = 10  #частота сигнала 10 Гц
duty_cycle = 50  # коэффициент заполнения 50%
delay = 0.2 # время паузы 0.2 сек

GPIO.setmode(GPIO.BCM)
GPIO.setup (pwm_0, GPIO.OUT)
GPIO.setup (pwm_1, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup (backward_pin0, GPIO.OUT)
GPIO.setup (backward_pin1, GPIO.OUT)
pwmOutput_0 = GPIO.PWM (pwm_0, frequency)
pwmOutput_1 = GPIO.PWM (pwm_1, frequency)

 
def forward():
    
    pwmOutput_0.start(duty_cycle)
    pwmOutput_1.start(duty_cycle)
    time.sleep (delay)
    pwmOutput_0.stop(duty_cycle)
    pwmOutput_1.stop(duty_cycle)
    print("button forward pressed")
    #GPIO.cleanup() 
    return

def backward():
    
    GPIO.output (backward_pin0, 1)
    GPIO.output (backward_pin1, 1)     
    pwmOutput_0.start(duty_cycle)
    pwmOutput_1.start(duty_cycle)
    time.sleep (delay)
    pwmOutput_0.stop(duty_cycle)
    pwmOutput_1.stop(duty_cycle)
    print("button backward pressed")
    #GPIO.cleanup() 
    return

def left():
    
    pwmOutput_0.start(duty_cycle/2)
    pwmOutput_1.start(duty_cycle/2)
    time.sleep (delay)
    pwmOutput_0.stop(duty_cycle)
    pwmOutput_1.stop(duty_cycle)
    print("button left pressed")
    #GPIO.cleanup()
    return
    
def right():
    
    pwmOutput_0.start(duty_cycle/2)
    pwmOutput_1.start(duty_cycle/2)
    time.sleep (delay)
    pwmOutput_0.stop(duty_cycle)
    pwmOutput_1.stop(duty_cycle)
    print("button right pressed")
    #GPIO.cleanup()
    return
# и скорее всего нужно будет дggitобавить функцию стоп, когда отпускаешь кнопку bd[1, 0].when_released = robot.stop, также использовалось с robot


def stop():
    pwmOutput_0.start(duty_cycle*0)
    pwmOutput_1.start(duty_cycle*0)
    pwmOutput_0.stop(duty_cycle)
    pwmOutput_1.stop(duty_cycle)


# это тогда, как я понимаю нужно убрать, ибо robot испольховалось в bd[1, 0].when_pressed = robot.forward, в ты в шиме пропишешь подключение
#robot = Robot(left=(4, 14), right=(17, 18))
bd = BlueDot(cols=3, rows=3)

bd.color = "red"
bd.square = True

bd[0, 0].visible = False
bd[2, 0].visible = False
bd[0, 2].visible = False
bd[2, 2].visible = False
#bd[1, 1].visible = False

bd[1, 0].when_pressed = forward # тут функция вызывается
bd[1, 2].when_pressed = backward
bd[0, 1].when_pressed = left
bd[2, 1].when_pressed = right
bd[1, 1].when_pressed = main.qr()

bd[1, 0].when_released = stop
bd[1, 2].when_released = stop
bd[0, 1].when_released = stop
bd[2, 1].when_released = stop

pause()
