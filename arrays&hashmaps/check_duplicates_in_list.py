def find_duplicates_in_list(input_list):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
    seen = set()

    for item in input_list:
        if item in seen:
            return True
        seen.add(item)
    return False
print(find_duplicates_in_list([1, 2, 3, 4, 5]))  # Output: True

# time complexity: O(n)
# space complexity: O(n) for the seen set