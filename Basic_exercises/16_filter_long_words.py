"""
Write a function filter_long_words() that takes a list of words and an integer n 
and returns the list of words that are longer than n.
"""


def filter_long_words(list_of_words, lenght):
        longer = []
        for each in range(len(list_of_words)):
            if len(list_of_words[each]) > lenght:
                longer.append(list_of_words[each])
        return longer


def main():
        check = ["Dis", "string", "is", "as", "long", "as", "it's", "wrong"]
        print(filter_long_words(check, 4))


if __name__ == '__main__':
        main()
