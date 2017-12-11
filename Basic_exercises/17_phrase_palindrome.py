"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!".
Note that punctuation, capitalization, and spacing are usually ignored.
"""


def check_palindrome(phrase):
    phrase = phrase.lower()
    clean_phrase = ""
    for character in phrase:
        if character not in " ',?!.":
            clean_phrase += character
    if clean_phrase == clean_phrase[::-1]:
        return True
    else:
        return False


def main():
    false_check = "This is defenetly not a palindrome phrase"
    check1 = "Go hang a salami I'm a lasagna hog."
    check2 = "Was it a rat I saw?"
    check3 = "Step on no pets"
    check4 = "Sit on a potato pan, Otis"
    check5 = "Lisa Bonet ate no basil"
    check5 = "Satan, oscillate my metallic sonatas"
    check6 = "I roamed under it as a tired nude Maori"
    check7 = "Rise to vote sir"
    check8 = "Dammit, I'm mad!"
    print(check_palindrome(false_check))
    print(check_palindrome(check1))
    print(check_palindrome(check2))
    print(check_palindrome(check2))
    print(check_palindrome(check4))
    print(check_palindrome(check5))
    print(check_palindrome(check6))
    print(check_palindrome(check7))
    print(check_palindrome(check8))


if __name__ == '__main__':
    main()
