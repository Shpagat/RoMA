import RPi.GPIO as GPIO
from pi74HC595 import pi74HC595
import time


pwm_0 = 18  # пин для ШИМ
backward_pin0 = 4  # пин для обратного хода
frequency_pin0 = 2  # пин для получения информации о частоте

pwm_1 = 14  # пин для ШИМ
backward_pin1 = 15  # пин для обратного хода
frequency_pin1 = 18  # пин для получения информации о частоте

frequency = 10  # частота сигнала 10 Гц
duty_cycle = 50  # коэффициент заполнения 50%
delay = 0.2  # время паузы 0.2 сек

DS = 19
SH = 20
ST = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_0, GPIO.OUT)
GPIO.setup(pwm_1, GPIO.OUT)
GPIO.setwarnings(False)

GPIO.setup(backward_pin0, GPIO.OUT)
GPIO.setup(backward_pin1, GPIO.OUT)

pwmOutput_0 = GPIO.PWM(pwm_0, frequency)
pwmOutput_1 = GPIO.PWM(pwm_1, frequency)
shift_register = pi74HC595(DS=DS, SH=SH, ST=ST)


shift_register.clear()
time.sleep(5)


pwmOutput_0.start(duty_cycle) #включение ШИМ
pwmOutput_1.start(duty_cycle)
time.sleep(2)
GPIO.output (backward_pin0, 0) # 0 на белый провод
GPIO.output (backward_pin1, 0)#
pwmOutput_0.start(duty_cycle)
pwmOutput_1.start(duty_cycle*2)
print('forward')
time.sleep(2)
GPIO.output (backward_pin0, 1) # 1 на беры провод
GPIO.output (backward_pin1, 1)#
pwmOutput_0.start(duty_cycle)
pwmOutput_1.start(duty_cycle)
print('backward')
time.sleep(2)
pwmOutput_0.start(duty_cycle*0) # ШИМ со скважностью 0
pwmOutput_1.start(duty_cycle*0)
print('stop5')
time.sleep(2)
pwmOutput_0.stop(duty_cycle) #остановка генерации
pwmOutput_1.stop(duty_cycle)
time.sleep(2)
shift_register.set_by_list([1, 0, 0, 0, 0, 0, 1, 0])
print (shift_register.get_values())
time.sleep(1)
shift_register.set_by_list([0, 0, 0, 0, 0, 1, 0, 1])
print (shift_register.get_values())
time.sleep(1)
shift_register.set_by_list([1, 0, 0, 0, 1, 0, 0, 0])
print (shift_register.get_values())
time.sleep(1)
shift_register.set_by_list([0, 0, 0, 1, 0, 0, 0, 1])
print (shift_register.get_values())
time.sleep(1)
shift_register.set_by_list([1, 0, 1, 0, 0, 0, 0, 0])
print (shift_register.get_values())
time.sleep(1)
#shift_register.set_by_list([0, 1, 1, 0, 0, 1, 0, 1])
shift_register.clear()
pwmOutput_0.stop(duty_cycle)
pwmOutput_1.stop(duty_cycle)
time.sleep(2)
#pwmOutput_0.start(duty_cycle*0)
#pwmOutput_1.start(duty_cycle*0)    
    
