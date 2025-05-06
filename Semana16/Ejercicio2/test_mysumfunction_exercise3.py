from exercise3 import sum_list_elements

def test_my_list_sum_with_small_list():
    #Arrange
    my_list=[2,4]
    #Act
    my_result=sum_list_elements(my_list)
    #Assert
    assert my_result==6


def test_my_list_sum_large_list():
    #Arrange
    my_list=[682,524,468,625,307,231,416,740,108,256,53,980,153,571,48,61,75,599,678,931,681,91,167,255,634,505,522,201,891,407,952,672,148,544,649,351,85,64,509,959,518,228,329,459,456,527,710,299,143,281,368,954,267,193,982,828,556,109,372,620,768,298,622,226,645,445,426,398,296,900,43,319,497,464,276,642,789,332,573,428,783,127,40,991,540,603,746,287,428,238,744,287,431,196,212,406,836,192,369,773,472,282,337,939,551,968,869,135,703,33,89,449,882,844,670,125,660,180,376,500,593,671,728,378,466,521,186,264,479,583,376,590,391,258,625,740,146,105]
    #Act
    my_result=sum_list_elements(my_list)
    #Assert
    assert my_result==63772


def test_my_list_huge_numbers():
    #Arrange
    my_list=[365768,3456768,23345,343545,3545465,343232,565778,8979988]
    #Act
    my_result=sum_list_elements(my_list)
    #Assert
    assert my_result==17623889
