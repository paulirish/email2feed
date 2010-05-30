import os
import sys
from google.appengine.ext import webapp
from models.models import Recipient, MailMessage
from google.appengine.ext.webapp import template
import main
from urlparse import urlparse

class Index(webapp.RequestHandler):
    def get(self):
        self.response.out("home")
        
class Show(webapp.RequestHandler):
    def get(self):
        email = self.request.get("e")
        messages = MailMessage.all().filter("toAddress = ",email).order("-dateReceived")

        
        viewdata = { 'messages':messages
                    ,'to':email}

        path = os.path.join(main.ROOT_DIR, 'views/feed/show.html')
        self.response.out.write(template.render(path, viewdata))
    

class List(webapp.RequestHandler):
    def get(self):
         
        viewdata = {'recipients':Recipient.all()}

        path = os.path.join(main.ROOT_DIR, 'views/feed/list.html')
        self.response.out.write(template.render(path, viewdata))
