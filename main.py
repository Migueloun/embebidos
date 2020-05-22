import sys
import os, os.path
import random
import string
import json

import cherrypy

from bebida import Bebida

class Index(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

@cherrypy.expose
class MenuWebService(object):        
    def GET(self):                
        return json.dumps([ob.__dict__ for ob in bebidas])

@cherrypy.expose
class Detalle(object):        
    def GET(self, id):
        return open('detalle.html') 

@cherrypy.expose
class DetalleDeBebida(object):
    def GET(self, id):        
        for bebida in bebidas:
            if bebida.bebida_id == int(id):
                return json.dumps(bebida.__dict__)

        return None    

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/menu': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/detalle': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True
        },
        '/detalleDeBebida': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    bebidas = [
        Bebida(1, "Paloma", True),
        Bebida(2, "Cuba", True),
        Bebida(3, "Martini", True),
        Bebida(4, "Frutsi", False)
    ]

    webapp = Index()
    webapp.menu = MenuWebService()
    webapp.detalle = Detalle()
    webapp.detalleDeBebida = DetalleDeBebida()        
    cherrypy.config.update({
        'server.socket_host' : str(sys.argv[1]),
        'server.socket_port' : 8080,
    })
    cherrypy.quickstart(webapp, '/', conf)