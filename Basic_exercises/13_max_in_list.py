"""
The function max() from exercise 1) and the function max_of_three() from exercise 2) 
will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? 
Write a
function max_in_list() that takes a list of numbers and returns the largest one.
"""


def max_in_list(given_list):
    result = 0
    for number in given_list:
        if number > result:
            result = number
    return result


def main():
    cubes = [i**3 for i in range(5)]
    print("\"{}\" is the highest of the given list.".format(max_in_list(cubes)))


if __name__ == '__main__':
    main()
