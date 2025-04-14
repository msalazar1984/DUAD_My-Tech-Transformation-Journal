import csv


def open_csvfile(my_list):
    return my_list

    
def input_information(students_info):
    grades_dict={}
    students_header=['Nombre','Sección','Nota Español','Nota Inglés','Nota Estudios Sociales','Nota Ciencias']
    students_info_values=[]
    index=0
    counter=0
    sum=0
    int_grades=[]
    signatures_names=['Español','Inglés','Estudios Sociales','Ciencias']
    str_studentname=input("Ingrese por favor el nombre del Estudiante: ")
    str_grade=input("Ingrese por favor la sección del estudiante: ")
    students_info_values.append(str_studentname)
    students_info_values.append(str_grade)
    
    while counter<=3:
        try:
            
            my_variable=int(input(f'Ingrese por favor la Nota de {signatures_names[counter]}{counter}: '))
            if my_variable>100 or my_variable<0:
                #print(f'{int_grades[index]}{index}')
                raise Exception
            else:
                int_grades.append(my_variable)
                students_info_values.append(int_grades[counter])
            counter+=1
        except ValueError:
            print("Error de Tipo de Datos: La Nota Ingresada tiene que ser un número")  
        except Exception as ex:
            print(f'Error de Valor: Las Notas del Estudiante deben de estar entre 0 y 100')
        
    for item in students_header:
        grades_dict[item]=students_info_values[index]
        if (index>=2):
            sum=sum+students_info_values[index]
        index+=1
    
    grades_dict['Promedio']=(sum/4)
    students_header.append('Promedio')
    students_info.append(grades_dict)
    print("Estudiante almacenado con Éxito")


def sorting_top3students(my_list):
    top_students_name=[]
    top_students_average=[]
    my_dictionary={}
    top_students=[]
    
    try:
        if my_list!=[] and len(my_list)>=3:
            my_list.sort(key=lambda x: x['Promedio:'],reverse=True)
            for item in range(0,3):
                top_students_name.append(my_list[item]['Nombre'])
                top_students_average.append(my_list[item]['Promedio'])
                my_dictionary['Nombre']=top_students_name[item]
                my_dictionary['Promedio']=top_students_average[item]
                top_students.append(my_dictionary)
                my_dictionary={}
            print (top_students)
        else:
            raise Exception
    except Exception as error:
        print(f'La Operación no se puede realizar por que no hay suficientes archivos o estudiantes registrados en el sistema')


def calculate_total_average(my_list):
    sum=0
    try:
        if my_list!=[]:
            for item in range(0,len(my_list)):
                sum=sum + float(my_list[item]['Promedio'])
            print (sum/len(my_list))
        else:
            raise Exception
    except Exception as error:
        print("La Operación no se puede realizar no hay archivos o estudiantes registrados en el sistema")