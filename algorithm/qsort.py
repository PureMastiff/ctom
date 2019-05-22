# coding=utf-8

seq = [12, 23, 1, 23, 34, 4]
def qsort(seq):
    if seq == []:
        return []
    else:
        pivot = seq[0]
        less = qsort([x for x in seq[1:] if x < pivot])
        greater = qsort([x for x in seq[1:] if x >= pivot])
    return less + [pivot] + greater


if __name__ == '__main__':
    print(qsort(seq))