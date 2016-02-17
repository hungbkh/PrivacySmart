import schedule
import time
import datetime
from log_access_app_handle import scheduleSendLogAccessApp

def job():
	print("I'm working...")

print"Start Schedule at %s.."%datetime.datetime.now()
# schedule.every(2).seconds.do(job)
schedule.every().day.at("0:12").do(scheduleSendLogAccessApp)
while 1:
	schedule.run_pending()
	time.sleep(1)