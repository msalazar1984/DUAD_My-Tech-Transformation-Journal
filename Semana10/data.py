import csv


def export_file(database):
    headers=('Nombre','Sección','Nota Español','Nota Inglés','Nota Estudios Sociales','Nota Ciencias','Promedio')
    file_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana10/ExportStudents.csv"
    try:
        if database!=[]:
            with open(file_path,mode='w',encoding='utf-8') as file:
                writer=csv.DictWriter(file,headers)
                writer.writeheader()
                writer.writerows(database)
            print("El Archivo fue exportado correctamente")
        else:
            raise Exception
    except Exception as error:
        print("El registro del sistema se encuentra vacio no hay archivos o estudiantes creados no hay información que se pueda exportar")



def import_file(my_boolean,my_list):
    file_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana10/ExportStudents.csv"

    my_csv_file=[]
    try:
        if my_boolean==True:
            str_confirm=input("Por favor confirme si desea sobreescribir el registro S/N: ")
            if str_confirm=="S":
                with open(file_path,'r',encoding='utf-8') as file:
                    reader=csv.DictReader(file)
                    for row in reader:
                        my_csv_file.append(row)
                my_list=my_csv_file
                print("Archivo Importado con Éxito")
            if str_confirm=="N":
                print("Ejecución de Importar cancelada con éxito")
        if my_boolean==False:
            raise Exception
        if str_confirm!="S" and str_confirm!="N":
            raise ValueError
    except ValueError:
        print("Ninguno de los valores ingresados corresponde a S o N")
    except Exception as error:
        print(f'No Existe un archivo previamente exportado, no se puede ejecutar la acción de Importar{error}')

    
    


    
