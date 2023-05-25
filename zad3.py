import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def countingsort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Generowanie losowej tablicy liczb całkowitych
array_size = 1000000
random_array = [random.randint(1, 100) for _ in range(array_size)]

# Sortowanie i pomiar czasu dla quicksort
start_time = time.time()
sorted_array_quicksort = quicksort(random_array)
quicksort_time = time.time() - start_time

# Sortowanie i pomiar czasu dla countingsort
start_time = time.time()
sorted_array_countingsort = countingsort(random_array)
countingsort_time = time.time() - start_time

# Sortowanie i pomiar czasu dla heapsort
start_time = time.time()
sorted_array_heapsort = heapsort(random_array)
heapsort_time = time.time() - start_time

# Wyświetlanie czasów sortowania
print("Czas sortowania dla quicksort:", quicksort_time, "s")
print("Czas sortowania dla countingsort:", countingsort_time, "s")
print("Czas sortowania dla heapsort:", heapsort_time, "s")
