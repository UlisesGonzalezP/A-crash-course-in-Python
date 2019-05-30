#RETURN VALUES
#Frecuentemente se requiere que la función nos devuelva un valor, para ello se utiliza la palabra return como se muestra a continuación:
def how_many(list_of_things):
    count = len(list_of_things)#El metodo len cuenta los valores de la lista
    return count

robots = ["nomad","Ponginator","Alfred"]#Creamos la lista
#Mandamos llamar a la función
print(how_many(robots))

print("\n")
#return puede devolver mas de un valor como se muestra a continuación
def how_manyS(list_of_thingss):
    counts = len(list_of_thingss)
    return counts, 1
#Mandamos llamar a la función
(x, y) = how_manyS(robots)
print(x, y)