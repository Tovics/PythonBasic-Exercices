"""
Define a function max() that takes two numbers as arguments and returns the largest of them. 
Use the if-then-else construct available in Python. 
(It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def max_(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


def main():
    user_input1 = input("Give me a number: ")
    user_input2 = input("Give me another number: ")
    num1 = float(user_input1)
    num2 = float(user_input2)
    bigger = max_(num1, num2)
    print("{} is the bigger number".format(bigger))


if __name__ == '__main__':
    main()
