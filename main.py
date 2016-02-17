import tornado.ioloop
import tornado.web
from send_mail_handle import SendMailHandle
from get_all_devices_handle import GetAllDevicesHandle
from insert_device_handle import InsertDeviceHandle
from update_password_handle import UpdatePasswordHandle
from forget_password_handle import ForgetPasswordHandle
from log_access_app_handle import LogAccessAppHandle
from your_log_access_handle import YourLogAccessAppHandle
import schedule
import time
import datetime

def make_app():
	return tornado.web.Application([
		(r"/SendMail", SendMailHandle),
		(r"/GetAllDevices", GetAllDevicesHandle),
		(r"/InsertDevice", InsertDeviceHandle),
		(r"/UpdatePassword", UpdatePasswordHandle),
		(r"/ForgetPassword", ForgetPasswordHandle),
		(r"/LogAccessApp", LogAccessAppHandle),
		(r"/GetYourLog", YourLogAccessAppHandle),
		])

def job():
	print("I'm working...")

if __name__ == "__main__":
	print(datetime.datetime.now())
	print"Start Server..."
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()



