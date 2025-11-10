def count_odd_and_even(arr):
    odd_count = 0
    even_count = 0
    
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return odd_count, even_count


print(count_odd_and_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: (3, 3)
# time complexity: O(n)
# space complexity: O(1)