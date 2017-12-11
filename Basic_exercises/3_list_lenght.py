"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def lenght_of(thing):
    lenght = 0
    for item in thing:
        lenght = lenght + 1
    return lenght


def main():
    check1 = "Dis string is as long as it's wrong"  # 35
    check2 = ("hedgehog", "cat", "dog", 1234, [1, 2, 3, 4], 4.567)  # 6
    lenght = lenght_of(check2)
    print("The lenght is: {}".format(lenght))


if __name__ == '__main__':
    main()
