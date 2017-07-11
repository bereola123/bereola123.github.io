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
import os
import jinja2

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class MadlibHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('madlib_input.html')
		self.response.write(template.render())

	def post(self):
		name = self.request.get('name')
		adjective = self.request.get('adj')
		noun = self.request.get('noun')
		verb = self.request.get('verb')
		number = self.request.get('number')

		number = int(number)

		template = jinja_environment.get_template('madlib_output.html')
		self.response.write(template.render({
			'name': name,
			'adjective': adjective,
			'noun': noun,
			'verb': verb,
			'number': number,
			}
			))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/madlib', MadlibHandler),
], debug=True)
