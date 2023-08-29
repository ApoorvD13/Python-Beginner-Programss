arr = [234, 2124, 3, 647, 5423, 5, 56, 86, 65, 45, 78, 90, 23, 21, 43]


def quicksort(arr, left, right):
    if left < right:
        parpos = partition(arr, left, right)
        quicksort(arr, left, parpos-1)
        quicksort(arr, parpos+1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i

quicksort(arr, 0, len(arr)-1)

print(arr)