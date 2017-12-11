def stringy(size):
    empty_list = [i for i in range(size) if i % 1 == 0]
    result = []
    for i in range(len(empty_list)):
        if i % 2 == 0:
            result.append("1")
        elif i % 2 == 1:
            result.append("0")
    output = "".join(result)
    return output


print(stringy(4))
