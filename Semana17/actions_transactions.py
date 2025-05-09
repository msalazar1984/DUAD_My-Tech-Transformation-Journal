import csv,os

class Transaction():

    def __init__(self,type,category,description,date,amount):
        self.type=type
        self.category=category
        self.description=description
        self.date=date
        self.amount=amount
    
    def __repr__(self):
        return f'Type: {self.type}, Category: {self.category}, Description: {self.description}, Date: {self.date}, Amount: {self.amount}'


def validate_input(function):
    def wrapper(arg1,arg2,arg3,arg4,arg5,arg6):
        try:
            if arg2=="" or arg3=="" or arg4=="" or arg5=="" or arg6=="":
                raise err
            else:
                my_result=(function(arg1,arg2,arg3,arg4,arg5,arg6))
                return(my_result)
        except Exception as err:
            return None
    return wrapper


def validate_file(function):
    def wrapper(arg1,arg2):
        try:
            if os.path.exists(arg2):
                my_result=function(arg1,arg2)
                return(my_result)  
            else:
                raise err
        except Exception as err:
            return None
    return wrapper


@validate_input
def input_transaction(my_list,str_type,str_category,str_description,str_date,int_amount):
    my_new_transaction=Transaction(str_type,str_category,str_description,str_date,int_amount)
    my_list.append(my_new_transaction.__repr__())
    return my_list


@validate_file
def import_file(my_list,file_path):
    file_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/Programas/Semana10/DUAD_My-Tech-Transformation-Journal/Semana17/database.csv"
    my_csv_file=[]
    counter=0
    with open(file_path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            my_csv_file.append(row)
            str_type=my_csv_file[counter]['Type']
            str_category=my_csv_file[counter]['Category']
            str_description=my_csv_file[counter]['Description']
            str_date=my_csv_file[counter]['Date']
            int_amount=my_csv_file[counter]['Amount'] 
            my_new_transaction=Transaction(str_type,str_category,str_description,str_date,int_amount)
            my_list.append(my_new_transaction.__repr__())
            counter+=1
    return my_list