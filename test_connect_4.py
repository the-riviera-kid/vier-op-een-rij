from connect_4 import connect_4
from connect_4 import get_row

def test_target_in_sequence():
    assert connect_4([], 'red') == False

def test_target_found():
    assert connect_4(['x', 'x', 'x', 'x'], 'x') == True

def test_target_not_found_four_locations():
    assert connect_4(['x', 'y', 'x', 'x'], 'x') == False

def test_target_found_in_seven():
    assert connect_4(['x', 'x', 'y','y','y','y','x'], 'y') == True

def test_target_occurs_five_times():
    assert connect_4([1,1,1,1,1,], 1) == True

def test_target_occurs_four_times_not_consecutively():
    assert connect_4([1,2,1,2,1,2,1], 1) == False

def test_target_appears_zero_times():
    assert connect_4(['a','b'], 'c') == False

def test_target_appears_one_time():
    assert connect_4(['a','b'], 'a') == False

def test_target_appears_four_times_consecutive():
    assert connect_4([1,1,1,1,], '1') == False

def test_get_row_empty_grid():
    assert get_row([], (1, 2)) == None

def test_get_row_one_element_not_in_grid():
    assert get_row([['x']], (2, 1)) == None

def test_get_row_one_element_in_grid():
    assert get_row([['x']], (0, 0)) == ['x']

def test_get_row_two_elements_in_grid():
    assert get_row([['x', 'x']], (1, 0)) == ['x', 'x']
