from main import *

def test_winning_match():
    """
    Given similar secret code and a guess, 
    When calling the function combinations_comparison
    Then returns 4 corrects positions
    """
    code_length = 4
    secret = ["B", "R", "P", "Y"]
    guess = ["B", "r", "p", "Y"]
    #correct_position, wrong_position = combinations_comparison(code_length, secret, guess)
    assert(combinations_comparison(code_length, secret, guess)) == code_length, 0
    #assert(wrong_position) == 0

def test_no_correct_position():
    """
    Given different secret code and a guess
    When calling the function combinations_comparison
    Then returns 0 correct positions
    """
    code_length = 4
    secret = ["B", "R", "P", "Y"]
    guess = ["g", "o", "v", "w"]
    correct_position, wrong_position = combinations_comparison(code_length, secret, guess)
    assert(correct_position) == 0
    assert(wrong_position) == 0

def test_all_colors_():
    """
    Given secret same colors
    When calling the function
    Then returns 2 correct positions
    """
    code_length = 4
    secret = ["B", "B", "B", "B"]
    guess = ["B", "B", "P", "P"]
    correct_position, _ = combinations_comparison(code_length, secret, guess)
    assert(correct_position) == 2

def test_4():
    """
    Given
    When
    Then
    """
    code_length = 4
    secret = ["B", "B", "B", "O"]
    guess = ["B", "B", "O", "B"]
    correct_position, wrong_position = combinations_comparison(code_length, secret, guess)
    assert(correct_position) == 2
    assert(wrong_position) == 2

def test_5():
    """
    Given
    When
    Then
    """
    code_length = 4
    secret = ["B", "B", "B", "O"]
    guess = ["B", "B", "B", "P"]
    correct_position, _ = combinations_comparison(code_length, secret, guess)
    assert(correct_position) == 3

def test_6():
    """
    Given 
    When 
    Then 
    """
    code_length = 4
    secret = ["B", "B", "O", "O"]
    guess = ["B", "O", "B", "O"]
    correct_position, wrong_position = combinations_comparison(code_length, secret, guess)
    assert(correct_position) == 2
    assert(wrong_position) == 2

def test_7():
    """
    Given 
    When 
    Then 
    """
    code_length = 4
    secret = ["B", "R", "Y", "P"]
    guess = ["p", "y", "r", "b"]
    _, wrong_position = combinations_comparison(code_length, secret, guess)
    assert(wrong_position) == 4

def test_8():
    """
    Given 
    When 
    Then 
    """
    code_length = 4
    secret = ["B", "R", "Y", "P"]
    guess = ["o", "b", "o", "o"]
    correct_position, wrong_position = combinations_comparison(code_length, secret, guess)
    assert(correct_position) == 0
    assert(wrong_position) == 1

# if __name__ == '__main__':
#     test_winning_match()
#     test_no_correct_position()
#     test_all_colors_()
#     test_4()
#     test_5()
#     test_6()
#     test_7()
#     test_8()
#     print("Everything passed")