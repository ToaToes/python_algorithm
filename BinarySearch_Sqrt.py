'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

'''

# To use a Binary Search:

def my_sqrt(x: int) -> int:
    if x < 2:
        return x  # Handle cases for 0 and 1 directly

    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1

    return right  # right will be the floor of the square root

# Example usage
print(my_sqrt(4))   # Output: 2
print(my_sqrt(8))   # Output: 2
print(my_sqrt(0))   # Output: 0
print(my_sqrt(1))   # Output: 1
print(my_sqrt(16))  # Output: 4
