from tornado.escape import json_encode
import tornado.ioloop
import tornado.web
import statements
import collections
from main_handle import MainHandle
import urlparse
import json
from tornado.escape import json_decode
from datetime import datetime
import MySQLdb
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

class ForbidAccessHandle(MainHandle):
	def post(self):
		print"Forbid access app..."
		body = tornado.escape.json_decode(self.request.body)
		res = {}
		dicts = []
		value_ip = []
		value_ip.append(body['email'])
		value_ip.append(body['imei'])
		value_ip.append(body["package"])
		self.cursor.execute(statements.CM_CHECK_ACCESS_APP, value_ip)
		self.db.commit()
		row = self.cursor.fetchone()
		if row == 0:
			res['error_code'] = 0
			res['value'] = 1
		else:
			res['error_code'] = 0
			res['value'] = 0
		self.write(json_encode(res))

class AddAppToForbidMode(MainHandle):
	def post(self):
		print"Add app to forbid mode..."
		body = tornado.escape.json_decode(self.request.body)
		res = {}
		dicts = []
		value_ip = []
		value_ip.append(body['email'])
		value_ip.append(body['imei'])
		value_ip.append(body["package"])
		self.cursor.execute(statements.CM_ADD_APP_TO_FORBID, value_ip)
		self.db.commit()
		row = self.cursor.fetchall()      
		if row == 0:
			res['error_code'] = 1
			res['messsage'] = 'updated failed'     
		else:
			res['error_code'] = 0
			res['messsage'] = 'updated successfully, number rows:'+str(row)
			self.write(json_encode(res))