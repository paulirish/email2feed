from google.appengine.ext import db


class MailMessage(db.Model):
    toAddress = db.StringProperty()
    fromAddress = db.StringProperty()
    subject = db.StringProperty()
    body = db.StringProperty(multiline=True)
    dateSent = db.StringProperty()
    dateReceived = db.DateTimeProperty()


class Recipient(db.Model):
    toAddress = db.StringProperty()