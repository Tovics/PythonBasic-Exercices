"""
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, 
and returns True if x is a member of a, False otherwise. 
(Note that this is exactly what the in operator does, 
but for the sake of the exercise you should pretend Python did not have this operator.)
"""


"""
def is_member_cheat(x, a):
    if x in a:
        return True
    else:
        return False
"""


def is_member(x, a):
    check = 0
    for i in a:
        if i == x:
            check += 1
    if check > 0:
        return check
    else:
        return False


def main():
    user_input = input("Give me a letter or a number: ")
    number_checklist = list(range(1, 11))
    letter_checklist = "abcdefghijklemnopqrstvwxyz"
    if is_member(user_input, letter_checklist) > 0:
        print("\"{}\" is in the list.".format(user_input))
    else:
        print("\"{}\" is NOT in the list.".format(user_input))

    print(is_member(user_input, letter_checklist))


if __name__ == '__main__':
    main()
