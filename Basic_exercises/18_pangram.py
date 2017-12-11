"""
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. 
Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""


def is_pangram(some_string):
    some_string = some_string.lower()
    concentrate = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0

    for each in some_string:
        if each not in " ',?!.":
            concentrate += each

    for letter in alphabet:
        if letter in some_string:
            count += 1

    if count == 26:
        return True
    else:
        return False


def main():
    check = "The quick brown fox jumps over the lazy dog."
    false_check = "This is not a pangram"
    print(is_pangram(check))
    print(is_pangram(false_check))


if __name__ == '__main__':
    main()
