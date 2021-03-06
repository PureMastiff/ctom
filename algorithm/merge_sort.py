# coding=utf-8

seq = [12, 23, 1, 23, 34, 4]

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(seq):

    if len(seq) <= 1:
        return seq
    middle = len(seq) / 2
    left = merge_sort(seq[:middle])
    right = merge_sort(seq[middle:])

    return merge(left, right)


if __name__ == '__main__':
    print (merge_sort(seq))