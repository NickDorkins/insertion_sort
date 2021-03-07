from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort


def test_version():
    assert __version__ == '0.1.0'

def test_can_sort_unsorted_list():
    expected = [1,2,3,4,5,6,7,8,9,10]
    actual = insertion_sort([3,4,9,8,7,6,2,10,1,5])
    assert actual == expected

def test_can_sort_unsorted_list_with_negative_values():
    expected = [-6,-4,-1,2,3,5,7,8,9,10]
    actual = insertion_sort([3,-4,9,8,7,-6,2,10,-1,5])
    assert actual == expected

# def test_error_handling_for_non_int_list():
#     expected = "Error"
#     actual = insertion_sort(['a','b','c','d','e','f','g','h','i','j'])
#     assert actual == expected