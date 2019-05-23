# coding=utf-8


seq = [12, 23, 1, 23, 34, 4]

# https://www.cnblogs.com/cookie1026/p/6115925.html
def insert_sort(seq):
    length = len(seq)

    for i in range(1,length):
        k = seq[i]
        j = i - 1
        while j >= 0:
            if seq[j] > k:
                seq[j+1] = seq[j]
                seq[j] = k
            j = j - 1
    return seq


if __name__ == '__main__':
    print(insert_sort(seq))