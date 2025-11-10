def merge_two_sorted_lists(list1, list2):
    """approach: two pointers
    Merges two sorted lists into a single sorted list.
    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.
    Returns:
        list: A merged sorted list containing all elements from both input lists.

         
    """


    
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

print(merge_two_sorted_lists([1, 3, 5], [4, 2, 6]))  # 