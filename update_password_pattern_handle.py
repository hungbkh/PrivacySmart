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

class UpdatePasswordPatternHandle(MainHandle):

    def post(self):    
        body = tornado.escape.json_decode(self.request.body)
        #self.write(body)
        #return
        res = {}
        dicts = []
        value_ip = []
        value_ip.append(body['password'])
        value_ip.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        value_ip.append(body['imei'])

        self.cursor.execute(statements.CM_UPDATE_PASSWORD_DEVICE, value_ip)
        self.db.commit()
        row = self.cursor.fetchall()      
        if row == 0:
            res['error_code'] = 1
            res['messsage'] = 'updated failed'
        else:
            res['error_code'] = 0
            res['messsage'] = 'updated successfully'
        self.write(json_encode(res))
