"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all 
the numbers in a list of numbers. 
For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""


def summing(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        result += i
    return result


def multiply(list_of_numbers):
    result = 1
    for i in list_of_numbers:
        result *= i
    return result


def main():
    example = [1, 2, 3, 4]
    print("The result of summing the given list is: {}".format(summing(example)))   # the result must be 10
    print("The result of multiplying the given list is: {}".format(multiply(example)))  # the result must be 24


if __name__ == '__main__':
    main()


"""
#Try this, if the list contains 0:

cubes = [i**3 for i in range(5)]


def multiply(list_of_numbers):
    result = 1
    for i in list_of_numbers:
        if i == 0:
            result = result * (i + 1)
        else:
            result *= i
    return result
"""
