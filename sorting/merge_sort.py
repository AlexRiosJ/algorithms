import array_utils

def merge_sort(array, left, right):
    if left < right:
        half = int((left + right) / 2)
        merge_sort(array, left, half)
        merge_sort(array, half + 1, right)
        merge(array, left, half, right)

def merge(array, start, end_left, end_right):
    temp = [0] * ((end_right - start) + 1)
    i = start
    j = end_left + 1
    for k in range(len(temp)):
        if j > end_right:
            temp[k] = array[i]
            i += 1
        elif i > end_left:
            temp[k] = array[j]
            j += 1
        elif i <= end_left and j <= end_right:
            if array[i] <= array[j]:
                temp[k] = array[i]
                i += 1
            else:
                temp[k] = array[j]
                j += 1
    array[start:start + len(temp)] = temp[:]

array = array_utils.random_array(50, 100)
print(array)
merge_sort(array, 0, len(array) - 1)
print(array)
