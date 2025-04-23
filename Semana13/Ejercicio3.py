from datetime import datetime


class User():
    def __init__(self,day_birth,month_birth,year_birth):
        
        self.date_of_birth=datetime(year_birth,month_birth,day_birth)
        self.today_date=datetime.today()
    

    @property
    def my_age(self):
        self.age=(self.today_date.year-self.date_of_birth.year)
        if self.today_date.month<self.date_of_birth.month or (self.today_date.month==self.date_of_birth.month and self.today_date.day<self.date_of_birth.day):
            self.age-=1
        return self.age


def decorator_with_arguments(function):
    def wrapper(my_user):
        try:
            if my_user.my_age<18:
                raise err
            else:
                my_result=(function(my_user))
                print(my_result)
        except Exception as err:
            print(f'User is {my_user.my_age} years old is under age and cannot proceed')

    return wrapper

@decorator_with_arguments
def processed_age(user):
    my_result=f'User is {user.my_age} years old and He/She can proceed'
    return (my_result)


def main():
    my_boolean=True
    while my_boolean==True:
        try:
            int_operation_menu=int(input("Please type an option 1. Type date of birth(Day-Month-Year), 2. Validate input, 3.Exit program"))
            if int_operation_menu==1:
                try:
                    int_dayofbirth=int(input("Please enter day of birth (Only values between 1 and 31 are allowed): "))
                    int_monthofbirth=int(input("Please enter month of birth (only values between 1 and 12 are allowed): "))
                    int_yearofbirth=int(input("Please enter year of birth: (values cannot be greater than today's date): "))
                    
                    if int_dayofbirth<1 or int_dayofbirth>31:
                        raise err_day
                    if int_monthofbirth<1 or int_monthofbirth>12:
                        raise err_month
                    if datetime(int_yearofbirth,int_monthofbirth,int_dayofbirth)>datetime.today():
                        raise err_year
                    
                except ValueError:
                    print("Days, months or years only can be numbers, any other character is not allowed")
                except Exception as err_day:
                    print("Day of birth only can be values between 1 and 31")
                except Exception as err_month:
                    print("Month of birth only can be values between 1 and 12")
                except Exception as err_year:
                    print("Year of birth is incorrect, date of birth cannot be greater than today's date")
        
            if int_operation_menu==2:
                #print(f'{int_dayofbirth}{int_monthofbirth}{int_yearofbirth}')
                try:
                    my_user=User(int_dayofbirth,int_monthofbirth,int_yearofbirth)
                    processed_age(my_user)
                except ValueError:
                    print("Date of birth cannot be proceed there is an error in typed values, please enter a new date of birth")
            elif int_operation_menu==3:
                my_boolean=False
            if int_operation_menu<1 or int_operation_menu>3:
                raise err_menu
        except ValueError:
            print(f'Menu only read numbers, letters are invalid characters')
        except Exception as err_menu:
            print(f'Please type an option between 1 and 3')


main()