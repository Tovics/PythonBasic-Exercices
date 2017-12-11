"""
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, 
False otherwise.
You may use your is_member() function, or the in operator, but for the sake of the exercise, 
you should (also) write it using two nested for-loops.
"""


def overlapping(list_a, list_b):
    for letter_a in list_a:
        for letter_b in list_b:
            if letter_a == letter_b:
                return True
    return False


def import_form_file(filename="lappfold.txt"):
    imported_lists = []
    with open(filename) as file_content:
        lists = file_content.readlines()
    for i in lists:
        imported_lists.append(i.replace("\n", " ").split(", "))
    return imported_lists


def main():
    list1 = ["a", "b", "c"]
    list2 = ["b", "d", "e"]
    list3 = ["f", "g", "h"]
    print(overlapping(list1, list2))
    print(overlapping(list1, list3))
    print(import_form_file())


if __name__ == '__main__':
    main()
