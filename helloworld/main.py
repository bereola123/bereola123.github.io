#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
import logging
import jinja2
import os

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = jinja_environment.get_template('hello.html')
        self.response.write(template.render())

class CountHandler(webapp2.RequestHandler):
	def get(self):
		for i in range(100):
			self.response.write(i)
			self.response.write('<br>')

class DaijonHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Daijon')

class FCHandler(webapp2.RequestHandler):
	def get(self):
		fortunes = [
		'something bad',
		'something good',
		'something mysterious',
		'IDK',
		]
		rand_fortune = random.choice(fortunes)
		self.response.write(rand_fortune)

class RandomHandler(webapp2.RequestHandler):
	def get(self):
		x = random.randint(0,100)
		y = random.randint(0,100)
		logging.info(x)
		logging.info(y)
		self.response.write(x+y)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/Daijon', DaijonHandler),
    ('/fortunecookie', FCHandler),
    ('/random', RandomHandler),
], debug=True)
