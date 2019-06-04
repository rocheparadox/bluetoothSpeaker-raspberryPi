#import required packages
import subprocess
import RPi.GPIO as gpio
import time
import os
import logging


pair_pin=11
#fetch the file directory from which the python script is run
fileDirectory = os.path.dirname(os.path.realpath(__file__))

#Set the log file location as same as the python script location
logFile=fileDirectory+"/bluetoothSpeaker.log"
logging.basicConfig(filename=logFile, filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def pairNewDevice(channel):
    #ISR for pin 11
    print("Waiting to pair")
    logging.info("Waiting to pair")
    output = subprocess.call(["/bin/bash",fileDirectory+"/pair_and_trust_bluetooth_device.sh", ">>", fileDirectory+"/bluetoothSpeaker.log"])

gpio.setmode(gpio.BOARD)
gpio.setup(pair_pin, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
    #Set the pair_pin as an interrupt pin that detects the falling edge and when it does, call the pairNewDevice function
    gpio.add_event_detect(pair_pin, gpio.FALLING, callback=pairNewDevice, bouncetime=1000)

    print("Bluetooth program has started")
    logging.info("Bluetooth program has started")
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    gpio.cleanup()



