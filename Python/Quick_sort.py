
def partition(arr, start, end):
    """
    Input : array , lower index,upper index
    Output : it returns index of Partition element

    it fixed the position of pivot element, all the left element of pivot
    are smaller and right elements are grater then pivot element
    """
    mid = (start + end)//2
    pivot = arr[mid]
    i = start
    j = end
    arr[start], arr[mid] = arr[mid], arr[start]
    while i < j:
        while arr[i] <= pivot and i < end:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[start] = arr[start], arr[j]
    return j


def quick_sort(arr, start, end):
    """
    it sorts the given array ascending order recursively.

    param
        arr: array of elements.
        start: starting index of array.
        end: last index of array.
    return: None.
    """
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)


def varify(arr):
    """
    it varify given array is sorted or not,if array is sort it returns True,
    otherwise it returns False.

    param
        arr: array of elements
        return: True/False
    """
    n = len(arr)
    i = 0
    result = True
    while i < n-1:
        if arr[i] > arr[i+1]:
            result = False
        i += 1
    return result


if __name__ == '__main__':
    arr = []
    n = int(input('Enter array size :'))
    for i in range(n):
        arr.append(int(input('Enter element :')))
    print('Before sort :', arr)
    quick_sort(arr, 0, n-1)

    print('After sort :', arr)
    print('Verify Sort :', varify(arr))
