import tornado.ioloop as ioloop
import tornado.web as web
import config as CONFIG
from webapp.handler.test_handler import TestHandler
from webapp.handler.ac_handler import AcHandler
from webapp.handler.status_handler import StatusHandler
from util.logger import web_logger as LOGGER

from servo.ac_servo import AcServo


if __name__ == '__main__':
	objects = {
		'ac_servo': AcServo(CONFIG.SERVO_PIN, CONFIG.SERVO_DELAY)
	}
	
	# Initial state
	objects['ac_servo'].off()

	# Tornado app setup
	app = web.Application([
		(r"/test", TestHandler),
		(r"/ac", AcHandler),
		(r"/status", StatusHandler)
	], debug=True, **objects)
	
	LOGGER.info('Starting server at port {}...'.format(CONFIG.SERVER_PORT))
	app.listen(CONFIG.SERVER_PORT, address='0.0.0.0')
	ioloop.IOLoop.current().start()
