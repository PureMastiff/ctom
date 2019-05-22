

seq = [12, 23, 1, 23, 34, 4]

def bubble_sort(seq):
    length = len(seq)
    for i in range(0, length):
        for j in range(i+1, length):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq

if __name__ == '__main__':
    print(bubble_sort(seq))