#FOR_LOOP
#Itera un bloque de codigo, por ejemplo una lista, la lee y cuando se queda sin elementos se sale y continua el programa
robots = ["nomad","Ponginator","Alfred"]#Creamos la lista
for robot in robots:
    print(robot)

print("\n")    
#También se pueden recorrer elementos en un diccionario utilizando 2 variables para almacenar los elementos:
Nomad = {'type':'rover','color':'black','processor':'JetsonTX1'}#Creamos el diccionario
for name,data in Nomad.items():
    print(name + ': ' + data)

print("\n")    
#Funcion para enumerar los valores de salida del for
for num,robot in enumerate(robots):
    print(num,robot)