#!/usr/bin/python3X
from servo.ac_servo import AcServo
import config as CONFIG


if __name__ == '__main__':
	servo = AcServo(CONFIG.SERVO_PIN, CONFIG.SERVO_DELAY)
	servo.off()

