import RPi.GPIO as GPIO
import time
import cv2  # импорт модуля  из библиотеки Opencv


def sphi_sensor():
    sphi_pin = 23

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
                print(sphi)
                break
            print(sphi)
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()


def ir_sensor():
    ir_pin = 23

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ir_pin, GPIO.IN)

    try:
        while True:
            # если препятствие обнаружено
            if GPIO.input(ir_pin) == 0:
                ir = 1
                print(ir)
                break
            # если препятствие не обнаружено
            elif GPIO.input(ir_pin) == 1:
                ir = 0
            print(ir)
            time.sleep(1)
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


def qr_detector():

    # настройка и включение камеры
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # создание объекта детектора. В Opencv имеется  встроенный метод детектор QR
    detector = cv2.QRCodeDetector()

    # нахождение и декодирование нашего кода
    while True:
        for dutyCycle in range(0, 101, 1):
            pwmOutput_0.ChangeDutyCycle(dutyCycle)
            time.sleep(DELAY_TIME)
    except KeyboardInterrupt:
    pwmOutput_0.stop()
    GPIO.cleanup()
    print('exiting')
