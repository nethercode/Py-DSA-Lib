from base import log
import algo

def test_0():
    log("This is a log message.")
    
def test_1():
    target_element = 42
    result = algo.linear_search(list_file, target_element)
    if result != -1:
        print(f"Linear Search Result: Element {target_element} found at index {result}.")
    else:
        print(f"Linear Search Result: Element {target_element} not found in the list.")

def test_2():
    target_element = 64
    result = algo.binary_search(list_file, target_element)
    if result != -1:
        print(f"Binary Search Result: Element {target_element} found at index {result}.")
    else:
        print(f"Binary Search Result: Element {target_element} not found in the list.")

def test_3():
    bubble_sorted_list = algo.bubble_sort(list_file)
    print("Bubble Sorted List:", bubble_sorted_list)

def test_4():
    insertion_sorted_list = algo.insertion_sort(list_file)
    print("Insertion Sorted List:", insertion_sorted_list)

def test_5():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    algo.quick_sort(numbers)
    print("Quick Sorted List:", numbers)

def test_6():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    merge_sorted_list = algo.merge_sort(numbers)
    print("Merge Sorted List:", merge_sorted_list)

def test_7():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    algo.selection_sort(numbers)
    print("Selection Sorted List:", numbers)

def test_8():
    with open(list_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    algo.heap_sort(numbers)
    print("Heap Sorted List:", numbers)

if __name__ == "__main__":
    list_file = "list.txt"
    test_0()
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()