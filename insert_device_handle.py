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
from Crypto.Cipher import DES
from datetime import datetime, timedelta
import sys
import re
import base64
from EnDeCrypt import AESCipher

class InsertDeviceHandle(MainHandle):

    def post(self):    
        body = tornado.escape.json_decode(self.request.body)
        print"InsertDeviceHandle"
        endecypr = AESCipher()
        res = {}
        dicts = []
        value_ip = []
        value_ip.append(body['imei'])
        value_ip.append(body['device_name'])
        value_ip.append(body['email'])
        value_ip.append(endecypr.encrypt(parseToken(body['password'])))
        value_ip.append(body['password_pattern'])
        value_ip.append(body['password_face'])
        value_ip.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        value_ip.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(value_ip)
        
        self.cursor.execute(statements.CM_INSERT_DEVICE, value_ip)
        self.db.commit()
        row = self.cursor.fetchall()     
        for r in row:
            print(r)
        if row == 0:
            res['error_code'] = 1
            res['messsage'] = 'updated failed'
        else:
            res['error_code'] = 0
            res['messsage'] = 'updated successfully'
        self.write(json_encode(res))

def parseToken(str):
  cipher = DES.new('oldhouse',DES.MODE_CFB, 'houseold')
  resolved=cipher.decrypt(base64.b64decode(str))
  return resolved