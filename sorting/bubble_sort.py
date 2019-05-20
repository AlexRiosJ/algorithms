import array_utils

def bubble_sort(array):
    swap = False
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array_utils.swap(array, j, j + 1)
                swap = True    
        if not swap:
            break

array = array_utils.random_array(50, 100)
print(array)
bubble_sort(array)
print(array)