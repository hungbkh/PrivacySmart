import tornado.ioloop
import tornado.web
import MySQLdb
from main_handle import MainHandle
import statements
from tornado.escape import json_encode
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import send_mail_helper

class ForgetPasswordHandle(MainHandle):
    def post(self):        
        body = tornado.escape.json_decode(self.request.body)
        res = {}
        value_ip = []
        email = body['email']
        value_ip.append(body['imei'])
        value_ip.append(email)
        self.cursor.execute(statements.CM_FORGET_PASSWORD, value_ip)
        row = self.cursor.fetchone()
        if row:
            password = row[0]
            device_name = row[1]
            if password:
                body = """
                Your password on device: %s is %s.              
                """%(str(device_name), str(password))
                input = [body, email]
                send_mail_helper.SendEmail(input)
                # server = smtplib.SMTP('smtp.gmail.com', 587)
                # server.ehlo()
                # server.starttls()
                # server.login('jackcherry1290@gmail.com', 'forever261289')
                # msg = MIMEMultipart()
                # msg['From'] = "jackcherry1290@gmail.com"
                # msg['To'] = str(body['email'])
                # msg['Subject'] = "PASSWORD RECOVERY"
                # body = """
                # Your password on device: %s is %s.              
                # """%(str(device_name), str(password))
                # msg.attach(MIMEText(body, 'plain'))
                # text = msg.as_string()
                # server.sendmail("jackcherry1290@gmail.com", email, text)
                # # server.sendmail("jackcherry1290@gmail.com", "loveviet.90bkh@gmail.com", text)
                # server.quit()
                res['error_code'] = 0
                res['error_msg'] = 'done'
                self.write(json_encode(res))
                return
            else:     
                res['error_code'] = 1
                res['error_msg'] = "Can\'t find email"
                self.write(json_encode(res))
                return
        else:
            res['error_code'] = 1
            res['error_msg'] = "Can\'t find email"
            self.write(json_encode(res))
            return