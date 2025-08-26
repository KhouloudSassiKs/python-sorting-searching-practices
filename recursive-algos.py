""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Recursively sum the elements at even indexes of an array.

    Parameters:
        arr (list): The input array of numbers
        idx (int): The current index (default=0)

    Returns:
        int/float: Sum of elements at even indexes
"""
def recursive_sum_even(arr, idx=0):
    # Base case: if index is out of range
    if idx >= len(arr):
        return 0

    # Recursive case: add current element + move two steps forward
    return arr[idx] + recursive_sum_even(arr, idx + 2)


# Example usage:
nums = [10, 20, 30, 40, 50, 60]
print(recursive_sum_even(nums))  # Output: 90 (10 + 30 + 50)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    if num < 0:
        return None  # Factorial not defined for negative numbers
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
"""
def factorial(num):
    
    Compute factorial of a non-negative integer recursively.

    Parameters:
        num (int): A non-negative integer

    Returns:
        int: factorial of num
        None: if input is invalid (negative)
   

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    if num < 0:
        return None  # Factorial not defined for negative numbers
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)
"""
def factorials(nums):
    results = []
    for num in nums:
        f = factorial(num)
        if f is not None:
            results.append(f)
        else:
            results.append("Error")
    return results


# Example usage:
print(factorials([5, 0, 3, -2]))  
# Output: [120, 1, 6, 'Error']
