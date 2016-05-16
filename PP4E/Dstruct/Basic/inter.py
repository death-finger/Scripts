def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

def union(seq1, seq2):
    res = list(seq1)
    for x in seq2:
        if not x in res:
            res.append(x)
    return res

