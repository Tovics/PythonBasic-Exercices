"""
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
A simple set of heuristic rules can be given as follows:
If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing For words consisting of consonant-vowel-consonant,
double the final letter before adding ing By default just add ing.
Your task in this exercise is to define a function make_ing_form()
which given a verb in infinitive form returns its present participle form.
Test your function with words such as lie, see, move and hug. However,
you must not expect such simple rules to work for all cases.
"""


def make_ing_form(some_word):
    exeptions = ("be", "see", "flee")
    if some_word not in exeptions:
        if some_word.endswith("e"):
            some_word = some_word[:-1]
            result = some_word + "ing"
        else:
            result = some_word + "ing"
        return result
    elif some_word.endswith("ie"):
        some_word = some_word.rstrip("ie")
        result = some_word + "y" + "ing"

    elif some_word[-2] in "aiou":
        result = some_word + some_word[-1] + "ing"

    return result


def main():
    check = input(str("Give me some word to make it present participle: "))
    print(make_ing_form(check))


if __name__ == "__main__":
    main()