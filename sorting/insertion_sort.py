import array_utils

def insertion_sort(array):
    pivot = 0
    i = 0
    p = 1
    for p in range(len(array)):
        pivot = array[p]
        i = p - 1
        while(i >= 0 and array[i] > pivot):
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = pivot

array = array_utils.random_array(50, 100)
print(array)
insertion_sort(array)
print(array)