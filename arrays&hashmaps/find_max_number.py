def find_max_number(numbers):
    """Returns the maximum number from a list of numbers.

    Args:
        numbers (list): A list of numerical values."""
        
    target = 0
    for number in numbers:
        if number > target:
            target = number
            return target
    
    return target

print(find_max_number([3, 5, 2, 8, 1]))