from exercise5 import counting_upper_lower_cases

def test_counter_upper_lower_cases_from_no_upper_cases_string():
    #Arrange
    my_test_string="this is my string to test"
    #Act
    my_result_string=counting_upper_lower_cases(my_test_string)
    #Assert
    assert my_result_string=="I have 0 Upper Cases and 20 Lower Cases"


def test_counter_upper_lower_cases_with_only_numbers_string():
    #Arrange
    my_test_string="1244 234 2454 234 4545 5556"
    #Act
    my_result_string=counting_upper_lower_cases(my_test_string)
    #Assert
    assert my_result_string=="I have 0 Upper Cases and 0 Lower Cases"


def test_counter_upper_lower_cases_with_no_spaces_string():
    #Arrange
    my_test_string="HimynameisMiguelSalazar"
    #Act
    my_result_string=counting_upper_lower_cases(my_test_string)
    #Assert
    assert my_result_string=="I have 3 Upper Cases and 20 Lower Cases"
