def reverse(list):
    if list == []:
        return []
    else:
        return reverse(list[1:] + list[:1])

def ireverse(list):
    res = []
    for x in list: res = [x] + res
    return res
