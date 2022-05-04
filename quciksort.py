import random

def quicksort(i, j, array):
    
    def part_util(i, j, array):
        pivot_index = i
        pivot = array[pivot_index]
        while i < j:
            while i < len(array) and array[i] <= pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if(i < j):
                array[i], array[j] = array[j], array[i]
        array[j], array[pivot_index] = array[pivot_index], array[j]
        return j
    
    if (i < j):
        pivot = part_util(i, j, array)
        quicksort(i, pivot - 1, array)
        quicksort(pivot + 1, j, array)
    return array
    
    
ls = [random.randint(0,100) for i in range(20)]
print(ls)
lss = quicksort(0,len(ls)-1,ls)
print(lss)
