import tornado.ioloop
import tornado.web
from send_mail_handle import SendMailHandle
from get_all_devices_handle import GetAllDevicesHandle
from insert_device_handle import InsertDeviceHandle
from update_password_handle import UpdatePasswordHandle
from forget_password_handle import ForgetPasswordHandle

def make_app():
	return tornado.web.Application([
		(r"/SendMail", SendMailHandle),
		(r"/GetAllDevices", GetAllDevicesHandle),
		(r"/InsertDevice", InsertDeviceHandle),
		(r"/UpdatePassword", UpdatePasswordHandle),
		(r"/ForgetPassword", ForgetPasswordHandle)
		])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()