from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass
    

class Circle(Shape):
    def __init__(self,radius,pi):
        self.radius=radius
        self.pi=pi
    

    def calculate_area(self):
        self.my_area=self.radius*self.radius*self.pi
        return self.my_area
    

    def calculate_perimeter(self):
        self.my_perimeter=2*self.radius*self.pi
        return self.my_perimeter

class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    
    def calculate_area(self):
        self.my_area=self.side*self.side
        return self.my_area

    
    def calculate_perimeter(self):
        self.my_perimeter=4*self.side
        return self.my_perimeter

class Rectangle(Shape):
    def  __init__(self,large,width):
        self.large=large
        self.width=width
    

    def calculate_area(self):
        self.my_area=self.large*self.width
        return self.my_area
    

    def calculate_perimeter(self):
        self.my_perimeter=2*self.large+2*self.width
        return self.my_perimeter


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
                        my_circle=Circle(my_radius,math.pi)
                        print(f'El Perimetro de mi Círculo es de: {my_circle.calculate_perimeter()}')
                        print(f'El Area de mi Círculo es de: {my_circle.calculate_area()}')
                except ValueError:
                    print("No se pueden recibir letras")
                except Exception as err:
                    print("El radio no puede ser negativo")
        
            elif my_operation_number==2:
                try:
                    my_side=int(input("Ingrese Por Favor la medida del lado del Cuadrado al que le desea calcular el área y el perimetro: "))
                    if my_side<0:
                        raise Exception
                    else:
                        my_square=Square(my_side)
                        print(f'El Perimetro de mi Cuadrado es de: {my_square.calculate_perimeter()}')
                        print(f'El Area de mi Cuadrado es de: {my_square.calculate_area()}')
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
                        print(f'El Perimetro de mi Rectángulo es de: {my_rectangle.calculate_perimeter()}')
                        print(f'El Area de mi Rectángulo es de: {my_rectangle.calculate_area()}')
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