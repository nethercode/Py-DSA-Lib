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