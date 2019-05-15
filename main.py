'''Importamos las librerías -turtle, para utilizar las tortugas- y -random, para poder invocar valores aleatorios-.'''
import turtle
import random
import ToolBox_Carrera

'''Nuestra clase principal (objeto) será la carrera propiamente dicha.'''
class Carrera():
    '''La clase constructor contendrá los atributos (todos privados) de los cuales podremos setear la distancia de la carrera, el número de tortugas corredoras y el máximo avance por turno.'''
    def __init__(self):
        '''Fijamos la anchura de la pista en 540 pixels (suficiente para poder albergar cómodamente hasta 8 calles para otras tantas tortugas corredoras).'''
        self.__ancho = 540

        '''Preguntaremos si se desea introducir el largo de la pista (distancia en pixels, de mínimo 400 y de máximo 1600) que recorrerán las tortugas. Si no se hace se fijará en 1000.'''
        pideValor = ToolBox_Carrera.solIntOrN("Distancia establecida en 1000 pixels.\nSi te parece bien pulsa N.\nSi deseas cambiarla introduce un nuevo valor: ", minimo = 400, maximo = 1600)
        
        if pideValor == "N":
            self.__largo = 1200
        else:
            self.__largo = 200 + pideValor
        
        '''Fijamos un mínimo de 2 corredoras, pero preguntaremos si se desean más (hasta un máximo de ocho).'''
        pideValor = ToolBox_Carrera.solIntOrN("\nTenemos 2 corredoras.\nSi te parece bien pulsa N.\nSi no, dinos cuantas quieres ver correr: ", minimo = 2, maximo= 8)
        
        if pideValor == "N":
            self.__tortus = 2
        else:
            self.__tortus = pideValor
        
        '''Colocamos la línea de salida y la de meta.'''        
        self.__salida = 100 - (self.__largo / 2)
        self.__meta = (self.__largo / 2) - 100
        
        '''Calculamos el ancho de la calle para cada corredora.'''
        self.__calle = self.__ancho / self.__tortus

        '''Una vez fijada la parametrización, pintamos la pista de carreras.'''
        self.__pista()

        '''Para finalizar, creamos a las corredoras'''
        self.__corredoras = []
        self.__creaTortus()

    '''Esta clase privada (sólo invocada desde el constructor) se ocupará de dibujar la pista de carreras.'''
    def __pista(self):
        '''Para la pista se generará una instancia Screen -de la clase turtle- que se parametrizará con un color de fondo y las medidas de largo y ancho establecidas.'''
        self.__pantalla = turtle.Screen()
        self.__pantalla.bgcolor("lightgray")
        self.__pantalla.setup(self.__largo, self.__ancho)
        
        '''Pintamos las líneas demarcadoras de la pista.'''
        self.__pintaRayas()

    '''Esta clase privada (sólo invocada desde el constructor) se ocupará de dibujar las líneas, de salida/meta y las separaciones de las calles, de la pista de carreras.'''
    def __pintaRayas(self):
        '''Para dibujar, generamos una tortuga, que es una instancia Turtle -de la clase turtle-.''' 
        pintaRayas = turtle.Turtle()
        
        '''Fijamos que esta tortuga sea invisible, que pinte en negro, con una achura de 2 y a la máxima velocidad posible.'''
        pintaRayas.hideturtle()
        pintaRayas.pencolor("black")
        pintaRayas.pensize(2)
        pintaRayas.speed(10)
        
        '''Levantamos el lápiz. Colocamos la tortuga en la posición inferior de la ubicación de la linea de salida y la giramos para que apunte hacia arriba.'''
        pintaRayas.penup()
        pintaRayas.setpos(self.__salida, - self.__calle * self.__tortus / 2)
        pintaRayas.left(90)
        
        '''Bajamos el lápiz y pintamos una línea, haciendo avanzar a la tortuga una distancia igual a la anchura de la pista de carreras.'''
        pintaRayas.pendown()
        pintaRayas.forward(self.__ancho)
        
        '''Levantamos el lápiz. Colocamos la tortuga en la posición superior de la ubicación de la linea de meta.'''
        pintaRayas.penup()        
        pintaRayas.setx(self.__meta)
        
        '''Bajamos el lápiz y pintamos una línea, haciendo retroceder a la tortuga una distancia igual a la anchura de la pista de carreras.'''
        pintaRayas.pendown()
        pintaRayas.back(self.__ancho)
        
        '''Levantamos el lápiz. Giramos la tortuga para que apunte hacia la izquierda.'''
        pintaRayas.penup()
        pintaRayas.right(90)
        
        '''Para pintar las líneas de separación de las calles de la pista de carreras tendremos que ir colocándola de forma consecutiva a intervalos equidistantes por la anchura de la pista.'''
        '''Calculamos la primera posición del eje Y e iteramos para pintar un numero de líneas demarcadoras igual al numero de corredoras menos uno.'''
        dondeY = self.__calle - (self.__ancho / 2)
        for i in range(self.__tortus - 1):
            '''En cada iteración, colocamos la tortuga en su posición Y calculada y en una posición X anticipada quince pixels a la línea de salida y pintamos esos quince pixels.'''
            pintaRayas.setpos(self.__salida - 15, dondeY)
            pintaRayas.pendown()
            pintaRayas.forward(15)
            pintaRayas.penup()
            
            '''Pintamos una línea discontínua, controlando que la posición X de la tortuga no sobrepase la línea de meta.'''
            while pintaRayas.xcor() < self.__meta:                
                '''Bajamos el lápiz y pintamos 60 pixels si podemos... si no, los que se puedan.'''
                pintaRayas.pendown()
                if (self.__meta - pintaRayas.xcor()) >= 60:
                    pintaRayas.forward(60)
                else:
                    pintaRayas.forward(self.__meta - pintaRayas.xcor())
                
                '''Levantamos el lápiz y avanzamos 40 pixels si podemos, si no, los que se puedan.'''
                pintaRayas.penup()
                if (self.__meta - pintaRayas.xcor()) >= 40:
                    pintaRayas.forward(40)
                else:
                    pintaRayas.forward(self.__meta - pintaRayas.xcor())
                        
            '''Tras completar la línea discontínua, pintamos quince pixels tras la línea de meta.'''
            pintaRayas.pendown()
            pintaRayas.forward(15)
            pintaRayas.penup()
            
            '''Finalizamos la iteración calculando la siguiente posición Y para pintar un nueva línea de separación de calles.'''
            dondeY += self.__calle

    '''Esta clase privada (sólo invocada desde el constructor) se ocupará de crear las tortugas corredoras.'''   
    def __creaTortus(self):
        '''Fijamos una tupla de ocho colores, para un máximo de ocho tortugas corredoras.'''
        self.__colores = ("red", "green", "blue", "orange", "purple", "gray", "yellow", "black")

        '''Calculamos la posición central de una calle como el punto medio de su ancho. Y fijamos la posición Y inicial para la primera tortuga corredora.''' 
        espacio = self.__calle / 2
        ini = 1 - self.__tortus

        '''Adecuamos el tamaño de las tortugas corredoras en función de cuantas sean en total.'''
        tama = 9 - self.__tortus
        
        '''Las tortugas irán colocando centradas, desde la de la calle inferior a la de la calle superior. Iteramos tantas veces como tortugas corredoras haya.'''        
        for i in range(self.__tortus):
            '''Las corredoras serán instancias Turtle -de la clase turtle-, con forma de tortuga, a las que fijaremos su tamaño y su color (mediante la tupla de colores).'''
            tortuga = turtle.Turtle()
            tortuga.shape("turtle")
            tortuga.shapesize(tama, tama)
            tortuga.color(self.__colores[i])
                
            '''Levantamos el lápiz porque no queremos que las corredoras pinten y colocamos cada una en la línea de salida de su calle.'''
            tortuga.penup()
            tortuga.setpos(self.__salida, ini * espacio)
            
            '''Cada corredora se añade a un lista, para poder iterarlas durante la competición.'''
            self.__corredoras.append(tortuga)
            
            '''Calculamos la posición Y inicial para la siguiente tortuga corredora.'''
            ini += 2

    '''Esta clase será la que inicie la carrera y dilucide la tortuga ganadora.'''
    def competir(self):        
        '''Fijamos el máximo de avance en función del largo establecido para la pista.'''      
        maxAvance = round(self.__largo / 150, 0)
        
        '''Iteraremos turnos, mientras que ninguna tortuga rebase la meta.'''
        final = False
        while not final:
            for tortuga in self.__corredoras:
                '''Para cada tortuga corredora generamos un número aleatorio (entre 1 y el máximo de avance) y la hacemos avanzar esos pixels.'''
                avance = random.randint(1, maxAvance)
                tortuga.fd(avance)
                
                '''Si la posición X de la tortuga corredora rebasa la meta, activamos la condición de salida de la iteración de turnos y damos el mensaje con la ganadora.'''
                if tortuga.xcor() >= self.__meta:
                    final = True
                    color = tortuga.fillcolor()
                    print("\n...and the WINNER is the {} TURTLE.".format(color.upper()))
                
                    '''Forzamos la salida del bucle de iteración de las corredoras para que (en este mismo turno) ninguna otra pueda rebasar la meta.'''
                    break

if __name__ == "__main__":
    miCarrera = Carrera()
    miCarrera.competir()