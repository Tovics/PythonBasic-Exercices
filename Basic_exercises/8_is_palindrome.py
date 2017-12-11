"""
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). 
For example, is_palindrome("radar") should return True.
"""


def is_palindrome(check):
    if check == check[::-1]:
        return True
    else:
        return False


def main():
    user_input = input("What word you are wondering about: ")
    if is_palindrome(user_input) is True:
        print("The word \"{}\" is a palindrome.".format(user_input))
    else:
        print("The word \"{}\" is just a boring word, not a palindrome.".format(user_input))


if __name__ == '__main__':
    main()