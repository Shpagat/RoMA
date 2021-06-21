from pi74HC595 import pi74HC595
import RPi.GPIO as GPIO
import time
import cv2  # импорт модуля  из библиотеки Opencv


def sphi_sensor(sphi_pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sphi_pin, GPIO.IN)

    try:
        while True:
            # световой поток активен
            if GPIO.input(sphi_pin) == 1:
                sphi = 0
            else:
                # световой поток прерван
                sphi = 1
                return(sphi)
                # break
            return(sphi)
            # time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()


def ir_sensor(ir_pin):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ir_pin, GPIO.IN)

    try:
        while True:
            # если препятствие обнаружено
            if GPIO.input(ir_pin) == 0:
                ir = 1
                return(ir)
            # если препятствие не обнаружено
            elif GPIO.input(ir_pin) == 1:
                ir = 0
            return(ir)
    except KeyboardInterrupt:
        GPIO.cleanup()


def ultrasonic_sensor():
    GPIO.setmode(GPIO.BCM)

    echo = 23
    trig = 24

    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)

    try:
        while True:
            GPIO.output(trig, 0)
            time.sleep(2)

            GPIO.output(trig, 1)
            time.sleep(0.00001)
            GPIO.output(trig, 0)

            while GPIO.input(echo) == 0:
                pulse_start = time.time()

            while GPIO.input(echo) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)

            if distance > 40:
                print("Distance:", distance, "cm")
            elif distance <= 40:
                print("Warning!")
    except KeyboardInterrupt:
        GPIO.cleanup()


def shift(address):
    GPIO.setmode(GPIO.BCM)
    shift_register = pi74HC595()
    shift_register.set_by_list([address[0:]])
    time.sleep(1)
    shift_register.clear()


def qr_detector():  # функция расшифровки qr-кода

    # создание словаря
    key_to_multiplier = {
        '376d737b2b2341b79cc4100fe1a32202': 100000001,
        '93017d1beaa441149b6551d8b8759f0b': 100000010,
        'ae6248d62ca44bd3aa88430e64535a4d': 100000100,
        '06486108a588442587d746dc3515e4b6': 100001000,
        '9194c8e8673a4c32a0b4699d8718d5d3': 100010000
    }

    cap = cv2.VideoCapture(0)  # настройка и включение камеры

    # создание объекта детектора. В Opencv имеется  встроенный метод детектор QR
    detector = cv2.QRCodeDetector()

    # нахождение и декодирование нашего кода
    while True:

        _, img = cap.read()  # получить изображение

        # извлечь местоположение штрих-кода и зашифрованную информацию
        data, _, _ = detector.detectAndDecode(img)
        key = data

        # возвращаем расшифрованное значение
        if key in key_to_multiplier:

            # закрываем видеопоток, освобождаем память
            cap.release()
            cv2.destroyAllWindows()

            return key_to_multiplier[key]
