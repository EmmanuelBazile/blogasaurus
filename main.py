import jinja2
import webapp2
import os


the_jinja_enviroment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_enviroment.get_template('index.html')
        self.response.headers['Content-type'] = 'text/html'
        self.response.write(template.render())

# class ResultsPage(webapp2.RequestHandler):
#     def get(self):
#         template = the_jinja_enviroment.get_template('results.html')
#         self.response.headers['Content-type'] = 'text/html'
#         self.response.write(template.render())


app = webapp2.WSGIApplication([
('/', IndexPage),
# ('/results', ResultsPage),

], debug=True)
