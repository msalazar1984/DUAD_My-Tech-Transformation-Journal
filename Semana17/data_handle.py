import csv,os


def validate_file(function):
    def wrapper(arg1,arg2):
        try:
            if os.path.exists(arg1):
                my_result=function(arg1,arg2)
                return(my_result)  
            else:
                raise err
        except Exception as err:
            return None
    return wrapper


def format_currency(value):
    try:
        return "₵{:,.0f}".format(float(value))
    except ValueError:
        return value

@validate_file
def filter_csv(file_path,str_transaction_type):
    my_list=[]
    with open(file_path,'r',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            my_list.append(row)
    filtered_data=[item for item in my_list if item['Transaction Type']==str_transaction_type]
    return filtered_data


def find_category(str_value,my_list):
    my_boolean=False
    for item in range(0,len(my_list)):
        if my_list[item]['Name']==str_value:
            my_boolean=True
    if my_boolean==True:
        return True
    else:
        return False


def structuring_file_to_export(my_database,headers):
    add_str=": "
    counter=0
    index=0
    my_database_values=[]
    my_categories_dict={}
    my_categories=[]
    #try:
    if my_database!=[]:
        while counter<=len(my_database)-1:
                
            for item in range(0,len(headers)):
                start=my_database[counter].find(f'{headers[item]}{add_str}')
                if item!=len(headers)-1:
                    end=my_database[counter].find(",",start)
                    my_database_values.append(my_database[counter][start+len(f'{headers[item]}{add_str}'):end])
                else:
                    my_database_values.append(my_database[counter][start+len(f'{headers[item]}{add_str}'):])
            
            for element in headers:
                my_categories_dict[element]=my_database_values[index]
                index+=1
            index=0
            my_categories.append(my_categories_dict)
            my_categories_dict={}
            my_database_values=[]
            counter+=1
        return my_categories
    

def structuring_file_to_import(my_database,headers):
    add_str=": "
    counter=0
    my_database_values=[]
    my_categories=[]
    #try:
    if my_database!=[]:
        while counter<=len(my_database)-1:
                
            for item in range(0,len(headers)):
                start=my_database[counter].find(f'{headers[item]}{add_str}')
                if item!=len(headers)-1:
                    end=my_database[counter].find(",",start)
                    my_database_values.append(my_database[counter][start+len(f'{headers[item]}{add_str}'):end])
                else:
                    my_database_values.append(my_database[counter][start+len(f'{headers[item]}{add_str}'):])
            
            my_categories.append(my_database_values)
            my_database_values=[]
            counter+=1
        return my_categories
