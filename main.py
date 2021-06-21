import RPi.GPIO as GPIO
import functions

led_1 = 0b10000000
led_2 = 0b00000001
sphi_pin = 16
ir_pin = 27
motor = 0b01000000
counter = 1

GPIO.setmode(GPIO.BCM)



counter = 1
while KeyboardInterrupt():
    # создание словаря
    address = {
        '100000001': 100100000,
        '100000010': 100010000,
        '100000100': 100001000,
        '100001000': 100000100,
        '100010000': 100000010
    }
    while counter <= 5:
        
        key = str(functions.qr_detector())  # запуск сканирования qr-кода
        print (key)
        if key in address:
            print (key)

            if functions.ir_sensor(ir_pin) == 1:  # ожидание датчика
                address = (str(address[key])[1:])
                address = list(address)
                print (address)
                functions.shift(address)  # открытие ячейки
                print(key)
                del address[key]  # удаление элемента из списка
                print(str(key[0:]))
                counter += 1
        else:
            print('Not found id')
    while functions.sphi_sensor(sphi_pin) == 0:   # закрытие ячеек
        functions.motor(motor)
GPIO.cleanup()
print('programm completed')

