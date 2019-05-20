import array_utils

def counting_sort(array, k):
    freq = [0] * k
    for i in range(len(array)):
        freq[array[i] - 1] += 1

    temp = 0
    for i in range(k):
        for j in range(freq[i]):
            array[temp] = i + 1
            temp += 1

array = array_utils.random_array(50, 100)
print(array)
counting_sort(array, 100)
print(array)