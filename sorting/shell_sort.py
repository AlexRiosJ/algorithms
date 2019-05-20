import array_utils

def shell_sort(array):
    delta = 1
    pivot = 0
    i = 0
    while(delta <= len(array) / 3):
        delta = delta * 3 + 1
    while(delta > 0):
        p = delta
        for p in range(len(array)):
            pivot = array[p]
            i = p - delta
            while(i >= 0 and array[i] > pivot):
                array[i + delta] = array[i]
                i = i - delta
            array[i + delta] = pivot
        delta = int((delta - 1) / 3)

array = array_utils.random_array(50, 100)
print(array)
shell_sort(array)
print(array)