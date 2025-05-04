from exercise4 import reversed_string

def test_my_reversedstring_with_a_phrase():
    #Act
    my_test_string="Existence or non-existence, that is the dilemma"
    #Arrange
    my_reversed_test_string=reversed_string(my_test_string)
    my_result="ammelid eht si taht ,ecnetsixe-non ro ecnetsixE"
    #Assert
    assert my_reversed_test_string==my_result


def test_my_reversedstring_with_a_single_upper_letter():
    #Act
    my_test_string="X"
    #Arrange
    my_reversed_test_string=reversed_string(my_test_string)
    my_result="X"
    #Assert
    assert my_reversed_test_string==my_result


def test_my_reversedstring_with_no_spaces_phrase():
    #Act
    my_test_string="Existenceornon-existence,thatisthedilemma"
    #Arrange
    my_reversed_test_string=reversed_string(my_test_string)
    my_result="ammelidehtsitaht,ecnetsixe-nonroecnetsixE"
    #Assert
    assert my_reversed_test_string==my_result


