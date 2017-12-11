"""
Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it.
Represent the frequency listing as a Python dictionary.
Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").
"""


def char_freq(some_string):
    result = {}
    for i in range(len(some_string)):
        if some_string[i] in result:
            result[some_string[i]] = result.get(some_string[i]) + 1
        else:
            result[some_string[i]] = 1
    return result


def main():
    check = "abbabcbdbabdbdbabababcbcbab"
    print(char_freq(check))


if __name__ == '__main__':
    main()