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

def is_palindrome(word):
		first_half = None
		second_half = None

		if len(word) % 2 == 0:
			first_half = len(word) / 2
			second_half = len(word) / 2
		else:
			first_half = (len(word) / 2) + 1
			second_half = len(word) / 2

		first_half = word[:first_half]
		second_half = word[second_half:]
		second_half = second_half[::-1]

		if first_half == second_half:
			return word + ' is a palindrome!'
		else:
			return word + ' is not a palindrome...'

class TemplateHandler(webapp2.RequestHandler):
	def get(self):
		palindrome_output = is_palindrome('kayak')
		template = jinja_environment.get_template('palindrome.html')
		self.response.write(template.render(
			{'palindrome': palindrome_output}))
	

class MainHandler(webapp2.RequestHandler):
	def get(self):
		palindrome_output = is_palindrome('kayak')
		self.response.write(palindrome_output)

class FortuneHandler(webapp2.RequestHandler):
		def get(self):
			fortunes = [
			'something good',
			'something bad',
			'something mysterious',
			]

			rand_fortune = random.choice(fortunes)

			template = (
				jinja_environment.get_template('fortune.html'))
			self.response.write(template.render(
				{
					'fortune': rand_fortune
				}))
class SumHandler(webapp2.RequestHandler):
	def get(self):
		first_number = random.randint(0, 100)
		second_number = random.randint(0, 100)
		template = jinja_environment.get_template('sum.html')
		self.response.write(template.render({
			'num1' : first_number,
			'num2' : second_number,
			'sum' : first_number + second_number
			}))
app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/template', TemplateHandler),
	('/fortune', FortuneHandler)
], debug=True)
