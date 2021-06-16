import RPi.GPIO as GPIO
import functions

led = 2
sphi_pin = 25
ir_pin = 2
motor = 17
counter = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)

def qr():
    led = 2
    sphi_pin = 25
    ir_pin = 2
    motor = 17
    counter = 1
    while KeyboardInterrupt():
        # создание словаря
        address = {
            '100000001': 100000001,
            '100000010': 100000010,
            '100000100': 100000100,
            '100001000': 100001000,
            '100010000': 100010000
        }
        while counter <= 5:
            key = str(functions.qr_detector())  # запуск сканирования qr-кода
            if key in address:
                print (key)
                if functions.ir_sensor(ir_pin) == 1:  # ожидание датчика
                    functions.shift(str(address[key]))  # открытие ячейки
                    print(key)
                    del address[key]  # удаление элемента из списка
                    print(str(key[0:]))
                    counter += 1
            else:
                print('Not found id')

        while functions.sphi_sensor(sphi_pin) == 0:   # закрытие ячеек
            GPIO.output(motor, 1)
        GPIO.output(motor, 0)
        GPIO.cleanup()

    print('programm completed')
    return 
