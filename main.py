from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from util.MailHandler import MailHandler
import logging, email, os
import controllers.Misc
import controllers.Feed

ROOT_DIR = os.path.dirname(__file__)

application = webapp.WSGIApplication(
                                     [MailHandler.mapping()
                                      ,('/',controllers.Misc.NotFound)
                                      ,('/feed/show',controllers.Feed.Show)
                                      ,('/feed/list',controllers.Feed.List)
                                      ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
