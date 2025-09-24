import random
import string


def merge_sort(data):
    """Perform merge sort on a list of strings (compare by first 3 characters)."""
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists into one, comparing only the first 3 characters."""
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][:3] <= right[right_index][:3]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def generate_random_strings(count=20, length=6):
    """Generate a list of random alphanumeric strings."""
    return [
        ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        for _ in range(count)
    ]


if __name__ == "__main__":
    # Generate random data
    data = generate_random_strings()

    print("\nOriginal list of random strings:")
    print(data)

    sorted_data = merge_sort(data)

    print("\nSorted list of random strings (by first 3 characters):")
    print(sorted_data)
