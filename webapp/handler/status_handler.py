from tornado.escape import json_decode, json_encode
from webapp.handler.base_handler import BaseHandler
from webapp.util.logger import web_logger as LOGGER
import config as CONFIG


class StatusHandler(BaseHandler):
	def get(self):
		status = {
			'acState': self.settings['ac_servo'].get_current_state()
		}

		self.write(json_encode(status))
