import math

class Circle():
    def __init__(self):
        self.radius=int(input("Por favor ingrese el radio del circulo al que le desea calcular el area: "))


    def getarea(self):
        area=(math.pi) *math.pow(self.radius,2)
        print(area)

my_new_circle=Circle()
my_new_circle.getarea()