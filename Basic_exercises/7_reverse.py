"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I"
"""


def reverse(stringy_string):
    return stringy_string[::-1]


def main():
    user_input = input("Type in that you want to reverse: ")
    print("Here you are: {} ".format(reverse(user_input)))


if __name__ == '__main__':
    main()
