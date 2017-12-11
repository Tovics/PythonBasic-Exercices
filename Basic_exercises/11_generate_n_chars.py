"""
Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long,
consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". 
(Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". 
For the sake of the exercise you should ignore that the problem can be solved in this manner.)
"""

"""
def generate_chars_cheat(n, c):
    return n * c

# print(generate_chars_cheat(6, "x"))
"""


def generate_chars(n, c):
    result = ""
    for i in range(n):
        result = result + c
    return result


def main():
    user_input1 = input("How long your string should be: ")
    user_input2 = input("What character you want to see: ")
    number = int(user_input1)
    character = str(user_input2)
    print("Here's your string dude: {}".format(generate_chars(number, character)))


if __name__ == '__main__':
    main()
