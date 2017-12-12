"""
Using the higher order function reduce(),
write a function max_in_list() that takes a list of numbers and returns the largest one.
Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?
"""
import functools


def max_in_list(given_list):
    print(given_list)
    result = 0
    for number in given_list:
        if number > result:
            result = number
    return result


def main():
    cubes = [i**3 for i in range(5)]
    print("\"{}\" is the highest of the given list.".format(max_in_list(cubes)))

    maxi_lambda_magic = lambda a, b: a if (a > b) else b
    print(functools.reduce(maxi_lambda_magic, cubes))


if __name__ == '__main__':
    main()
