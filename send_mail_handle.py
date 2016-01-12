import tornado.ioloop
import tornado.web
import smtplib
from main_handle import MainHandle
from tornado.escape import json_encode
import collections
import statements

class SendMailHandle(MainHandle):
    def post(self):
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        # server.starttls()
        # server.login('jackcherry1290@gmail.com', 'forever261289')
        # msg = "HI!"
        # server.sendmail("jackcherry1290@gmail.com", "loveviet.90bkh@gmail.com", msg)
        # server.quit()
        # self.write("done")
        # return
        body = tornado.escape.json_decode(self.request.body)
        res = {}
        value_ip = []
        value_ip.append(body['imei'])
    	self.cursor.execute(statements.CM_GET_EMAIL, value_ip)
        row = self.cursor.fetchone()
        if row:
            email = row[0]      
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('jackcherry1290@gmail.com', 'forever261289')
            msg = "HI!"
            server.sendmail("jackcherry1290@gmail.com", "%s"%email, msg)
            # server.sendmail("jackcherry1290@gmail.com", "loveviet.90bkh@gmail.com", msg)
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
