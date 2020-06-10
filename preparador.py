import sys
import os, os.path
import requests
import json
from clases import *

host_port = "http://" + str(sys.argv[1]) + ":8080"
print("Host y puerto ingresado:", host_port)

r = requests.get(host_port + "/siguienteEnFila")
print(r.status_code)

try:    
    print(r.json())    
    data = r.json()    



    ingredientes_de_bebida = []        
    for ingrediente in data['ingredientes']:            
        ingredientes_de_bebida.append(Ingrediente(ingrediente['cantidad_en_ml'], Materia_prima(ingrediente['Materia_prima']['materia_prima_id'], ingrediente['Materia_prima']['nombre'], ingrediente['Materia_prima']['tiene_alcohol'])))

    bebida_a_preparar = Bebida(data['bebida_id'], data['nombre'], data['descripcion'], ingredientes_de_bebida)

    print(len(bebida_a_preparar.ingredientes))
    
except:
    print("No hay bebida enfilada. Esperar 5 segundos")


