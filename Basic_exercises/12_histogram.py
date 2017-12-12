"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""


def histogram(list_of_integers):
    for i in list_of_integers:
        print("*" * i)


def main():
    example = [4, 9, 7]
    histogram(example)


if __name__ == '__main__':
    main()
