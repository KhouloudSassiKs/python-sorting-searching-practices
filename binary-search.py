"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Iterative binary search on a sorted list.

    Parameters:
        sortedList (list): A list of elements sorted in ascending order.
        target (any): The element to search for.

    Returns:
        int or None: The index of the target if found, otherwise None.
    """
def binary_search_iterative(sortedList, target):  
    left = 0
    right = len(sortedList) - 1  # inclusive upper bound
    # Loop until the search space is exhausted
    while left <= right:
        mid = (left + right) // 2  # middle index

        # Check if the middle element is the target
        if sortedList[mid] == target:
            return mid
        # If the target is smaller, ignore the right half
        elif target < sortedList[mid]:
            right = mid - 1
        # If the target is larger, ignore the left half
        else:
            left = mid + 1

    # Target not found
    return None
  
# Example usage using the if __name__ == "__main__": python idiom allowing import in other modules:
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]

    print(binary_search_iterative(nums, 7))   # return: 3
    print(binary_search_iterative(nums, 2))   # Output: None
    print(binary_search_iterative(nums, 11))  # Output: 5
    print(binary_search_iterative(nums, 1))   # Output: 0
