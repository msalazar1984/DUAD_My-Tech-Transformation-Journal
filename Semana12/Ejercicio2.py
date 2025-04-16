from abc import ABC, abstractmethod
import math


class Shape(ABC):
        

    def calculate_perimeter(self,constant,large,width):
        self.constant=constant
        self.large=large
        self.width=width
        my_perymeter=(2*self.constant*self.large)+(2*self.width)
        return my_perymeter


    def calculate_area(self,constant,large,width):
        self.constant=constant
        self.large=large
        self.width=width
        my_area=(constant*large*width)
        return my_area
    

class Circle(Shape):
    def __init__(self,radius,pi,width):
        self.radius=radius
        self.pi=pi
        self.width=width
    

class Square(Shape):
    def __init__(self,large,width):
        self.large=large
        self.width=width


class Rectangle(Shape):
    def  __init__(self,large,width):
        self.large=large
        self.width=width


def my_results():
    my_boolean=True
    while my_boolean==True:
        try:
            my_operation_number=int(input("Ingrese por favor el numero de operacion: 1.Circulo, 2.Cuadrado, 3.Rectangulo, 4. Salir"))
        
            if my_operation_number==1:
                try:
                    my_radius=int(input("Ingrese Por Favor el radio del círculo al que le desea calcular el área y el perimetro: "))
                    if my_radius<0:
                        raise Exception
                    else:
                        my_circle=Circle(my_radius,math.pi,0)
                        print(f'El Perimetro de mi Círculo es de: {my_circle.calculate_perimeter(my_circle.pi,my_circle.radius,my_circle.width)}')
                        print(f'El Area de mi Círculo es de: {my_circle.calculate_area(my_circle.pi,my_circle.radius,my_circle.radius)}')
                except ValueError:
                    print("No se pueden recibir letras")
                except Exception as err:
                    print("El radio no puede ser negativo")
        
            elif my_operation_number==2:
                try:
                    my_large=int(input("Ingrese Por Favor la medida del lado del Cuadrado al que le desea calcular el área y el perimetro: "))
                    if my_large<0:
                        raise Exception
                    else:
                        my_square=Square(my_large,my_large)
                        print(f'El Perimetro de mi Cuadrado es de: {my_square.calculate_perimeter(1,my_square.large,my_square.width)}')
                        print(f'El Area de mi Cuadrado es de: {my_square.calculate_area(1,my_square.large,my_square.large)}')
                except ValueError:
                    print("No se pueden recibir letras")
                except Exception as err:
                    print("El lado no puede ser negativo")

            elif my_operation_number==3:
                try:
                    my_large=int(input("Ingrese Por Favor la medida del largo del Rectángulo al que le desea calcular el área y el perimetro: "))
                    my_width=int(input("Ingrese Por Favor la medida del ancho del Rectángulo al que le desea calcular el área y el perimetro: "))
                    if my_large<0 or my_width<0:
                        raise Exception
                    else:
                        my_rectangle=Rectangle(my_large,my_width)
                        print(f'El Perimetro de mi Rectángulo es de: {my_rectangle.calculate_perimeter(1,my_rectangle.large,my_rectangle.width)}')
                        print(f'El Area de mi Rectángulo es de: {my_rectangle.calculate_area(1,my_rectangle.large,my_rectangle.width)}')
                except ValueError:
                    print("No se pueden recibir letras")
                except Exception as err:
                    print("El Largo o ancho no puede ser negativo")
            elif my_operation_number==4:
                my_boolean=False
            if my_operation_number<1 or my_operation_number>4:
                raise Exception
        except ValueError:
            print("En el Menu no se pueden recibir letras")
        except Exception as err:
            print("La opcion del menu tiene que estar entre 1 o 4")


my_results()