def right_rorate_list(lst,k):

    if not lst:
        return lst
    return lst[-k:] + lst[:-k]

# Example usage:
example_list = [1, 2, 3, 4, 5]
rotated_list = right_rorate_list(example_list,2)
print(rotated_list)  # 

def left_rorate_list(lst,k):

    if not lst:
        return lst
    return lst[k:] + lst[:k]

print(left_rorate_list(example_list,2))  # [3, 4, 5, 1, 2]