from exercise7 import prime_number_detector


def test_prime_number_detector_with_large_numbers():
    #Arrange
    my_test_numbers_list=[213213,34543543,234234,3432424,23424324,23424343,23243434,6766576]
    #Act
    my_result_list=prime_number_detector(my_test_numbers_list)
    #Assert
    assert my_test_numbers_list==my_result_list


def test_prime_number_detector_with_one_number():
    #Arrange
    my_test_numbers_list=[13]
    #Act
    my_result_list=prime_number_detector(my_test_numbers_list)
    #Assert
    assert my_test_numbers_list==my_result_list


def test_prime_number_detector_with_strings():
    #Arrange
    my_test_numbers_list=["Hello","world","this","is","python","programming"]
    #Act
    my_result_list=prime_number_detector(my_test_numbers_list)
    #Assert
    assert my_test_numbers_list==my_result_list
    