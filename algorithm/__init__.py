
seq = [1, 34, 2, 12, 4, 33]

def qsort(seq):
    if seq == []:
        return []
    else:
        pivot = seq[0]
        less = qsort([x for x in seq[1:] if x < pivot])
        greater = qsort([x for x in seq[1:] if x > pivot])

    return less + [pivot] + greater

print(qsort(seq))

print(seq)
def insert_sort(seq):
    length = len(seq)
    for i in range(1,length):
        k = seq[i]
        j = i - 1
        while j >= 0:
            if seq[j] > k:
                seq[j+1] = seq[j]
                seq[j] = k
            j =j - 1
    return seq

print(insert_sort(seq))


def bubble_sort(seq):
    length = len(seq)

    for i in range(0, length):
        for j in range(i+1, length):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]

    return seq

print('ddd')
print(bubble_sort(seq))


seqs = bubble_sort(seq)
target = 33

def binary_searach(seq, target):
    length = len(seq)
    print('seq:{}'.format(seq))
    if length<1:
        return False
    mid = length//2
    if seq[mid] == target:
        return True
    elif seq[mid] > target:
        return binary_searach(seq[0:mid], target)
    elif seq[mid] < target:
        return binary_searach(seq[mid+1:], target)

print(binary_searach(seqs, target))

