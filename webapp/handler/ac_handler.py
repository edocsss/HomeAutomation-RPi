from tornado.escape import json_decode, json_encode
from webapp.handler.base_handler import BaseHandler
from servo.ac_servo import AcServo
import config as CONFIG
from webapp.util.logger import web_logger as LOGGER
from webapp.decorators.basic_auth import basic_auth


@basic_auth
class AcHandler(BaseHandler):
	def post(self):
		data = json_decode(self.request.body)
		if 'acState' in data:
			ac_state = data['acState']
			LOGGER.info('Next AC state: {}'.format(ac_state))
			
			ac_servo = self.settings['ac_servo']
			if ac_state:
				ac_servo.on()
			else:
				ac_servo.off()

			self.write(json_encode({
				'result': True
			}))
		else:
			self.write(json_encode({
				'result': False
			}))

	def get(self):
		self.write(json_encode({
			'acState': self.settings['ac_servo'].get_current_state()
		}))
