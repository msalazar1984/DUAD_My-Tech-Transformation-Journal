def counting_upper_lower_cases(my_string):
    counter_upper=0
    counter_lower=0
    for index in range(0,len(my_string)):
        if(my_string[index].isupper()==True):
            counter_upper+=1
        if(my_string[index].islower()==True):
            counter_lower+=1
    result_string=(f'I have {counter_upper} Upper Cases and {counter_lower} Lower Cases')
    return result_string