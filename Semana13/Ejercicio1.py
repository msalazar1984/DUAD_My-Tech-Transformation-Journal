def decorator_with_arguments(function):
    def wrapper(arg1, arg2):
        print(f'Mis Argumentos son: {arg1}, {arg2}')
        print(function(arg1, arg2))
    return wrapper


@decorator_with_arguments
def countries(country_one, country_two):
    return(f'Los paises que mas me gustan son {country_one} y {country_two}')


def main():
    str_countryone="Costa Rica"
    str_countrytwo="España"
    countries(str_countryone, str_countrytwo)


main()