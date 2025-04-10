import actions,data


def menu(my_saved_list):
    num_option=0
    my_boolean=False
    system_on=True
    
    while system_on==True:
        try:
            num_option=int(input("Ingrese por favor el número de Opción que desea ingresar. 1-Ingresar información de estudiante, 2-Ver Información de Estudiantes, 3-TOP3 Promedios, 4-Ver Promedio Total, 5-Exportar archivo, 6-Importar archivo previamente exportado, 7-Salir del Programa"))
            if num_option==1:
                actions.input_information(my_saved_list)
            elif num_option==2:
                print(actions.open_csvfile(my_saved_list))
            elif num_option==3:
                print(actions.sorting_top3students(my_saved_list))
            elif num_option==4:
                actions.calculate_total_average(my_saved_list)
            elif num_option==5:
                data.export_file(my_saved_list)
                if my_saved_list!=[]:
                    my_boolean=True
                else:
                    my_boolean=False
            elif num_option==6:
                data.import_file(my_boolean,my_saved_list)
                my_boolean=False
            elif num_option==7:
                system_on=False
            if num_option>7 or num_option<1:
                raise Exception
        except ValueError:
            print("Por favor Ingrese un número en el Menú no se permiten letras o signos")
        except Exception as error:
            print(f'La opción de Menú ingresada es inválida por favor ingrese valores entre 1 y 7 {error}')
        



