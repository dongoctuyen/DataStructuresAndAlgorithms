def quick_select(left: int, right: int, k_index: int, array: list[int]):
    if not (left <= k_index <= right): return
    pivot_value = array[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while array[i] < pivot_value: i += 1
        while array[j] > pivot_value: j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_select(left, j, k_index, array)
    quick_select(i, right, k_index, array)
