def remove_duplicates(input_list):
    """
    Remove duplicates from a list while preserving the original order.

    Args:
        input_list (list): The list from which to remove duplicates.

    Returns:
        list: A new list with duplicates removed.
    """
    seen = set()
    result = []
    for num in input_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# time complexity: O(n) 
# space complexity: O(n) for the result list