#DICTIONARIES
#Similar a una lista, permitiendo nombrar articulos, se declara con {}
Nomad = {'type':'rover','color':'black','processor':'JetsonTX1'}
print(Nomad['type'])#Se proporciona la clave o indice para acceder al elemento
#En este ejemplo se sobreescribe el primer elemento
BARB = {'type':'test-bed','color':'black','type':'wheeled'}
print(BARB)
#Los diccionarios se pueden anidar como valores dentro de otros:
myRobots = {'BARB':'WIP','Nomad':'Nomad','Llamabot':'WIP'}
print(myRobots)
#Este ejemplo actualiza un valor en el diccionario a partir del indice
myRobots['Llamabot'] = 'Getting to it'
print(myRobots)
#Un indice puede ser eliminado con la palabra del
del myRobots['Llamabot']
print(myRobots)
#Se puede copiar un diccionario con el metodo copy
workingRobots = myRobots.copy()
print(workingRobots)
#Para agregar un diccionario al final de otro se usa el metodo update
otherRobots = {'Rasbot-pi':'Pi-bot from book','spiderbot':'broken'}
myRobots.update(otherRobots)
print(myRobots)