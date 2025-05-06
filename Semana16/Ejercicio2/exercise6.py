def split_string(my_split_string):
    new_list=my_split_string.split('-')
    new_list.sort()
    result_string=""
    for index in range(0,len(new_list)):
        result_string=f'{result_string} {new_list[index]}'
    return result_string