def reverse(list):
    if not list:
        return list
    else:
        return reverse(list[1:] + list[:1])

def ireverse(list):
    res = list[:0]
    for i in range(len(list)):
        res = list[i:i+1] + res
    return res
