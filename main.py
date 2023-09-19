from base import put_message as pm
from search import linear_search as lisf
from search import binary_search as bisf
from sort import bubble_sort as busf
from sort import insertion_sort as insf

def main_0():
    result = pm("Text can go here.")
    print(result)
    
def main_1():
    target_element = 42
    result = lisf(list_file, target_element)
    if result != -1:
        print(f"Linear Search Result: Element {target_element} found at index {result}.")
    else:
        print(f"Linear Search Result: Element {target_element} not found in the list.")

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