def quick_sort(left: int, right: int, array: list):
    if left > right: return
    pivot_value = array[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while array[i] < pivot_value: i += 1
        while array[j] > pivot_value: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort(left, j, array)
    quick_sort(i, right, array)
