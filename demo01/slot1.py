# MicroPython for LEGO Hardware (LEGO Education's SPIKE Prime)
from spike import PrimeHub, Motor
from spike.control import wait_for_seconds

# motor connected to A:
my_motor = Motor('A')
my_motor.start(-50) # backward
wait_for_seconds(2)
my_motor.stop()