def merge(arr1, arr2):
    arr = []
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    while i < n1:
        arr.append(arr1[i])
        i += 1
    while j < n2:
        arr.append(arr2[j])
        j += 1
    return arr


def merge_sort(arr):

    end = len(arr)
    if end <= 1:
        return arr
    mid = end // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    arr = merge(left, right)
    return arr


def verify(arr):
    result = True
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            result = False
            break
        i += 1
    return result


l1 = [i for i in range(15, 0, -1)]
l2 = merge_sort(l1)
print(verify(l1))
print(l1)
print(verify(l2))
print(l2)
