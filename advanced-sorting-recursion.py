import random


def find_kth_largest(nums, k):
    """
    Find the k-th largest element in a list using Quickselect.

    Args:
        nums (list[int]): List of integers.
        k (int): The k-th largest element to find (1-based index).

    Returns:
        int | None: The k-th largest element, or None if the list is empty.
    """
    if not nums:
        return None

    target_index = len(nums) - k  # index if sorted ascending
    left, right = 0, len(nums) - 1

    while True:
        pos = partition(nums, left, right)

        if pos == target_index:
            return nums[pos]
        elif pos > target_index:
            right = pos - 1
        else:
            left = pos + 1


def partition(nums, left, right):
    """
    Partition the array around a randomly chosen pivot.
    Elements < pivot move left, elements >= pivot move right.

    Args:
        nums (list[int]): List of integers.
        left (int): Left index of the current segment.
        right (int): Right index of the current segment.

    Returns:
        int: Final index of the pivot.
    """
    pivot_index = random.randint(left, right)
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    pivot = nums[right]

    store_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index += 1

    nums[store_index], nums[right] = nums[right], nums[store_index]
    return store_index


if __name__ == "__main__":
    # Example usage
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  
    # Expected output: 5

    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  
    # Expected output: 4
