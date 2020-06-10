import sys
import os, os.path
import requests
import json
import time
from clases import *
import wiringpi as wiringpi

# Host (ip y puerto)
host_port = "http://" + str(sys.argv[1]) + ":8080"
print("Host y puerto ingresado:", host_port)

# Setup de wiringpi
wiringpi.wiringPiSetup()
# Pines para los leds
wiringpi.pinMode(0, 1)
wiringpi.pinMode(1, 1)
wiringpi.pinMode(2, 1)
wiringpi.pinMode(3, 1)
wiringpi.pinMode(4, 1)
wiringpi.pinMode(5, 1)
#Pines para el sensor de presión
wiringpi.pinMode(21, 0)
wiringpi.pinMode(22, 1)

wiringpi.digitalWrite(22, 1)

while(True):  
    if(wiringpi.digitalRead(21) == 0):        
        wiringpi.digitalWrite(22, 0)
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

            for ingrediente in bebida_a_preparar.ingredientes:
                ingrediente.suministrar_ingrediente()            

            while(wiringpi.digitalRead(21) == 0):                
                pass

            wiringpi.digitalWrite(22, 1)
            
            
        except:
            print("No hay bebida enfilada. Esperar 5 segundos")
            while(wiringpi.digitalRead(21) == 0):                
                pass          

            wiringpi.digitalWrite(22, 1)


