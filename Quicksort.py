def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

print("\nSorted array:", quicksort(arr))
