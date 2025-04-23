
def decorator_with_arguments(function):
    def wrapper(*args,**kargs):
        my_boolean=True
        for item in args:
            try:
                if item.isdigit()!=True:
                    my_boolean=False
                    raise err  
            except Exception as err:
                print(f'No all values are numeric')
                break
        if my_boolean==True:
            my_result=function(*args,**kargs)
            print (my_result)
    return wrapper


@decorator_with_arguments
def processing_result(*args,**kargs):
        str_result=f'Process successfully completed, all values are numbers'
        return str_result


def main():
    my_booleano=True
    my_list=[]
    while my_booleano==True:
        try:
            int_menu=int(input("Please type an option 1. Type an item 2. Process items 3. Exit program"))
            if int_menu==1:
                new_element=input("Type please an item: ")
                my_list.append(new_element)
            elif int_menu==2:
                processing_result(*my_list)
            elif int_menu==3:
                my_booleano=False
            if int_menu<1 or int_menu>3:
                raise err
        except ValueError:
            print("Menu only can read numbers")
        except Exception as err:
            print(f'Please type an option between 1 and 3')

main()

                        