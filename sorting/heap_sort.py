import array_utils

def heap_sort(array):
    build_max_heap(array)
    heap_size = len(array)
    while(heap_size > 1):
        array_utils.swap(array, 0, heap_size - 1)
        max_heapify(array, 0, heap_size - 2)
        heap_size -= 1

def build_max_heap(array):
    root = int((len(array) / 2)) - 1
    while(root >= 0):
        max_heapify(array, root, len(array) - 1)
        root -= 1

def max_heapify(array, root, heap_size):
    left = 2 * root + 1
    right = left + 1
    maximum = root
    if left <= heap_size and array[left] > array[maximum]:
        maximum = left
    if right <= heap_size and array[right] > array[maximum]:
        maximum = right
    if maximum != root:
        array_utils.swap(array, maximum, root)
        max_heapify(array, maximum, heap_size)

array = array_utils.random_array(50, 100)
print(array)
heap_sort(array)
print(array)