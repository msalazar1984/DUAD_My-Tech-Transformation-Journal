
def decorator_with_arguments(function):
    def wrapper(*args,**kargs):
        my_boolean=True
        for item in args:
            try:
                if item.isdigit()!=True:
                    my_boolean=False
                    raise err  
            except Exception as err:
                print(f'No todos los valores son numericos')
                break
        if my_boolean==True:
            my_result=function(*args,**kargs)
            print (my_result)
    return wrapper


@decorator_with_arguments
def processing_result(*args,**kargs):
        str_result=f'Proceso completado con exito, todos los valores son numeros'
        return str_result


def main():
    my_booleano=True
    my_list=[]
    while my_booleano==True:
        try:
            int_menu=int(input("Ingrese por favor una opción válida 1. Ingresar elemento 2. Procesar elementos 3. Salir del Programa"))
            if int_menu==1:
                new_element=input("Ingrese por favor un nuevo elemento: ")
                my_list.append(new_element)
            elif int_menu==2:
                processing_result(*my_list)
            elif int_menu==3:
                my_booleano=False
            if int_menu<1 or int_menu>3:
                raise err
        except ValueError:
            print("El Menu solo puede recibir valores numericos")
        except Exception as err:
            print(f'En el Menu solo estan disponibles opciones entre 1 y 3')

main()

                        