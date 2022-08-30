"""flames game"""

BOY_NAME = 'AJAY'
GIRL_NAME = 'PRIYA'


def convert(string):
    """returns a list from string"""
    list1 = []
    list1[:0] = string
    return list1


list_1 = convert(BOY_NAME)
list_2 = convert(GIRL_NAME)


def modify_list(list_one, list_two):
    """remove same element from two lists"""
    for i in list_1:
        for j in list_2:
            if i == j:
                list_one.remove(i)
                list_two.remove(j)
    return [list_two, list_two]


main_list = list_1 + list_2
COUNT = len(main_list)
result = ["Friends", "Love ", " Affection ", "Marriage", "Enemy", "Siblings"]

while len(result) > 1:
    SPLIT_INDEX = (COUNT % len(result) - 1)
    print(SPLIT_INDEX)
    if SPLIT_INDEX >= 0:

        # list slicing
        right = result[SPLIT_INDEX + 1:]
        left = result[: SPLIT_INDEX]
        print(right, left)

        # list concatenation
        result = right + left
    else:
        result = result[: len(result) - 1]

        # print final result
print("Relationship status :", result[0])
