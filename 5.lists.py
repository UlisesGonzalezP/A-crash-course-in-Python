#LISTS
#Se crea una lista con [] y puede trabajar con varios tipos de datos
robots = ["nomad","Ponginator","Alfred"]
print(robots)
#Como los strings, el primer elemento corresponde a la posición o indice 0
print(robots[0])
print(robots[-1])
#Se corta una lista definiendo un rango, lo cual genera una nueva
print(robots[1:3])
#Este ejemplo agrega miembros a la lista
more_bots = robots + ['Roomba','Neato','InMoov']
print(more_bots)
#Este ejemplo cambia miembros en la lista
more_bots[3] = 'ASIMO'
print(more_bots)
#Este ejemplo elimina miembros en una lista
more_bots[3:5] = []
print(more_bots)
#Asignar miembros de una lista a variables:
a,b = more_bots[0:2]
print(a,b)
#Hay varios metodos incluidos en listas automaticamente, por ejemplo:
#el siguiente metodo forza la primer letra a mayuscula
print(robots[0].title())