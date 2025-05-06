def reversed_string(my_string):
    new_string=""
    for i in range(len(my_string)-1,-1,-1):
        new_string=f'{new_string}{my_string[i]}'
    return (new_string)