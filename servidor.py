import sys
import os, os.path
import random
import string
import json

import cherrypy

from clases import *

class Index(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

@cherrypy.expose
class MenuWebService(object):        
    def GET(self):                
        #return json.dumps([ob.__dict__ for ob in bebidas_disponibles])
        return json.dumps(bebidas_disponibles, default=to_serializable)

@cherrypy.expose
class Detalle(object):        
    def GET(self, id):        
        return open('detalle.html') 

@cherrypy.expose
class DetalleDeBebida(object):
    def GET(self, id):        
        for bebida in bebidas_disponibles:
            if bebida.bebida_id == int(id):
                return json.dumps(bebida, default=to_serializable)

        return None    

@cherrypy.expose
class OrdenarBebida(object):
    def GET(self, id):
        for bebida in bebidas_disponibles:
            if bebida.bebida_id == int(id):
                # Revisar si hay los niveles suficientes para preparar la bebida
                # Agregar bebida a la fila de bebidas
                if(bebida.hay_ingredientes()):
                    queue_de_bebidas.append(bebida)
                    print(queue_de_bebidas)
                    return "La bebida se agregó correctamente a la fila"
                return "No hay suficientes ingredientes para preparar tu bebida"                
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
        '/ordenarBebida': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }

    # Esta lista representa las bebidas disponibles
    bebidas_disponibles = Obtener_bebidas_de_archivo()

    # Representa la fila de bebidas
    queue_de_bebidas = []

    #Aquí configuramos las rutas http y las clases relacionadas
    webapp = Index()
    webapp.menu = MenuWebService()
    webapp.detalle = Detalle()
    webapp.detalleDeBebida = DetalleDeBebida()  
    webapp.ordenarBebida = OrdenarBebida()      
    cherrypy.config.update({
        'server.socket_host' : str(sys.argv[1]),
        'server.socket_port' : 8080,
    })
    cherrypy.quickstart(webapp, '/', conf)