#IF STATEMENTS
#El siguiente codigo recorre la lista robot y determina si es nomad
robots = ["nomad","Ponginator","Alfred"]#Creamos la lista
for robot in robots:
    if robot == "nomad":
        print("This is Nomad")
    else:
        print(robot + " is not Nomad")

"""La igualdad, un solo signo '=' representa asignación, '==' representa comparación
myRobot = "Nomad"
myRobot == "Ponginator" Devolvera "False"
myRobot == "Nomad"      Devolvera "True"""
print("\n")

#AND y OR para multiples condiciones
for robot in robots:
    if robot == "Ponginator" or robot == "Alfred":
        print("These aren't the droids I'm looking for.")