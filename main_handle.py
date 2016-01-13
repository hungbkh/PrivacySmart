import tornado.ioloop
import tornado.web
import MySQLdb

class MainHandle(tornado.web.RequestHandler):
    def initialize(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="0000",
            db="spl_users",
            charset='utf8',
            use_unicode=True)
        self.cursor = self.db.cursor()