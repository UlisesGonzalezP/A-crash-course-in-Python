#DEFAULT VALUES
#Se puede crear un valor predeterminado para cada argumento de la siguiente manera:
def favorite_thing(favorite = "robotics"):
    print("My favorite thing in the world is " + favorite)
    
#Mandamos llamar a la función pasandole un parametro como argumento
favorite_thing("pie")
#Mandamos llamar a la función con un parametro vacio
favorite_thing()#Para comprobar el valor por defecto definido en la función
