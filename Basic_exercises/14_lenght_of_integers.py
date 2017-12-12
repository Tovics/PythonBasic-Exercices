"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""


"""
def length_of(thing):
    length = []
    for item in range(len(thing)):
        length.append(len(thing[item]))
    return length

print(length_of(check))
"""


def main():
    user_input = input("Type here the sentence you want to know the length of it's words: ")
    sentence = str(user_input)
    countable_sentence = sentence.split()
    length = []
    for item in range(len(countable_sentence)):
        length.append(len(countable_sentence[item]))
    print("The lengths of the words in the given sentence is: {}".format(length))


if __name__ == '__main__':
    main()
