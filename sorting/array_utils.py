from random import *

def random_array(n, r):
    array = []
    for i in range(n):
        array.append(randint(1, r))
    return array

def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp