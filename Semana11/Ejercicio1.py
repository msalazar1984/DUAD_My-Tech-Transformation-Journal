import math

class Circle():
    def __init__(self):
            self.radius=int(input("Por favor ingrese el radio del círculo al que le desea calcular el área: "))


    def get_area(self):
        area=(math.pi) *math.pow(self.radius,2)
        return area


def calculate_area():
    
    try:
        my_new_circle=Circle()
        if my_new_circle.radius<0:
            raise Exception
        else:
            print(my_new_circle.get_area())
    except ValueError:
        print("En el valor del radio no se permiten letras")
    except Exception as ex:
        print("No se puede calcular el área, el radio es negativo")


calculate_area()
