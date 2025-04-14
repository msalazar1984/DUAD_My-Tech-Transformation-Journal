import csv,os,actions


def export_file(database):
    headers=('Nombre','Sección','Nota Español','Nota Inglés','Nota Estudios Sociales','Nota Ciencias','Promedio')
    my_values_list=[]
    my_students_dict={}
    my_students=[]
    index=0
    file_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana11/Ejercicio3/ExportStudents.csv"
    add_str=": "
    counter=0
    try:
        if database!=[]:
            while counter<=len(database)-1:
                for item in range(0,len(headers)):
                    start=database[counter].find(f'{headers[item]}{add_str}')
                    if item!=len(headers)-1:
                        end=database[counter].find(",",start)
                        my_values_list.append(database[counter][start+len(f'{headers[item]}{add_str}'):end])
                    else:
                        my_values_list.append(database[counter][start+len(f'{headers[item]}{add_str}'):])
                for element in headers:
                    my_students_dict[element]=my_values_list[index]
                    index+=1
                index=0
                print(my_students_dict)
                my_students.append(my_students_dict)
                my_students_dict={}
                my_values_list=[]
                counter+=1
            with open(file_path,mode='w',encoding='utf-8') as file:
                writer=csv.DictWriter(file,headers)
                writer.writeheader()
                writer.writerows(my_students)
                print("El Archivo fue exportado correctamente")
        else:
            raise Exception
    except Exception as error:
        print(f'El registro del sistema se encuentra vacio no hay archivos o estudiantes creados no hay información que se pueda exportar{error}')



def import_file(my_list):
    file_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana11/Ejercicio3/ExportStudents.csv"
    my_csv_file=[]
    counter=0
    try:
        if os.path.exists(file_path):
            str_confirm=input("Por favor confirme si desea sobreescribir el registro S/N: ")
            if str_confirm=="S":
                with open(file_path,'r',encoding='utf-8') as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                        my_csv_file.append(row)
                        str_name=my_csv_file[counter]['Nombre']
                        str_grade=my_csv_file[counter]['Sección']
                        score1=my_csv_file[counter]['Nota Español']
                        score2=my_csv_file[counter]['Nota Inglés']
                        score3=my_csv_file[counter]['Nota Estudios Sociales']
                        score4=my_csv_file[counter]['Nota Ciencias']
                        average=my_csv_file[counter]['Promedio']
                        
                        my_new_student=actions.Student(str_name,str_grade,score1,score2,score3,score4,average)
                        my_list.append(actions.Student.__repr__(my_new_student))
                        counter+=1
                    print("Archivo Importado con Éxito")
            if str_confirm=="N":
                print("Ejecución de Importar cancelada con éxito")
        else:
            raise Exception
        if str_confirm!="S" and str_confirm!="N":
            raise ValueError
    except ValueError:
        print("Ninguno de los valores ingresados corresponde a S o N")
    except Exception as error:
        print(f'No Existe un archivo previamente exportado, no se puede ejecutar la acción de Importar')
    return my_list
    
    


    
