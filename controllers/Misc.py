from google.appengine.ext import webapp

class NotFound(webapp.RequestHandler):
    def get(self):
        self.error(404)        
        self.response.out.write("not found")
        