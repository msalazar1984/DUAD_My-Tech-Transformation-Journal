def my_bubble_sort(my_list):
        if not isinstance(my_list,list):
            raise TypeError
        for index1 in range(0,len(my_list)-1):
            changes=False
            for index2 in range(0,len(my_list)-1-index1):
                current_element=my_list[index2]
                next_element=my_list[index2+1]

                print(f'Im in the iteration{index1}, current element is equal to: {current_element} and next element is equal to: {next_element}')

                if current_element>next_element:
                    my_list[index2]=next_element
                    my_list[index2+1]=current_element
                    changes=True
            if not changes:
                return