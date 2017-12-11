

something = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"


def high_and_low(numbers):
    highest = 0
    lowest = 10000
    list_of_numbers = numbers.split(" ")
    real_numbers = []
    print (list_of_numbers)
    for i in list_of_numbers:
        real_numbers.append(int(i))
    for low in real_numbers:
        if int(low) < lowest:
            lowest = low
    for high in real_numbers:
        if int(high) > highest:
            highest = high
    result = str(highest) + " " + str(lowest)
    print (result)


high_and_low(something
)
