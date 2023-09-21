def binary_search(file_path, target_element):
    with open(file_path, 'r') as file:
        input_list = [int(line.strip()) for line in file]

    left = 0
    right = len(input_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if input_list[mid] == target_element:
            return mid
        elif input_list[mid] < target_element:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def linear_search(file_path, target_element):
    with open(file_path, 'r') as file:
        input_list = [int(line.strip()) for line in file]
    
    for index, element in enumerate(input_list):
        if element == target_element:
            return index
    return -1

def bubble_sort(arr):
    with open(arr, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return numbers

def insertion_sort(arr):
    with open(arr, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

    return numbers

def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high

        while True:
            while left <= right and arr[left] <= pivot:
                left = left + 1
            while arr[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]
        return right

    def sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            sort(arr, low, pi - 1)
            sort(arr, pi + 1, high)

    sort(arr, 0, len(arr) - 1)

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        left = sort(left)
        right = sort(right)

        return merge(left, right)

    return sort(arr)

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
