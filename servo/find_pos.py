#!/usr/bin/python3

import time
import wiringpi


def init():
	wiringpi.wiringPiSetupGpio()
	wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
	wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
	wiringpi.pwmSetClock(192)
	wiringpi.pwmSetRange(2000)
			


if __name__ == '__main__':
	init()
	pos = 1
	while pos != -1:
		pos = int(input('Enter position: '))
		wiringpi.pwmWrite(18, pos)
		time.sleep(0.5)
