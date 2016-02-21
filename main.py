import tornado.ioloop
import tornado.web
import schedule
import time
import datetime

from send_mail_handle import SendMailHandle
from get_all_devices_handle import GetAllDevicesHandle
from insert_device_handle import InsertDeviceHandle
from update_password_handle import UpdatePasswordHandle
from forget_password_handle import ForgetPasswordHandle
from log_access_app_handle import LogAccessAppHandle
from your_log_access_handle import YourLogAccessAppHandle
from forbid_access_handle import ForbidAccessHandle,AddAppToForbidMode

def make_app():
	return tornado.web.Application([
		(r"/SendMail", SendMailHandle),
		(r"/GetAllDevices", GetAllDevicesHandle),
		(r"/InsertDevice", InsertDeviceHandle),
		(r"/UpdatePassword", UpdatePasswordHandle),
		(r"/ForgetPassword", ForgetPasswordHandle),
		(r"/LogAccessApp", LogAccessAppHandle),
		(r"/GetYourLog", YourLogAccessAppHandle),
		(r"/ForbidAccessHandle", ForbidAccessHandle),
		(r"/AddAppToForbidMod", AddAppToForbidMode),
		])

if __name__ == "__main__":
	print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	print"Start Server..."
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()



