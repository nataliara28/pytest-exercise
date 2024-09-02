# Exercise 1 - Count the occurence of a letter in a word

def char_counter(word, char):
    """
    The function returns the number of 'char'
    occurence in 'word' or 0 if there's no
    occurence.
    """
    try:
        total = 0
        for w in word:
            if w == char:
                total += 1
    except TypeError:
        total = None

    return total


# Exercise 2 - Check if email has @ symbol
def has_at_symbol(email):
    """
    The function takes an email address
    and checks if it contains the "@" symbol.
    """
    try:
        for char in email:
            if char == '@':
                return True
        else:
            return False
    except TypeError:
        return False


# Exercise 3 - Check if a list contains two consecutive even numbers
def is_consecutive_even(numbers):
    """
    Takes a list of numbers and
    return True if two consecutive
    numbers are even else return False in
    all other cases
    """
    try:
        is_even = False
        for num in numbers:
            if num % 2 == 0:
                if is_even == True:
                    break
                else:
                    is_even = True
            else:
                is_even = False
        if is_even:
            return True
        else:
            return False
    except TypeError:
        return True