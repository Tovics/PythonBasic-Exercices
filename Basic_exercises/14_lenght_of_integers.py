"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
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

    # The little loop below is there because the exercice ask for a program, not for a function.
    """
    countable_sentence = sentence.split()
    length = []
    for item in range(len(countable_sentence)):
        length.append(len(countable_sentence[item]))
    """
    # print("The lengths of the words in the given sentence is: {}".format(length))
    print(length_of(sentence))


if __name__ == '__main__':
    main()
