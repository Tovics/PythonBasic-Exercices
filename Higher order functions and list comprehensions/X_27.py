"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(),
and 3) using list comprehensions.
"""


def length_of(thing):
    countable_thing = thing.split()
    length = []
    for item in range(len(countable_thing)):
        length.append(len(countable_thing[item]))
    return length


def main():
    user_input = input("Type here the sentence you want to know the length of it's words: ")
    sentence = str(user_input)
    print(length_of(sentence))


if __name__ == '__main__':
    main()