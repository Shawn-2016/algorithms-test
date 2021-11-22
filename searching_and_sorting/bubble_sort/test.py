# O(n^2)
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))


# O(n*n) or O(n)
def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))

arr = [2, 3, 3, 1, 5, 2]
print(bubbleSort(arr))
