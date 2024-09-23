def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [num for num in arr[1:] if num < pivot]
    greater = [num for num in arr[1:] if num > pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater)
