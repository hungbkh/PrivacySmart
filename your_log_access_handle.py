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

class YourLogAccessAppHandle(MainHandle):
    def post(self):
		print"Your log access app..."
		body = tornado.escape.json_decode(self.request.body)        
		res = {}
		dicts = []
		value_ip = []
		value_ip.append(body['email'])
		value_ip.append(body['imei'])
		value_ip.append(datetime.now().strftime('%Y-%m-%d'))
		self.cursor.execute(statements.CM_GET_YOUR_LOG, value_ip)
		rows = self.cursor.fetchall()
		for r in rows:
			t = collections.OrderedDict()
			t['app_name'] = r[4]
			t['gps'] = r[6]
			t['network_ip'] = r[7]
			t['time'] = r[5]
			t['package'] = r[8]
			dicts.append(t)
		self.write(json_encode(dicts))