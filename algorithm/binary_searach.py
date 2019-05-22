


seq = [12, 23, 1, 23, 34, 4]
seq = sorted(seq)

target = 34

def binary_searach(seq, target):
    end = len(seq)
    if end < 1:
        return False
    mid = (end)//2

    if target == seq[mid]:
        return True
    elif target > seq[mid]:
        return binary_searach(seq[mid+1:], target)
    elif target < seq[mid]:
        return binary_searach(seq[0: mid], target)

print(binary_searach(seq, target))

def binary_chop(alist, data):
    """
    递归解决二分查找
    :param alist:
    :return:
    """
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return binary_chop(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop(alist[mid+1:], data)
    else:
        return True

# def binary_chop(alist, data):
#     """
#     非递归解决二分查找
#     :param alist:
#     :return:
#     """
#     n = len(alist)
#     first = 0
#     last = n - 1
#     while first <= last:
#         mid = (last + first) // 2
#         if alist[mid] > data:
#             last = mid - 1
#         elif alist[mid] < data:
#             first = mid + 1
#         else:
#             return True
#     return False
#
# if __name__ == '__main__':
#     lis = [2,4, 5, 12, 14, 23]
#     if binary_chop(lis, 23):
#         print('ok')