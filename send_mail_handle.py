import tornado.ioloop
import tornado.web
import smtplib
from main_handle import MainHandle
from tornado.escape import json_encode
import collections
import statements
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime

class SendMailHandle(MainHandle):
    def post(self):        
        body = tornado.escape.json_decode(self.request.body)
        res = {}
        value_ip = []
        value_ip.append(body['imei'])
        ip_address = body["ip_address"]
        time_request = body["time"]
    	self.cursor.execute(statements.CM_GET_EMAIL, value_ip)
        row = self.cursor.fetchone()
        if row:
            email = row[0]     
            device_name = row[1] 
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('jackcherry1290@gmail.com', 'forever261289')
            msg = MIMEMultipart()
            msg['From'] = "jackcherry1290@gmail.com"
            msg['To'] = "%s"%email
            msg['Subject'] = "SECURITY ALERT"
            body = """
            Failed Login Attempt to your device: %s
            A failed login attempt has occurred on %s, %s.
            Someone from the IP address %s used the device %s to attempt to login to server.
            If you did not attempt to access your account, please contact your Information Technology Security Team immediately.
            """%(str(device_name), str(device_name), str(time_request), str(ip_address), str(device_name))
            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            server.sendmail("jackcherry1290@gmail.com", "%s"%email, text)
            # server.sendmail("jackcherry1290@gmail.com", "loveviet.90bkh@gmail.com", text)
            server.quit()
            res['error_code'] = 0
            res['error_msg'] = 'done'
            self.write(json_encode(res))
            return
        else:
            res['error_code'] = 1
            res['error_msg'] = "Can\'t find email"
            self.write(json_encode(res))
            return
