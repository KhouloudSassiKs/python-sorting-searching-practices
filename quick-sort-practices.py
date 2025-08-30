import random
 """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Helper function to partition the list based on a pivot:
    It arranges elements around the pivot:
        - For ascending order (desc=False): elements <= pivot are on the left, > pivot on the right
        - For descending order (desc=True): elements >= pivot are on the left, < pivot on the right

    Args:
        lst (list): List to be partitioned
        low (int): Starting index of the sublist
        high (int): Ending index of the sublist (pivot element)
        desc (bool): True for descending sort, False for ascending sort

    Returns:
        int: Index of the pivot after partitioning
    """
def partition(lst, low, high, desc):
    pivot = lst[high]  # Choose the last element as pivot
    idx = low - 1       # Index of smaller element for swapping

    # Traverse through the sublist
    for j in range(low, high):
        # Ascending order condition
        if lst[j] >= pivot and desc == False:
            idx += 1
            lst[idx], lst[j] = lst[j], lst[idx]  # Swap elements

        # Descending order condition
        elif lst[j] <= pivot and desc == True:
            idx += 1
            lst[idx], lst[j] = lst[j], lst[idx]  # Swap elements

    # Place pivot in its correct position
    lst[idx + 1], lst[high] = lst[high], lst[idx + 1]

    return idx + 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Quick Sort function that recursively sorts the list in-place.

    Args:
        lst (list): List to be sorted
        low (int): Starting index of the sublist
        high (int): Ending index of the sublist
        desc (bool): True for descending sort, False for ascending sort
    """
def quick_sort(lst, low, high, desc):
    # Base case: if the list has only one element, it is already sorted
    if len(lst) == 1:
        return lst

    # Perform sorting only if the sublist has more than one element
    if low < high:
        # Partition the list and get the pivot index
        pi = partition(lst, low, high, desc)
        # Recursively sort elements before pivot
        quick_sort(lst, low, pi - 1, desc)
        # Recursively sort elements after pivot
        quick_sort(lst, pi + 1, high, desc)


# ---------------------- Example Usage ----------------------

# Generate a list of numbers from 1 to 50
numbers = [i for i in range(1, 51)]

# Print the original list
print("Original List:", numbers)

# Sort and print the list in descending order using Quick Sort
quick_sort(numbers, 0, len(numbers) - 1, True)
print("Sorted List Desc order:", numbers)

# Sort and print the list in ascending order using Quick Sort
quick_sort(numbers, 0, len(numbers) - 1, False)
print("Sorted List Asc order:", numbers)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Recursively sorts a list in ascending order using the Quick Sort algorithm.

    Args:
        arr (list): The list of numbers to sort.

    Returns:
        list: Sorted list in ascending order.
    """
import random
def quick_sort(arr):
    # Base case: lists with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose pivot as the middle element
    pivot = arr[len(arr) // 2]

    # Partition the list into three parts
    left = [x for x in arr if x < pivot]     # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]    # Elements greater than pivot

    # Recursively sort left and right, then combine output
    return quick_sort(left) + middle + quick_sort(right)

# ---------------------- Example Usage ----------------------
    # Generate a random list of 15 integers between 1 and 50
    random_numbers = [random.randint(1, 50) for _ in range(15)]
    print("Unsorted List:", random_numbers)

    # Sort the list using Quick Sort
    sorted_list = quick_sort(random_numbers)
    print("Sorted List:", sorted_list)
