"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""


def find_longest_word(list_of_words):
    longest = 0
    for word in range(len(list_of_words)):
        if longest < len(list_of_words[word]):
            lenght = len(list_of_words[word])
    return lenght


def main():
    user_input = input("Type here the sentence you want to know the lenght of it's longest word: ")
    sentence = str(user_input)
    countable_sentence = sentence.split()
    print("The longest word in the given sentence is {} characters long.".format(find_longest_word(countable_sentence)))


if __name__ == '__main__':
    main()
