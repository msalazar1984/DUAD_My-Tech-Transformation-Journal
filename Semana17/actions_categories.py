import csv,os


class Category():

    def __init__(self,name,transaction_type,description):
        self.name=name
        self.transaction_type=transaction_type
        self.description=description
    
    def __repr__(self):
        return f'Name: {self.name}, Transaction Type: {self.transaction_type}, Description: {self.description}'


def validate_input(function):
    def wrapper(arg1,arg2,arg3,arg4):
        try:
            if arg2=="" or arg3=="" or arg4=="":
                raise err
            else:
                my_result=(function(arg1,arg2,arg3,arg4))
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
def input_category(my_list,str_category_name,str_transaction_type,str_description):
    my_new_category=Category(str_category_name,str_transaction_type,str_description)
    my_list.append(my_new_category.__repr__())
    return my_list


@validate_file
def import_file(my_list,file_path):
    my_csv_file=[]
    counter=0
    with open(file_path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            my_csv_file.append(row)
            str_category_name=my_csv_file[counter]['Name']
            str_transaction_type=my_csv_file[counter]['Transaction Type']
            str_description=my_csv_file[counter]['Description'] 
            my_new_category=Category(str_category_name,str_transaction_type,str_description)
            my_list.append(my_new_category.__repr__())
            counter+=1
    return my_list  
