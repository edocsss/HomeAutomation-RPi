from tornado.escape import json_encode
from webapp.handler.base_handler import BaseHandler


class TestHandler(BaseHandler):
	def get(self):
		self.write(json_encode({
			'result': True
		}))
