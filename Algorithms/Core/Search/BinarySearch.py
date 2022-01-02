# Time Complexity: O(logN)
# Space Complexity: O(1)

def binarySearch(array: list[int], target: int) -> int:
    left, right = 0, len(array) - 1
    while left <= right:
        pivot = (left + right) // 2
        if target == array[pivot]:
            return pivot
        if target > array[pivot]:
            left = pivot + 1
        if target < array[pivot]:
            right = pivot - 1
    return -1


if __name__ == '__main__':
    array = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binarySearch(array, target=target))
