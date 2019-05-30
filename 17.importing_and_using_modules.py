#IMPORTING AND USING MODULES
#Para importar modulos se utiliza la palabra import + el nombre del modulo, por ejemplo:
import math
print(math.sqrt(9))

"""El anterior ejemplo importa todos los metodos del paquete math, si solo se desea 
importar una parte del modulo se hace lo siguiente"""
from math import sqrt
print(sqrt(9))

#También se puede importar el modulo definiendolo con un alias:
import math as m
print(m.sqrt(9))    
#Se importa un solo metodo con alias:
from math import sqrt as s
print(s(9))