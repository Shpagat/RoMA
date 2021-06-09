
# подключение библиотеки для работы с контактами ввода/вывода
import RPi.GPIO as IO
import time                      # подключение библиотеки для работы с задержками
IO.setwarnings(False)            # отключаем показ любых предупреждений
# мы будем программировать контакты GPIO по их функциональным номерам (BCM), то есть мы будем обращаться к PIN35 как ‘GPIO19’
IO.setmode(IO.BCM)
import RPi.GPIO as GPIO
import time
GPIO_PWM_0 = 19
FREQUENCY = 100
DELAY_TIME = 0.02
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PWM_0, GPIO.OUT)
pwmOutput_0 = GPIO.PWM(GPIO_PWM_0, FREQUENCY)
pwmOutput_0.start(0)
try:
    while True:
        for dutyCycle in range(0, 101, 1):
            pwmOutput_0.ChangeDutyCycle(dutyCycle) 
            time.sleep(DELAY_TIME)
except KeyboardInterrupt:
    pwmOutput_0.stop()
    GPIO.cleanup()
    print('exiting')