from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api.mail import EncodedPayload
from models.models import MailMessage, Recipient
import logging
import datetime


class MailHandler(InboundMailHandler):
    def receive(self, message):
        logging.info("Received a message from: " + message.sender)
        mailMessage = MailMessage()
        mailMessage.toAddress = message.to
        mailMessage.fromAddress = message.sender
        mailMessage.subject = message.subject
        mailMessage.body = self._getBody(message)
        mailMessage.dateSent = message.date
        mailMessage.dateReceived = datetime.datetime.now()
        mailMessage.put()
        rcpt = Recipient.gql("where toAddress=:to", to=mailMessage.toAddress).get()
        if (not rcpt):
            Recipient(toAddress=mailMessage.toAddress).put();
        logging.warn(rcpt)
    
    def _getBody(self, message):
        ret = None
        for contentType, body in message.bodies():
            if (contentType == 'text/html'):
                ret = body
                break
            if (contentType == 'text/plain'):
                ret = body
        if isinstance(ret, EncodedPayload):
            ret = ret.decode()
        return ret
            
        
        
        

        