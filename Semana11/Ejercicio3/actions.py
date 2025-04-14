import csv

class Student():

    def __init__(self,name,grade,score1,score2,score3,score4,average):
        self.name=name
        self.grade=grade
        self.score1=score1
        self.score2=score2
        self.score3=score3
        self.score4=score4
        self.average=average


    def __repr__(self):
        return f'Nombre: {self.name}, Sección: {self.grade}, Nota Español: {self.score1}, Nota Inglés: {self.score2}, Nota Estudios Sociales: {self.score3}, Nota Ciencias: {self.score4}, Promedio: {self.average}'


def open_csvfile(my_list):
    return my_list

    
def input_information(students_info):
    my_booleano=True
    strname=input("Ingrese por favor el nombre del Estudiante: ")
    strgrade=input("Ingrese por favor la sección del Estudiante: ")
    
    while my_booleano==True:
        try:
            int_score1=int(input("Ingrese por favor la Nota de Español : "))
            int_score2=int(input("Ingrese por favor la Nota de Inglés : "))
            int_score3=int(input("Ingrese por favor la Nota de Estudios Sociales : "))
            int_score4=int(input("Ingrese por favor la Nota de Ciencias : "))
            fltaverage=((int_score1+int_score2+int_score3+int_score4)/4)
            my_booleano=False
            if int_score1>100 or int_score1<0 or int_score2>100 or int_score2<0 or int_score3>100 or int_score3<0 or int_score4>100 or int_score4<0:
                print("Estoy aqui")
                raise Exception
            else:
                my_new_student=Student(strname,strgrade,int_score1,int_score2,int_score3,int_score4,fltaverage)
                students_info.append(repr(my_new_student))
                print(f'{students_info}')
            
        except ValueError:
            print("Error de Tipo de Datos: La Nota Ingresada tiene que ser un número")
        except Exception as ex:
            print(f'Error de Valor: Las Notas del Estudiante deben de estar entre 0 y 100')


def sorting_top3students(my_list):    
    try:
        if my_list!=[] or len(my_list)>=3:
            sorted_my_list=sorted(my_list, key=lambda x:x.split('Promedio: ')[1],reverse=True)
            for item in range(0,3):
                print(sorted_my_list[item])
        else:
            raise Exception
    except Exception as error:
        print(f'La Operación no se puede realizar por que no hay suficientes archivos o estudiantes registrados en el sistema')


def calculate_total_average(my_list):
    sum=0
    try:
        if my_list!=[]:
            for item in range(0,len(my_list)):
                start=my_list[item].find("Promedio: ")
                sum=sum+float(my_list[item][start+10:])
            print(sum/len(my_list))
        else:
            raise Exception
    except Exception as error:
        print(f'La Operación no se puede realizar no hay archivos o estudiantes registrados en el sistema{error}')