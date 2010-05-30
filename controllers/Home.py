from google.appengine.ext import webapp

class Index(webapp.RequestHandler):
    def get(self):
        self.response.out("home")
