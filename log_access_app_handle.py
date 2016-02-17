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

db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="0000",
            db="spl_users",
            charset='utf8',
            use_unicode=True)
# db = MySQLdb.connect(
#             host="localhost",
#             user="root",
#             passwd="forever2612",
#             db="spl_users",
#             charset='utf8',
#             use_unicode=True)
# you must create a Cursor object. It will let
#  you execute all the queries you need
cursor = db.cursor()

class LogAccessAppHandle(MainHandle):
    def post(self):    
        print"Log access app..."
        body = tornado.escape.json_decode(self.request.body)        
        res = {}
        dicts = []
        value_ip = []
        value_ip.append(body['imei'])
        value_ip.append(body['device_name'])
        value_ip.append(body['app_name'])
        value_ip.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        value_ip.append(body['gps'])
        value_ip.append(body['network_ip'])
        value_ip.append(body['package'])

        self.cursor.execute(statements.CM_LOG_ACCESS, value_ip)
        self.db.commit()
        row = self.cursor.fetchall()      
        if row == 0:
            res['error_code'] = 1
            res['messsage'] = 'updated failed'
        else:
            res['error_code'] = 0
            res['messsage'] = 'updated successfully'
            self.write(json_encode(res))    

def scheduleSendLogAccessApp():
    print("scheduleSendLogAccessApp")
    cursor.execute(statements.CM_EMAILS)
    rows = cursor.fetchall() 
    for row in rows:
        print("email:"+str(row[0]))
        vi = []
        vi.append(str(row[0]));
        vi.append(datetime.now().strftime('%Y-%m-%d'))
        cursor.execute(statements.CM_GET_LOG, vi)
        log_rows = cursor.fetchall() 
        content_mail = ''
        for log_row in log_rows:
            content_mail += "Device name:"+str(log_row[3]) + "  "
            content_mail += "App name:"+str(log_row[4])+"  "
            content_mail += "GPS:"+str(log_row[6])+"  "
            content_mail += "Network ip:"+str(log_row[7])+"  "
            content_mail += "At:"+str(log_row[5])+"\n"
        if content_mail != '':
            mail = [content_mail, str(row[0]),datetime.now().strftime('%Y-%m-%d')]
            sendEmail(mail)

def sendEmail(input):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jackcherry1290@gmail.com', 'forever261289')
    msg = MIMEMultipart()
    msg['From'] = "jackcherry1290@gmail.com"
    msg['To'] = str(input[1])
    msg['Subject'] = "LOG ACCESS TO YOUR APPS %s" % input[2]
    # body = """
    # Your password on device: %s is %s.              
    # """%(str(device_name), str(password))
    msg.attach(MIMEText(input[0], 'plain'))
    text = msg.as_string()
    server.sendmail("jackcherry1290@gmail.com", input[1], text)
    # server.sendmail("jackcherry1290@gmail.com", "loveviet.90bkh@gmail.com", text)
    server.quit()            