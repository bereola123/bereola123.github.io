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
import urllib2
import json

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(
		os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

class SumHandler(webapp2.RequestHandler):
	def get(self):
		first_num = self.request.get('num1')
		second_num = self.request.get('num2')

		first_num = int(first_num)
		second_num = int(second_num)

		sum_o_nums = first_num + second_num

		template = jinja_environment.get_template(
			'sum.html')
		self.response.write(template.render(
			{
				'first_num': first_num,
				'second_num': second_num,
				'sum': sum_o_nums,
			}
			))

class EmailsHandler(webapp2.RequestHandler):
	def get(self):
		emails = [
			{'title': 'help', 'sender': 'fakeaccount@gmail.com'},
			{'title': 'money pls', 'sender': 'fakeaccount@gmail.com'},
			{'title': 'hey!', 'sender': 'a_friend@gmail.com'},
			{'title': 'spam', 'sender': 'fakeaccount@gmail.com'},
			{'title': 'day 11 hmwk', 'sender': 'drb@hampton.edu'},
		]

		template = jinja_environment.get_template(
			'emails.html')
		self.response.write(template.render(
			{
				'emails': emails
			}
			))

class MoviesHandler(webapp2.RequestHandler):
	def get(self):
		name = self.request.get('name')
		length = self.request.get('length')
		reviews = self.request.get('reviews')
		stars = self.request.get('stars')

		length = int(length)
		reviews = int(reviews)
		stars = int(stars)

		template = jinja_environment.get_template(
			'movies.html')
		self.response.write(template.render(
			{
				'title': name,
				'length': length,
				'reviews': reviews,
				'stars': stars,
			}
			))

class MadlibHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('madlib.html')
		self.response.write(template.render())

	def post(self):
		character_name = self.request.get('cName')
		adjective = self.request.get('adj')
		template = jinja_environment.get_template('madlib_out.html')
		self.response.write(template.render({
			'adjective': adjective,
			'character': character_name,
			}
			))

class ApiHandler(webapp2.RequestHandler):
	def get(self):
		response = urllib2.urlopen('https://randomuser.me/api?results=10')
		content = response.read()
		content_dictionary = json.loads(content)
		template = jinja_environment.get_template('user.html')
		self.response.out.write(template.render({
			'contents' : content_dictionary
			}
			))

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/email', EmailsHandler),
	('/sum', SumHandler),
	('/movies', MoviesHandler),
	('/madlib', MadlibHandler),
	('/a', ApiHandler),
], debug=True)
