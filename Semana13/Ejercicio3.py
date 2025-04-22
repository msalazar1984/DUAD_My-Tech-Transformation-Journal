from datetime import datetime


class User():
    def __init__(self,day_birth,month_birth,year_birth):
        
        self.date_of_birth=datetime(year_birth,month_birth,day_birth)
        self.today_date=datetime.today()
    

    @property
    def my_age(self):
        self.age=(self.today_date.year-self.date_of_birth.year)
        if self.today_date.month<self.date_of_birth.month or (self.today_date.month==self.date_of_birth.month and self.today_date.day<self.date_of_birth.day):
            self.age-=1
        return self.age


def decorator_with_arguments(function):
    def wrapper(my_user):
        try:
            if my_user.my_age<18:
                raise err
            else:
                my_result=(function(my_user))
                print(my_result)
        except Exception as err:
            print(f'El usuario tiene {my_user.my_age} es menor de edad y por lo tanto no puede proceder')

    return wrapper

@decorator_with_arguments
def processed_age(user):
    my_result=f'La edad del Usuario es de {user.my_age} y se le permite proceder'
    return (my_result)


def main():
    my_boolean=True
    while my_boolean==True:
        try:
            int_operation_menu=int(input("Ingrese por favor la opcion con la que desea proceder 1. Ingresar Fecha de Nacimiento (Dia-Mes-Año), 2. Proceder con la validacion, 3.Salir del Programa"))
            if int_operation_menu==1:
                try:
                    int_dayofbirth=int(input("Ingrese Por Favor el Día de Nacimiento (Solo se permiten valores entre 1 y 31): "))
                    int_monthofbirth=int(input("Ingrese Por Favor el Mes de Nacimiento (Solo se permiten valores entre 1 y 12): "))
                    int_yearofbirth=int(input("Ingrese Por Favor el Año de Nacimiento: (No se pueden ingresar valores mayores al año de la fecha de hoy): "))
                    
                    if int_dayofbirth<1 or int_dayofbirth>31:
                        raise err_day
                    if int_monthofbirth<1 or int_monthofbirth>12:
                        raise err_month
                    if datetime(int_yearofbirth,int_monthofbirth,int_dayofbirth)>datetime.today():
                        raise err_year
                    
                except ValueError:
                    print("Los dias, meses o años solo pueden tener valores numericos no se permiten letras")
                except Exception as err_day:
                    print("Los dias solo pueden ser valores entre 1 y 31")
                except Exception as err_month:
                    print("Los meses solo pueden ser valores entre 1 y 12")
                except Exception as err_year:
                    print("El valor del año es incorrecto, la fecha no puede ser mayor a la fecha de hoy")
        
            if int_operation_menu==2:
                #print(f'{int_dayofbirth}{int_monthofbirth}{int_yearofbirth}')
                try:
                    my_user=User(int_dayofbirth,int_monthofbirth,int_yearofbirth)
                    processed_age(my_user)
                except ValueError:
                    print("Fecha no se puede procesar hay un error en los valores ingresados defina una nueva fecha")
            elif int_operation_menu==3:
                my_boolean=False
            if int_operation_menu<1 or int_operation_menu>3:
                raise err_menu
        except ValueError:
            print(f'El Menú solo recibe valores numéricos no se permiten letras')
        except Exception as err_menu:
            print(f'En el Menú solo se permiten valores entre 1 y 3')


main()