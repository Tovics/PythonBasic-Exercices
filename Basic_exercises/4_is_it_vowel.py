"""
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
"""


def is_vowel(letter):
    if letter in "aeiou":
        return True
    else:
        return False


def main():
    letter_to_check = str(input("Give me a letter(a string of length 1): "))
    if is_vowel(letter_to_check) is True:
        print("The letter \"{}\" is a vowel.".format(letter_to_check))
    else:
        print("The letter \"{}\" is a consonant.".format(letter_to_check))


if __name__ == '__main__':
    main()
