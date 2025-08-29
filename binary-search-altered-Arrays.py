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
