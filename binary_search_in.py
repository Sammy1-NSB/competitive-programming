def binary_search_desc(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr = [9, 7, 5, 3, 1]
target = 5

print(binary_search_desc(arr, target))