#!/usr/bin/env python3
# The INA219 source is from https://github.com/chrisb2/pi_ina219
# and helped me a lot! Thanks!

# ----------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------
from ina219 import INA219
import RPi.GPIO as GPIO
import time

# ----------------------------------------------------------------------
# Defines
# ----------------------------------------------------------------------
INTERVAL_SEC = 2
SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 1.0

GPIO_LED = 26
ALARM_THRESHOLD_VOTLS = 5.6

# ----------------------------------------------------------------------
# Globals
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# "Main" start...
# ----------------------------------------------------------------------
# setup GPIOs
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LED, GPIO.OUT, initial = GPIO.HIGH)

ina = INA219(SHUNT_OHMS, MAX_EXPECTED_AMPS)
ina.configure(ina.RANGE_16V, ina.GAIN_AUTO)

try:
    while True:
        # read voltage
        voltage = ina.voltage()
        print("Bus Voltage: %.3f V" % voltage)

        if(voltage > ALARM_THRESHOLD_VOTLS):
            GPIO.output(GPIO_LED, GPIO.HIGH)
        else:
            GPIO.output(GPIO_LED, not GPIO.input(GPIO_LED))

        time.sleep(INTERVAL_SEC)

except KeyboardInterrupt:
    GPIO.cleanup()


