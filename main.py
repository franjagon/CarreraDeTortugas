'''Importamos las librerías -turtle, para utilizar las tortugas- y -random, para poder invocar valores aleatorios-.'''
import turtle
import random

'''Nuestra clase principal será la carrera propiamente dicha.'''
class Carrera():
    
    def __init__(self, ancho, alto, tortus, dados):
        self.__pantalla = turtle.Screen()
        self.__pantalla.bgcolor("lightgray")
        
#        input("Distancia establecida en 12 (cm), si deseas cambiarla introduce un nuevo valor: ")
        
        self.__pantalla.setup(ancho, alto)
        
        self.__dados = dados
        self.__salida = 100 - (ancho / 2)
        self.__meta = (ancho / 2) - 100
        self.__carril = alto / tortus
        
        self.__corredoras = []
        
        self.__pintaRayas(tortus)
           
        self.__creaTortus(tortus)
    
    def __pintaRayas(self, tortus):
        pintaRayas = turtle.Turtle()
        pintaRayas.hideturtle()
        pintaRayas.pencolor("black")
        pintaRayas.pensize(2)
        pintaRayas.speed(10)
        pintaRayas.penup()
        pintaRayas.setpos(self.__salida, - self.__carril * tortus / 2)
        pintaRayas.pendown()
        pintaRayas.left(90)
        pintaRayas.forward(self.__carril * tortus)
        pintaRayas.penup()
        
        pintaRayas.setx(self.__meta)
        pintaRayas.pendown()
        pintaRayas.back(self.__carril * tortus)
        pintaRayas.penup()
        pintaRayas.right(90)
        
        dondeY = self.__carril - (self.__carril * tortus / 2)
        for i in range(tortus - 1):
            pintaRayas.setpos(self.__salida - 10, dondeY)
            while pintaRayas.xcor() < self.__meta + 10:
                pintaRayas.pendown()
                pintaRayas.forward(45)
                pintaRayas.penup()
                pintaRayas.forward(20)
            dondeY += self.__carril
        
    def __creaTortus(self, tortus):
        self.__colores = ("red", "green", "blue", "orange", "purple", "gray", "yellow", "black")
        
        espacio = self.__carril / 2
        ini = 1 - tortus
        tama = 9 - tortus
        
        for i in range(tortus):
            tortuga = turtle.Turtle()
            tortuga.color(self.__colores[i])
            tortuga.penup()
            tortuga.shape("turtle")
            tortuga.shapesize(tama, tama)
            tortuga.setpos(self.__salida, ini * espacio)
            self.__corredoras.append(tortuga)
            ini += 2
        
    def competir(self):
        final = False
        while not final:
            for tortuga in self.__corredoras:
                avance = random.randint(1, self.__dados * 6)
                tortuga.fd(avance)
                if tortuga.xcor() >= self.__meta:
                    final = True
                    color = tortuga.fillcolor()
                    print("...and the WINNER is the {} TURTLE.".format(color.upper()))
                    break

if __name__ == "__main__":
    miCarrera = Carrera(1200, 540, 8, 12)
    miCarrera.competir()