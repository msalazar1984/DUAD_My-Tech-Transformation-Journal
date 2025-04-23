def decorator_with_arguments(function):
    def wrapper(arg1, arg2):
        print(f'My Arguments are: {arg1}, {arg2}')
        my_function=function(arg1,arg2)
        print(my_function)
    return wrapper


@decorator_with_arguments
def countries(country_one, country_two):
    my_string_result=f'Countries I like the most are: {country_one} y {country_two}'
    return(my_string_result)


def main():
    str_countryone="Costa Rica"
    str_countrytwo="Spain"
    countries(str_countryone, str_countrytwo)


main()