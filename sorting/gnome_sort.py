import array_utils

def gnome_sort(array):
    i = 0
    while i <= len(array) - 1:
        if i == 0 or array[i - 1] <= array[i]:
            i += 1
        else:
            array_utils.swap(array, i, i - 1)
            i -= 1
            if i == 0:
                i -= 1

array = array_utils.random_array(50, 100)
print(array)
gnome_sort(array)
print(array)