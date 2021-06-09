import RPi.GPIO as GPIO
import functions

led = 2
sphi_pin = 3
ir_pin = 4
motor = 17
counter = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor, GPIO.OUT)

# создание словаря
adress = {
    '100000001': 100000001,
    '100000010': 100000010,
    '100000100': 100000100,
    '100001000': 100001000,
    '100010000': 100010000
}

while KeyboardInterrupt():
    # запуск сканирования qr-кода
    key = (functions.qr_detector)
    if key in adress:
        print (adress[key])
        while counter <= 5:
            if functions.ir_sensor(ir_pin) == 1:  # ожидание датчика
                functions.shift(adress)  # открытие ячейки
                print (key)
                counter += 1
            else:
                print('Not found id')

    while functions.sphi_sensor(sphi_pin) == 0:   # закрытие ячеек
        GPIO.output(motor, 1)
    GPIO.output(motor, 0)

print('programm completed')
GPIO.cleanup()
