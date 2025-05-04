def prime_number_detector(list_of_numbers):
    counter=0
    prime_counter=0
    counting_deleted=0
    q_elements=len(list_of_numbers)
    while counter<=q_elements-1:
        my_number=list_of_numbers[counter]
        prime_counter=0
        for number in range(1,my_number+1):
            if(my_number%number==0):
                prime_counter+=1
        if prime_counter>2:    
            list_of_numbers.pop(counter)
            counting_deleted+=1
            counter=counter+1-counting_deleted
        else:
            counter+=1
        q_elements=len(list_of_numbers)
    return list_of_numbers