import matplotlib.pyplot as plt
import timeit
import bisect
import random
import numpy as np

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    index = bisect.bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return index
    return -1

input_sizes = [1000 * 2**i for i in range(8)]  # 1000 - 128000
linear_times = []
binary_times = []

for size in input_sizes:
    arr = list(range(size))
    target = random.randint(0, size - 1)
    iter_count = 1000

    lin_time = timeit.timeit(lambda: linear_search(arr, target), number=iter_count)
    bin_time = timeit.timeit(lambda: binary_search(arr, target), number=iter_count)

    linear_times.append(lin_time)
    binary_times.append(bin_time)

#Theoretical curves
input_sizes_np = np.array(input_sizes)
log_n = np.log2(input_sizes_np)

# Scale factors
scale_linear = linear_times[-1] / input_sizes_np[-1]  # last linear time per element
scale_log = binary_times[-1] / log_n[-1]             # last binary time per log n

# Theoretical time curves
theoretical_linear = scale_linear * input_sizes_np
theoretical_log = scale_log * log_n

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, linear_times, 'o-', label='Measured Linear Search', color='red')
plt.plot(input_sizes, binary_times, 'x-', label='Measured Binary Search', color='blue')
plt.plot(input_sizes, theoretical_linear, '--', label='Theoretical O(n)', color='orange')
plt.plot(input_sizes, theoretical_log, '--', label='Theoretical O(log n)', color='green')

plt.xlabel('Input Size (n)')
plt.ylabel(f'Execution Time for {iter_count} runs (seconds)')
plt.title('Measured vs Theoretical Time Complexities')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
