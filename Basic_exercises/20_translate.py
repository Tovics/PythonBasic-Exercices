"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
"""


def translate(english_words):
    swedish = []
    english_swedish = {"merry": "god",
                       "christmas": "jul",
                       "and": "och",
                       "happy": "gott",
                       "new": "nytt",
                       "year": "år"}
    for word in english_words:
        if word in english_swedish:
            swedish.append(english_swedish[word])
    return swedish


def main():
    sentence = ["Merry", "christmas", "and", "happy", "new", "year"]
    swedish_sentence = translate(sentence)
    printable = " ".join(swedish_sentence)
    print(printable)


if __name__ == '__main__':
    main()
