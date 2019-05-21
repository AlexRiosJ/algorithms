import array_utils

def selection_sort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array_utils.swap(array, i, j)

array = array_utils.random_array(50, 100)
print(array)
selection_sort(array)
print(array)