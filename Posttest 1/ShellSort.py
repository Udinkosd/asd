import random

def shell_sort(array):
    n = len(array)
    interval = n // 2
    while interval > 0: 
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval  
                array[j] = temp
        interval //= 2 
    return array

def data_acak(): 
    array = [random.randint(1, 100) for _ in range(12)] 
    return array

data_awal = data_acak()

print('Data (Array) sebelum shellsort:')
print(data_awal)
print()
data_urut = shell_sort(data_awal)

print('Data (Array) setelah shellsort:')
print(data_urut)

print()
print('Array sebelum shellsort: [80, 19, 10, 62, 31, 70, 51, 29, 5, 45, 93, 12]')
print('Array menjadi sub-set: [80, 19, 10, 62, 31, 70] dan [51, 29, 5, 45, 93, 12]')
print('Interval k = 6 adalah [51, 19, 5, 45, 31, 12, 80, 29, 10, 62, 93, 70]')
print('Interval k = 3 adalah [45, 19, 5, 51, 29, 10, 62, 31, 12, 80, 93, 70]')
print('Interval k = 1 adalah [5, 10, 12, 19, 29, 31, 45, 51, 62, 70, 80, 93]')
print('Array setelah shellsort: [5, 10, 12, 19, 29, 31, 45, 51, 62, 70, 80, 93]')
