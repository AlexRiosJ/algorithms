import array_utils

def quick_sort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    temp = 0
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array_utils.swap(array, i, j)
    array_utils.swap(array, i + 1, high)
    return i + 1

array = array_utils.random_array(50, 100)
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)