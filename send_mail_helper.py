from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

def SendEmail(input):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jackcherry1290@gmail.com', 'forever261289')
    msg = MIMEMultipart()
    msg['From'] = "jackcherry1290@gmail.com"
    msg['To'] = str(input[1])
    msg['Subject'] = "PASSWORD RECOVERY"
    # body = """
    # Your password on device: %s is %s.              
    # """%(str(device_name), str(password))
    msg.attach(MIMEText(input[0], 'plain'))
    text = msg.as_string()
    server.sendmail("jackcherry1290@gmail.com", input[1], text)
    # server.sendmail("jackcherry1290@gmail.com", "loveviet.90bkh@gmail.com", text)
    server.quit()