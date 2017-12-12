"""
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). 
That is, double every consonant and place an occurrence of "o" in between. 
For example, translate("this is fun") should return the string "tothohisos isos fofunon"
"""


def translate(sentence):
    rovarspraket = ""
    exceptions = "aeiou ,!?'\"-"
    for character in sentence:
        if character not in exceptions:
            rovarspraket += character
            rovarspraket += "o"
        rovarspraket += character
    return rovarspraket


def main():
    user_input = input("What do you want to translate to rövarspråket: ")
    example = "this is fun"
    print("It looks like something like this: {}".format(translate(user_input)))


if __name__ == '__main__':
    main()
