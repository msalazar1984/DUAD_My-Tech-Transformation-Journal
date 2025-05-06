from exercise6 import split_string

def test_sorting_string_with_only_numbers():
    #Arrange
    my_test_string="12313-5656-34354-3454-2343-34343-343554"
    #Act
    my_result_string=split_string(my_test_string)
    #Assert
    assert my_result_string==" 12313 2343 34343 34354 343554 3454 5656"


def test_sorting_string_with_one_letter_string():
    #Arrange
    my_test_string="f-r-t-a-v-b"
    #Act
    my_result_string=split_string(my_test_string)
    #Assert
    assert my_result_string==" a b f r t v"


def test_sorting_string_with_spaces_string():
    #Arrange
    my_test_string="Hello world-my name-is Python"
    #Act
    my_result_string=split_string(my_test_string)
    #Assert
    assert my_result_string==" Hello world is Python my name"