import random
import string


def merge_sort(arr):
    """Perform merge sort on a list of characters."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists of characters into one sorted list."""
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append remaining elements (if any)
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def generate_random_chars(count=20):
    """Generate a list of random lowercase alphabets."""
    return [random.choice(string.ascii_lowercase) for _ in range(count)]


if __name__ == "__main__":
    data = generate_random_chars()

    print("Original list:\n", data)

    sorted_data = merge_sort(data)

    print("\nSorted list:\n", sorted_data)
