
name_1 = 'AJAY'
name_2 = 'PRIYA'


def convert(string):
    list1 = []
    list1[:0] = string
    return list1


list_1 = convert(name_1)
list_2 = convert(name_2)

for i in list_1:
    for j in list_2:
        if i == j:
            list_1.remove(i)
            list_2.remove(j)

c = list_1 + list_2
count = len(c)
result = ["Friends", "Love ", " Affection ", "Marriage", "Enemy", "Siblings"]

while len(result) > 1:
    split_index = (count % len(result) - 1)
    print(split_index)
    if split_index >= 0:

        # list slicing
        right = result[split_index + 1:]
        left = result[: split_index]
        print(right, left)

        # list concatenation
        result = right + left
    else:
        result = result[: len(result) - 1]

        # print final result
print("Relationship status :", result[0])
