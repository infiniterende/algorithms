def even_odd(arr):
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] % 2 == 0:
            i += 1
        elif arr[i] % 2 == 1 and arr[j] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
        elif arr[i] % 2 == 1 and arr[j] % 2 == 1:
            j -= 1

    return arr


# test cases - first number starts with even
# first number starts with odd
# lsat number is even
# last number is odd
# [2, 1, 4, 2, 3]
# [1, 3, 2, 4, 5]
# [2,4, 1, 6]

# time complexity = O(n), space - O(1)

print(even_odd([2, 1, 4, 2, 3]))
print(even_odd([1, 3, 2, 4, 5]))
print(even_odd([2, 4, 1, 6]))
