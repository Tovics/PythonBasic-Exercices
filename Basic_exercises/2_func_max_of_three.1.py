"""
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""


def max_of_three(number1, number2, number3):
    if (number1 > number2) and (number1 > number3):
        return number1
    elif (number2 > number1) and (number2 > number3):
        return number2
    elif (number3 > number1) and (number3 > number2):
        return number3


def main():
    user_input1 = input("Give me a number: ")
    user_input2 = input("Give me another number: ")
    user_input3 = input("Give me the last one: ")
    num1 = float(user_input1)
    num2 = float(user_input2)
    num3 = float(user_input3)
    biggest = max_of_three(num1, num2, num3)
    print("And the winner is: {}".format(biggest))


if __name__ == '__main__':
    main()
