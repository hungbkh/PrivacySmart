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

class GetAllDevicesHandle(MainHandle):

    def get(self):
        dicts = []
        self.cursor.execute(statements.CM_TEST)
        rows = self.cursor.fetchall()
        for r in rows:
            t = collections.OrderedDict()
            t['imei'] = r[0]
            t['device_name'] = r[1]
            t['email'] = r[2]     
            t['password'] = r[3]
            t['password_pattern'] = r[4]
            t['password_face'] = r[5]
            t['create_time'] = r[6]
            t['update_time'] = r[7]     
            dicts.append(t)
        self.write(json_encode(dicts))
