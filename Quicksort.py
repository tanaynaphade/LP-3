import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort_det(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_det(arr, low, pi-1)
        quicksort_det(arr, pi+1, high)

def quicksort_rand(arr, low, high):
    if low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]   # Random pivot
        pi = partition(arr, low, high)
        quicksort_rand(arr, low, pi-1)
        quicksort_rand(arr, pi+1, high)

# ---- Main ----
n = int(input("Enter number of elements: "))
arr1 = list(map(int, input("Enter elements: ").split()))
arr2 = arr1.copy()

quicksort_det(arr1, 0, n-1)
quicksort_rand(arr2, 0, n-1)

print("\nDeterministic QuickSort:", arr1)
print("Randomized QuickSort:", arr2)
