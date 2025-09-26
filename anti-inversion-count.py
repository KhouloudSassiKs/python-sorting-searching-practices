def count_anti_inversions(arr):
    """
    Count the number of anti-inversion pairs in an array.
    An anti-inversion pair is (i, j) such that i < j and arr[i] < arr[j].

    Args:
        arr (list[int]): Input list of integers.

    Returns:
        int: Total number of anti-inversion pairs.
    """
    if len(arr) <= 1:
        return 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Count anti-inversions in left, right, and across subarrays
    count = count_anti_inversions(left) + count_anti_inversions(right)
    merged, split_count = merge_count_anti_inversions(left, right)

    # Copy merged array back to original for consistency (optional)
    arr[:len(merged)] = merged

    return count + split_count


def merge_count_anti_inversions(left, right):
    """
    Merge two sorted arrays and count anti-inversions across them.

    Args:
        left (list[int]): Left sorted subarray.
        right (list[int]): Right sorted subarray.

    Returns:
        tuple: (merged sorted array, count of cross anti-inversions)
    """
    merged = []
    count = 0
    i = j = 0
    len_left = len(left)
    len_right = len(right)

    while i < len_left and j < len_right:
        if left[i] < right[j]:
            # All remaining elements in right[j:] form valid anti-inversions
            count += len_right - j
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count


if __name__ == "__main__":
    # Example usage
    test_array = [2, 4, 1, 3, 5]
    inv_count = count_anti_inversions(test_array)
    print(f'Number of anti-inversions in {test_array} is {inv_count}')  # Expected Output: 7
