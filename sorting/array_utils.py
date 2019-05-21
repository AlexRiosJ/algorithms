from random import *

def random_array(n, r):
    array = []
    for i in range(n):
        array.append(randint(1, r))
    return array

def swap(array, a, b):
    array[a], array[b] = array[b], array[a]