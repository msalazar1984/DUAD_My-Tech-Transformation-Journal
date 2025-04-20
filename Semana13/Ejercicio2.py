
def decorator_with_arguments(function):
    def wrapper(*args):
        counter=0
        try:
            for item in args:
                counter+=1
                float(item)
                
        except ValueError:
            print(f'Hay valores en los parametros que no son numeros')
        print(function(*args))
    return wrapper


@decorator_with_arguments
def processing_result(*args):
    for element in args:
        str_result=f'El elemento {element} fue procesado con exito'
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
                for item in my_list:
                    processing_result(item)
            elif int_menu==3:
                my_booleano=False
            if int_menu<1 or int_menu>3:
                raise err
        except ValueError:
            print("El Menu solo puede recibir valores numericos")
        except Exception as err:
            print("En el Menu solo estan disponibles opciones entre 1 y 3")

main()

                        