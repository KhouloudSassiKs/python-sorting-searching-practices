  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Search for a target in a rotated sorted array that is originally sorted in a descending order.

    Args:
        nums (List[int]): Rotated array sorted in descending order.
        target (int): Value to search for.

    Returns:
        int: Index of target if found, otherwise -1.

    Approach:
        At each step, one half of the array is guaranteed to be sorted (descending).
        Find which half is sorted and check if the target is in it:
        - If yes, move the range to search within that half.
        - If no, search in the other half.
    """
def search_dec_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        
        # Found the target
        if nums[mid] == target:
            return mid
        
        # Left half is sorted (descending)
        if nums[left] >= nums[mid]:
            if nums[left] >= target > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted (descending)
        else:
            if nums[mid] >= target >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Execution examples:
"""
# Rotated descending array, target in the rotated half
print(search_dec_rotated([4, 3, 2, 1, 8, 7, 6, 5], 1))   # Expected output: 3

# Non-rotated descending array, target exists
print(search_dec_rotated([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))  # Expected output: 5

# Descending array, target not in the list
print(search_dec_rotated([5, 4, 3, 2, 1], 8))  # Expected output: -1

# Rotated descending array, target at rotation point
print(search_dec_rotated([3, 2, 1, 9, 8, 7, 6, 5, 4], 9))  # Expected output: 3

# Single-element array, target matches
print(search_dec_rotated([10], 10))  # Expected output: 0

# Single-element array, target not found
print(search_dec_rotated([10], 5))  # Expected output: -1

# Rotated descending array, target at the very end
print(search_dec_rotated([7, 6, 5, 4, 3, 2, 1, 9, 8], 8))  # Expected output: 8

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Find the first and last positions of a target in a sorted array.

    Args:
        nums (List[float]): Sorted array (ascending).
        target (float): Value to search for.

    Returns:
        List[int]: [first_index, last_index] if target exists, otherwise [-1, -1].

    Approach:
        Uses a modified recursive binary search to find boundaries efficiently.
        - `find_first=True` finds the first occurrence of target.
        - `find_first=False` finds the index after the last occurrence, then subtracts 1.
    """
def get_first_last_pos(nums, target):
    def binary_search(left, right, find_first):
        """Recursive binary search to find boundary index."""
        if left > right:
            return left

        mid = (left + right) // 2

        # If searching first occurrence, or target is less than mid, search left
        if nums[mid] > target or (find_first and nums[mid] == target):
            return binary_search(left, mid - 1, find_first)
        # Otherwise, search right
        else:
            return binary_search(mid + 1, right, find_first)

    # Find first and last occurrence
    first = binary_search(0, len(nums) - 1, True)
    last = binary_search(first, len(nums) - 1, False) - 1

    # Validate existence
    if first <= last:
        return [first, last]
    return [-1, -1]


# Example usage / tests

print(get_first_last_pos([3.14, 3.14, 6.28, 9.42], 3.14))  # [0, 1]
print(get_first_last_pos([3.14, 3.14, 6.28, 9.42], 4.13))  # [-1, -1]
print(get_first_last_pos([], 3.14))                        # [-1, -1]
print(get_first_last_pos([1,2,2,2,3,4], 2))               # [1, 3]
print(get_first_last_pos([1,2,2,2,3,4], 3))               # [4, 4]
