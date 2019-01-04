test = [1, 2, [3, [1, [43, 44, 45], 2, [56, [101, 102, 103], 57, 58], 3], 4], [2]]


def flatten(lst):
    flat = []

    if len(lst) == 0:
        return flat

    def add(elem):
        if type(elem) == list and len(lst) > 0:
            for x in elem:
                add(x)
        else:
            flat.append(elem)

    add(lst)

    return flat


print(flatten(test))
