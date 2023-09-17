from print_file import print_fn as pf
from linear_search_file import linear_search_fn as lisf
from binary_search_file import binary_search_fn as bisf
from bubble_sort_file import bubble_sort_fn as busf
from insertion_sort_file import insertion_sort_fn as insf

def main_0():
    result = pf("Hello from main.py")
    print(result)
    
def main_1():
    example_target_element = 42
    result = lisf(list_file, example_target_element)
    if result != -1:
        print(f"Linear Search Result: Element {example_target_element} found at index {result}.")
    else:
        print(f"Linear Search Result: Element {example_target_element} not found in the list.")

def main_2():
    target_element = 64
    result = bisf(list_file, target_element)
    if result != -1:
        print(f"Binary Search Result: Element {target_element} found at index {result}.")
    else:
        print(f"Binary Search Result: Element {target_element} not found in the list.")

def main_3():
    bubble_sorted_list = busf(list_file)
    print("Bubble Sorted List:", bubble_sorted_list)

def main_4():
    insertion_sorted_list = insf(list_file)
    print("Insertion Sorted List:", insertion_sorted_list)

if __name__ == "__main__":
    list_file = "list.txt"
    main_0()
    main_1()
    main_2()
    main_3()
    main_4()