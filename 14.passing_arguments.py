#PASSING ARGUMENTS
"""Frecuentemente se requiere dar información a una función, para ello se necesitan 1 o mas variables
para almacenar dicha información, llamadas argumentos."""
def hello_user(first_name, last_name):#Definimos que requiere 2 argumentos para trabajar
    print("Hello " + first_name + " " + last_name + "!")#Regresamos la información de los argumentos
    
#Ahora mandamos llamar a la función previamente creada
hello_user("Jeff", "Cicolani")#Le pasamos por parametro los 2 argumentos que requiere
