import gsheetUpdater as gsheet
import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO

# read data using pin 14

def run_sensor(pin_num)
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    nstance = dht11.DHT11(pin=pin_num)

    try:
        while True:
            result = instance_0.read()
            if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))
                print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)
                gsheet.update_record(pin_num, str(datetime.datetime.now()),result.temperature, result.humidity)
                time.sleep(60)
            else:
                print(result.error_code)
                time.sleep(10)
            
    except KeyboardInterrupt:
        print("Cleanup")
        GPIO.cleanup()