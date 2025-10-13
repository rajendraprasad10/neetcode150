# Check if an array contains any duplicate elements. A hash set can efficiently track seen elements.

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))