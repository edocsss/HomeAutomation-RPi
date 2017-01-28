#!/usr/bin/python3

import time
import wiringpi
import config as CONFIG


class AcServo:
	AC_ON_POSITION = 150
	AC_ON_REST_POSITION = 151
	AC_OFF_POSITION = 165
	ON_REST_DELAY = 1

	def __init__(self, servo_pin, servo_delay):
		wiringpi.wiringPiSetupGpio()
		wiringpi.pinMode(servo_pin, wiringpi.GPIO.PWM_OUTPUT)
		wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
		wiringpi.pwmSetClock(CONFIG.PWM_CLOCK)
		wiringpi.pwmSetRange(CONFIG.PWM_RANGE)
		
		self.servo_pin = servo_pin
		self.servo_delay = servo_delay
		self.current_state = False
		
	def on(self):
		self._move(AcServo.AC_ON_POSITION)
		time.sleep(AcServo.ON_REST_DELAY)
		self._move(AcServo.AC_ON_REST_POSITION)
		self.current_state = True

	def off(self):
		self._move(AcServo.AC_OFF_POSITION)
		self.current_state = False

	def get_current_state(self):
		return self.current_state

	def _move(self, servo_position):
		wiringpi.pwmWrite(self.servo_pin, servo_position)
		time.sleep(self.servo_delay)
