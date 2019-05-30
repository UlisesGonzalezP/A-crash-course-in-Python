#FUNCTIONS
#Codigo predefinido que se puede llamar desde cualquier otra parte del programa
#El siguiente ejemplo corresponde a las acciones de un robot 
while(true):
    if command == turnLeft:
        #Aqui irian las instrucciones para girar a la izquierda
    if command == turnRight:
        #Aqui irian las instrucciones para girar a la derecha
    #Aqui podria ir mas codigo

#Y el siguiente ejemplo muestra como implementar funciones a las acciones anteriores
while(true):
    if command == turnLeft:
        turnLeft()
    if command == turnRight:
        turnRight()
    #Aqui podria ir mas codigo

#Este programa no funciona y genera errores por falta de codigo, solamente es un ejemplo para utilizar funciones.
    