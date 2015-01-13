#! usr/bin/env python
import webapp2

class myHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello, world!")

application = webapp2.WSGIApplication([
    ('/.*', myHandler),
], debug=True)
