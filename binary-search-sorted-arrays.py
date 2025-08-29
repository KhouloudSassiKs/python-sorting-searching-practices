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

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Recursive binary search on a list sorted in descending order.

    Parameters:
        sortedDescList (list): A list of elements sorted in descending order.
        target (int/any): The element to search for.
        low (int): Lower index (inclusive).
        high (int): Upper index (inclusive).

    Returns:
        int or None: The index of the target if found, otherwise None.
    """
def binary_search_recursive(sortedDescList, target, low, high):
    if low > high:
        return None  # Base case: not found

    mid = (low + high) // 2

    if sortedDescList[mid] == target:
        return mid
    elif target > sortedDescList[mid]:
        # If target is larger, it must be on the LEFT (since list is descending)
        return binary_search_recursive(sortedDescList, target, low, mid - 1)
    else:
        # If target is smaller, it must be on the RIGHT
        return binary_search_recursive(sortedDescList, target, mid + 1, high)

# Example usage
if __name__ == "__main__":
    sortedDescList = [20, 15, 11, 9, 7, 5, 3, 1]  # sorted in descending order

    print(binary_search_recursive(sortedDescList, 7, 0, len(sortedDescList) - 1))   # ➜ 4
    print(binary_search_recursive(sortedDescList, 21, 0, len(sortedDescList) - 1))  # ➜ None
    print(binary_search_recursive(sortedDescList, 20, 0, len(sortedDescList) - 1))  # ➜ 0
    print(binary_search_recursive(sortedDescList, 1, 0, len(sortedDescList) - 1))   # ➜ 7

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Finds an approximate root x such that func(x) ≈ 0 using binary search.

    Parameters:
        func: The continuous function to evaluate.
        left: Left endpoint of the search interval.
        right: Right endpoint of the search interval.
        epsilon: Acceptable difference between func(x) and 0.

    Returns:
        Approximate root x where func(x) ≈ 0.
    """
# Python program to find the value of 'x' where f(x) = 0 using Binary Search
import numpy as np

# Define a continuous function 'f'
# Example: f(x) = x^6 - 3x^4 + 4x^3 - 1
def f(x):
    return x**6 - 3 * x**4 + 4 * x**3 - 1

# Binary Search Function to find root
def binary_search(func, left, right, epsilon):
    while right - left > epsilon:
        middle = (left + right) / 2

        # If function value is close enough to zero, return the midpoint
        if np.isclose(func(middle), 0, atol=epsilon):
            return middle

        # Decide which half contains the root
        # If f(middle) > 0, root lies in [left, middle]; else in [middle, right]
        if func(middle) > 0:
            right = middle
        else:
            left = middle

    # Return midpoint as best approximation if exact zero not found
    return (left + right) / 2

# -----------------------------
# Parameters for the search
epsilon = 1e-6  # precision of approximation
start = -5      # left boundary of search interval
end = 5         # right boundary of search interval

# Perform binary search to find root
result = binary_search(f, start, end, epsilon)

print(f"x ≈ {result}, f(x) ≈ {f(result)}")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Finds an approximate x such that func(x) is close to a non null target value.

    Parameters:
        func: The function to evaluate.
        target: The desired target value of func(x).
        left: Left endpoint of the search interval.
        right: Right endpoint of the search interval.
        precision: Acceptable difference between func(x) and target.

    Returns:
        Approximate x such that func(x) ≈ target.
    """
# Python program to find the x value for which a given function reaches a target using Binary Search
import numpy as np

# Define a continuous function 'f'
def f(x):
    return x**4 - x**2 - 10

# Binary search function to find x such that f(x) ≈ target
def binary_search(func, target, left, right, precision):
    
    while (right - left) / 2 > precision:
        mid = (left + right) / 2

        # If the function value is close enough to the target, return mid
        if np.isclose(func(mid), target, atol=precision):
            return mid

        # Determine which half of the interval contains the target
        # Explanation of the “direction” logic:
        # - func(left) - target: direction from left to target
        # - func(mid) - target: direction from mid to target
        # If these directions are opposite, the target is between left and mid
        #      left --- target --- mid --- right
        # Else, the target is between mid and right
        #      left --- mid --- target --- right
        if (func(left) - target) * (func(mid) - target) < 0:
            right = mid  # target lies in [left, mid]
        else:
            left = mid   # target lies in [mid, right]

    # Return midpoint as best approximation if exact match not found
    return (left + right) / 2

# -----------------------------
# Example usage
epsilon = 1e-6  # precision of the approximation
target = 50      # target value to find
start = -5       # left boundary of search interval
end = 54         # right boundary of search interval

result = binary_search(f, target, start, end, epsilon)

print(f"x ≈ {result}, f(x) ≈ {f(result)}")
