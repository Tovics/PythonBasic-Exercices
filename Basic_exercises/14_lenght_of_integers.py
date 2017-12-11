"""
Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.
"""


"""
def lenght_of(thing):
    lenght = []
    for item in range(len(thing)):
        lenght.append(len(thing[item]))
    return lenght

print(lenght_of(check))
"""


def main():
    user_input = input("Type here the sentence you want to know the lenght of it's words: ")
    sentence = str(user_input)
    countable_sentence = sentence.split()
    lenght = []
    for item in range(len(countable_sentence)):
        lenght.append(len(countable_sentence[item]))
    print("The lenghts of the words in the given sentence is: {}".format(lenght))


if __name__ == '__main__':
    main()
