import random

def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2

# Generate a random array of size 10
arr = [random.randint(1, 100) for i in range(12)]
print("Unsorted array:")
print(arr)

# Sort the array using Shellsort
shellSort(arr)
print("Sorted array:")
print(arr)
