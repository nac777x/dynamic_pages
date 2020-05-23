import webapp2
#import template
import jinja2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
               
        self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write("Hello, it's done!!")
        
        template_folder = jinja2.FileSystemLoader('templates')
        env = jinja2.Environment(loader=template_folder)
        base = env.get_template('base.html')
        
        with open('breweries.json') as mydata:
            brewData = json.loads(mydata)
        
        self.response.out.write(base.render(brewData = brewData))
                
application = webapp2.WSGIApplication([('/', MainPage)], debug=True)
