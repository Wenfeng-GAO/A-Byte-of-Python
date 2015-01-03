#! /usr/bin/env python
import smtplib

gmail_user = "elricfeng@gmail.com"
gmail_pwd = "secret"
FROM = "elricfeng@gmail.com"
TO = ["elricfeng@gmail.com"] # must be a list
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"

# Prepare actual message
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465) # or port 465
    server.ehlo()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print "Successfully sent the mail"
except smtplib.SMTPException as e:
    print "Failed to send mail", e

