#CLASSES
class Robot():
    """
    Una simple clase robot
    esta multi-linea de comentarios es un buen lugar
    para poner una descripción de la clase.
    """
    #Define la inicialización de la función
    #Speed un valor entre 0 y 255
    #duration un valor en milisegundos
    def __init__(self, name, desc, color, owner, speed = 125, duration = 100):
        #Inicializamos nuestro robot
        self.name = name
        self.desc = desc
        self.color = color
        self.owner = owner
        self.speed = speed
        self.duration = duration
        
        #Ya que no se tiene un robot fisico, imprimimos mensajes para simular nuestro robot
        def drive_forward(self):
            #Simulamos conducir hacia adelante
            print(self.name.title() + " is driving" + " forward" + str(self.duration) + " milliseconds")

        def drive_backward(self):
            #Simulamos conducir hacia atras
            print(self.name.title() + " is driving" + " backward" + str(self.duration) + " milliseconds")            
            
        def turn_left(self):
            #Simulamos girar a la izquierda
            print(self.name.title() + " is turning" + " right" + str(self.duration) + " milliseconds")
            
        def turn_right(self):
            #Simulamos girar a la derecha
            print(self.name.title() + " is turning" + " left" + str(self.duration) + " milliseconds")
            
        def set_speed(self, speed):
            #Colocamos la velocidad de los motores
            self.speed = speed
            print("the motor speed is now " + str(self.speed))
            
        def set_duration(self, duration):
            #Colocamos la duración del viaje
            self.duration = duration
            print("the duration is now " + str(self.duration)) 