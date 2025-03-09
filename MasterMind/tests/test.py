from game.mastermind import *

def test_winning_match():
    """
    Given similar secret code and a guess, 
    When calling the function combinations_comparison
    Then returns 4 corrects positions
    """
    code_length = 4
    secret = ["B", "R", "P", "Y"]
    guess = ["B", "r", "p", "Y"]
    assert(combinations_comparison(code_length, secret, guess)) == code_length, 0

def test_no_correct_position():
    """
    Given different secret code and a guess
    When calling the function combinations_comparison
    Then returns 0 correct positions
    """
    code_length = 4
    secret = ["B", "R", "P", "Y"]
    guess = ["g", "o", "v", "w"]
    assert(combinations_comparison(code_length, secret, guess)) == 0, 0

def test_all_colors_():
    """
    Given secret same colors
    When calling the function
    Then returns 2 correct positions
    """
    code_length = 4
    secret = ["B", "B", "B", "B"]
    guess = ["B", "B", "P", "P"]
    assert(combinations_comparison(code_length, secret, guess)) == 2, 0

def test_4():
    """
    Given
    When
    Then
    """
    code_length = 4
    secret = ["B", "B", "B", "O"]
    guess = ["B", "B", "O", "B"]
    assert(combinations_comparison(code_length, secret, guess)) == 2, 2

def test_5():
    """
    Given
    When
    Then
    """
    code_length = 4
    secret = ["B", "B", "B", "O"]
    guess = ["B", "B", "B", "P"]
    assert(combinations_comparison(code_length, secret, guess)) == 3, 0

def test_6():
    """
    Given 
    When 
    Then 
    """
    code_length = 4
    secret = ["B", "B", "O", "O"]
    guess = ["B", "O", "B", "O"]
    assert(combinations_comparison(code_length, secret, guess)) == 2, 2

def test_7():
    """
    Given 
    When 
    Then 
    """
    code_length = 4
    secret = ["B", "R", "Y", "P"]
    guess = ["p", "y", "r", "b"]
    assert(combinations_comparison(code_length, secret, guess)) == 0, 4

def test_8():
    """
    Given 
    When 
    Then 
    """
    code_length = 4
    secret = ["B", "R", "Y", "P"]
    guess = ["o", "b", "o", "o"]
    assert(combinations_comparison(code_length, secret, guess)) == 0, 1

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