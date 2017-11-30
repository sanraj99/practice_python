

def remove_dupl(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res

print remove_dupl([10, 10, 1, 1, 1, 3, 3, 4, 5, 6, 7, 8, 8, 9])


def remove_duplicates(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
            res.append(x)
            seen.add(x)
    return res

print sorted(remove_duplicates(['a', 'b', 'c', 'd', 'd', 'e', 'd', 'a', 'c']))