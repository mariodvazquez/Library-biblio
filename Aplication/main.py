import webapp2
import jinja2
import os

directorio_plantillas = os.path.join(os.path.dirname(__file__), 'vista')
entorno_jinja = jinja2.Environment(loader = jinja2.FileSystemLoader(directorio_plantillas), autoescape = True)

class Handler(webapp2.RequestHandler):
    def render(self, plantilla, **kw):
        self.reponse.out.write(render_str(plantilla, **kw))

    def write(self, *a, *kw):
        self.response.out.write(*a, **kw)

class MainHandler(Handler):
    def get(self):
        self.render('index.html')

class Driver1(Handler):
    def get(self):
    	libros = [{'nombre': 'Harry Potter', 'Fecha': '1997'}, {'nombre': 'Hunger Games', 'Fecha': '2008'}, {'name': 'Divergent', 'Fecha': '2011'},{'nombre': 'Battle Royale', 'Fecha': '1999'}]
        self.render('PaginaHTML1.html', contenido = libros)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/pagina1', Driver1),
], debug=True)
