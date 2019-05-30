#STRING MANIPULATION
robot = 'nomad'
#Al utilizar cadenas o listas el primer caracter esta en el indice 0
print(robot[0])
#Con número negativo devuelve el final de la cadena y trabaja hacia atras
print(robot[-1])
#Define un rango indiceinicial:indicefinal
print(robot[0:3])
#Al dejar un indice en blanco el valor es asumido
print(robot[:3])
print(robot[3:])
#Concatenación de strings
print("Ro" + "bot")
#Concatenación de variables
x = "Ro"
y = "bot"
z = x + y
print(z)
#Concatenación de string y variable
print(x + "bot")
#Multiplicación de strings y concatenación
print(2 * "ro" + "bot")#Solo trabaja en literales y no en variables