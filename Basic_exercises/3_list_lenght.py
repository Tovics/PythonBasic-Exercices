"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def length_of(thing):
    length = 0
    for item in thing:
        length = length + 1
    return length


def main():
    check1 = "Dis string is as long as it's wrong"  # 35
    check2 = ("hedgehog", "cat", "dog", 1234, [1, 2, 3, 4], 4.567)  # 6
    length = length_of(check1)
    print("The length is: {}".format(length))


if __name__ == '__main__':
    main()
