'''Description
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]'''


def twoSum(nums, target):
    num_map = {}  # Dictionary to store value:index pairs

    for i, num in enumerate(nums):
        complement = target - num  # Find the needed number
        print(complement, num_map)
        if complement in num_map:
            return [num_map[complement], i]  # Return indices
        num_map[num] = i  # Store the current number in the dictionary
        print(num_map)

    return []  # Return empty if no pair is found
# Example usage:
print(twoSum([3, 4, 5, 6], 7))  # Output: [0, 1]