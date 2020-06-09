from clases import Bebida
from clases import Ingrediente
from clases import Materia_prima

bebidas_disponibles = [
        Bebida(0, "Cuba", "Esta es una bebida que se prepara con Ron y Coca", [
            Ingrediente(50, Materia_prima(0, "Ron", True)),
            Ingrediente(100, Materia_prima(1, "Coca", False))
        ]),
        Bebida(1, "Paloma", "No se utilizan palomas de verdad eh! jajaja saludos", [
            Ingrediente(113, Materia_prima(2, "Tequila", True)),
            Ingrediente(200, Materia_prima(3, "Toronja", False))
        ])
    ]

for bebida in bebidas_disponibles:
    print(bebida.nombre)
    print("Tiene alcochol: " + str(bebida.es_bebida_alcocholica()))
    print(bebida.obtener_ingredientes())
    print()