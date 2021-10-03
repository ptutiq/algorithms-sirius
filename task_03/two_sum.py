# Дан массив целых чисел numbers и целое число X; 
# нужно найти в массиве два элемента, сумма которых равняется X. 
# Гарантируется, что такие элементы в массиве есть.

# 1. Решить задачу применяя наивный алгоритм
# 2. Предлжить второе решение, которое оптимизрует наивны алгоритм 
# с применеием сортировки или вспомогательных структур
def binary_search(numbers, x):
    
    left = -1
    right = len(numbers)
    if x in numbers:
        while right > left +1:
            middle = (left + right) // 2
            if numbers[middle] >= x:
                right = middle 
            else:
                left = middle 
        return right
    else:
        return -1


def two_sum_primary(a,x):
    k = 0 
    for i in range(len(a)-1):
        if a[i] + a[i+1] == x:
                k += 1
                return (a[i],a[i+1],x)
    if k == 0:
        return -1
    


def two_sum_optimized(numbers, sum):
    b = sorted(numbers)
    return binary_search(b,sum)





numbers = [1,2,3,4,78,90,12,33]
sum_1 = int(input())

print('primary', two_sum_primary(numbers, sum_1))
print('optimized', two_sum_primary(numbers, sum_1))
